import sqlite3
import os
import datetime

class DB():

    __verbose = False
    __location = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, verbose = False):
        self.__conn = sqlite3.connect(self.__location + '/personality.db')
        self.__cursor = self.__conn.cursor()
        self.__verbose = verbose

    def __del__(self):
        self.__conn.close()

    def create_db(self):
        """Creates the database and tables. This method should be called only during the installation.
        """
        try :
            self.__cursor.execute(''' CREATE TABLE IF NOT EXISTS users (id bigint NOT NULL UNIQUE , username text, access_token varchar, access_secret varchar, shared boolean, survey boolean) ''')
            self.__cursor.execute(''' CREATE TABLE IF NOT EXISTS results (id integer PRIMARY KEY, uid bigint NOT NULL, hash varchar UNQIUE, score_o real, score_c real, score_e real, score_a real, score_n real, status varchar, auto_share boolean, FOREIGN KEY(uid) REFERENCES users(id)) ''')
        except:
            print('Cannot create DB')
        finally:
            self.__conn.commit()


    def check_if_user_exists(self, id):
        self.__cursor.execute(''' SELECT COUNT(*) from users WHERE id = ? ''', (id,))
        status = self.__cursor.fetchone()[0]
        return status == 1

    def add_user(self, id, username, access_token, access_secret):
        res = True
        if self.check_if_user_exists(id):
            return res
        else :
            try:
                self.__cursor.execute(''' INSERT into users VALUES(?,?,?,?,?,?) ''', (id, username, access_token, access_secret, 0, 0,))
                if self.__verbose:
                    print("User %s (%s) created succesfully" % (username, id))
            except:
                res = False
                if self.__verbose:
                    print("User %s (%s) cannot be inserted" % (username, id))
            finally:
                self.__conn.commit()
                return res

    def update_tokens(self, id, access_token, access_secret):
        res = True
        try:
            self.__cursor.execute(''' UPDATE users SET access_token = ?, access_secret = ? WHERE id = ? ''', (access_token, access_secret, id,))
            if self.__verbose:
                print("Tokens updated for uid %s" % id)
        except:
            res = False
            print("Tokens could not be updated")
        finally:
            self.__conn.commit()
            return res

    def insert_ocean(self, s_hash, uid, auto_share = False):
        res = True
        try:
            self.__cursor.execute(''' INSERT into results VALUES(?,?,?,?,?,?,?,?,?,?) ''', (None, uid, s_hash, 0, 0, 0, 0, 0, "INIT", auto_share))
            if self.__verbose:
                print("OCEAN scores initialized for hash %s" % s_hash)
        except:
            res = False
            print("OCEAN scores could not be initialized")
        finally:
            self.__conn.commit()
            return res

    def finalize_ocean(self, s_hash, ocean):
        res = True
        try:
            self.__cursor.execute(''' UPDATE results SET score_o = ?, score_c = ?, score_e = ?, score_a = ?, score_n = ?, status = ? WHERE hash = ? ''', (ocean['o'], ocean['c'], ocean['e'], ocean['a'], ocean['n'], "FINISHED", s_hash,))
            if self.__verbose:
                print("OCEAN scores set for hash %s" % s_hash)
        except:
            res = False
            print("OCEAN scores could not be set")
        finally:
            self.__conn.commit()
            return res

    def get_tokens_by_id(self, id):
        if self.check_if_user_exists(id) is False:
            return False
        try:
            self.__cursor.execute(''' SELECT access_token, access_secret from users WHERE id = ? ''', (id,))
            return self.__cursor.fetchone()
        except :
            return False

    def get_ocean_by_hash(self, hash):
        try:
            self.__cursor.execute(''' SELECT score_o, score_c, score_e, score_a, score_n from results WHERE hash = ? ''', (hash,))
            return self.__cursor.fetchone()
        except :
            return False

    def get_status_by_hash(self, hash):
        try:
            self.__cursor.execute(''' SELECT status from results WHERE hash = ? ''', (hash,))
            return self.__cursor.fetchone()[0]
        except :
            return False

    def get_uid_by_hash(self, hash):
        try:
            self.__cursor.execute(''' SELECT uid from results WHERE hash = ? ''', (hash,))
            return self.__cursor.fetchone()[0]
        except :
            return False

    def get_username_by_id(self, id):
        if self.check_if_user_exists(id) is False:
            return False
        try:
            self.__cursor.execute(''' SELECT username from users WHERE id = ? ''', (id,))
            return self.__cursor.fetchone()[0]
        except :
            return False