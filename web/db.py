import mysql.connector
import datetime

class DB():

    __verbose = False

    def __init__(self, CONFIG, verbose = False):
        self.__conn = mysql.connector.connect(user=CONFIG['database']['user'], password=CONFIG['database']['password'], host=CONFIG['database']['host'], database=CONFIG['database']['database'], autocommit=True)
        self.__cursor = self.__conn.cursor()
        self.__verbose = verbose

    def __del__(self):
        self.__conn.close()

    def create_db(self):
        """Creates the database and tables. This method should be called only during the installation.
        """
        try :
            self.__cursor.execute(''' CREATE TABLE IF NOT EXISTS users (id bigint NOT NULL UNIQUE, username text, access_token varchar(512), access_secret varchar(512), tweet_count integer) ''')
            self.__cursor.execute(''' CREATE TABLE IF NOT EXISTS results (id integer NOT NULL AUTO_INCREMENT , uid bigint NOT NULL, hash varchar(128) UNIQUE, score_o real, score_c real, score_e real, score_a real, score_n real, status varchar(32), auto_share boolean, survey boolean, PRIMARY KEY(id), FOREIGN KEY(uid) REFERENCES users(id)) ''')
            self.__cursor.execute('''  CREATE TABLE IF NOT EXISTS questionnaire (id integer NOT NULL AUTO_INCREMENT, r_id integer NOT NULL, q0 integer, q1 integer, q2 integer, q3 integer, q4 integer, q5 integer, q6 integer, q7 integer, q8 integer, q9 integer, q10 integer, q11 integer, q12 integer, q13 integer, q14 integer, q15 integer, q16 integer, q17 integer, q18 integer, q19 integer, q20 integer, q21 integer, q22 integer, q23 integer, q24 integer, q25 integer, q26 integer, q27 integer, q28 integer, q29 integer, q30 integer, q31 integer, q32 integer, q33 integer, q34 integer, q35 integer, q36 integer, q37 integer, q38 integer, q39 integer, q40 integer, q41 integer, q42 integer, q43 integer, q44 integer, q45 integer, q46 integer, q47 integer, q48 integer, q49 integer, score_o real, score_c real, score_e real, score_a real, score_n real, PRIMARY KEY(id), FOREIGN KEY(r_id) REFERENCES results(id)) ''')
        except:
            print('Cannot create DB')
        finally:
            self.__conn.commit()


    def check_if_user_exists(self, id):
        self.__cursor.execute(''' SELECT COUNT(*) from users WHERE id = %s ''', (id,))
        status = self.__cursor.fetchone()[0]
        return status == 1

    def add_user(self, id, username, access_token, access_secret, total_tweets = -1):
        res = True
        if self.check_if_user_exists(id):
            return res
        else :
            try:
                self.__cursor.execute(''' INSERT into users VALUES(%s,%s,%s,%s,%s) ''', (id, username, access_token, access_secret, total_tweets, ))
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
            self.__cursor.execute(''' UPDATE users SET access_token = %s, access_secret = %s WHERE id = %s ''', (access_token, access_secret, id,))
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
            auto_share_db = 0
            if auto_share is True:
                auto_share_db = 1
            self.__cursor.execute(''' INSERT into results VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ''', (None, uid, s_hash, 0, 0, 0, 0, 0, "INIT", auto_share_db, 0))
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
            self.__cursor.execute(''' UPDATE results SET score_o = %s, score_c = %s, score_e = %s, score_a = %s, score_n = %s, status = %s WHERE hash = %s ''', (float(ocean['o']), float(ocean['c']), float(ocean['e']), float(ocean['a']), float(ocean['n']), "FINISHED", s_hash,))
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
            self.__cursor.execute(''' SELECT access_token, access_secret from users WHERE id = %s ''', (id,))
            return self.__cursor.fetchone()
        except :
            return False

    def get_ocean_by_hash(self, hash):
        try:
            self.__cursor.execute(''' SELECT score_o, score_c, score_e, score_a, score_n from results WHERE hash = %s ''', (hash,))
            return self.__cursor.fetchone()
        except :
            return False

    def set_share_by_hash(self, hash):
        try:
            self.__cursor.execute(''' UPDATE results SET auto_share = %s WHERE hash = %s ''', (0, hash,))
            return self.__cursor.fetchone()
        except :
            return False

    def get_share_by_hash(self, hash):
        try:
            self.__cursor.execute(''' SELECT auto_share from results WHERE hash = %s ''', (hash,))
            return self.__cursor.fetchone()[0]
        except :
            return False

    def get_total_tweets_by_id(self, id):
        if self.check_if_user_exists(id) is False:
            return False
        try:
            self.__cursor.execute(''' SELECT tweet_count from users WHERE id = %s ''', (id,))
            return self.__cursor.fetchone()[0]
        except :
            return False

    def get_status_by_hash(self, hash):
        try:
            self.__cursor.execute(''' SELECT status from results WHERE hash = %s ''', (hash,))
            return self.__cursor.fetchone()[0]
        except :
            return False

    def get_uid_by_hash(self, hash):
        try:
            self.__cursor.execute(''' SELECT uid from results WHERE hash = %s ''', (hash,))
            return self.__cursor.fetchone()[0]
        except :
            return False

    def get_id_by_hash(self, hash):
        try:
            self.__cursor.execute(''' SELECT id from results WHERE hash = %s ''', (hash,))
            return self.__cursor.fetchone()[0]
        except :
            return False

    def get_survey_by_hash(self, hash):
        try:
            self.__cursor.execute(''' SELECT survey from results WHERE hash = %s ''', (hash,))
            return self.__cursor.fetchone()[0]
        except :
            return False

    def get_username_by_id(self, id):
        if self.check_if_user_exists(id) is False:
            return False
        try:
            self.__cursor.execute(''' SELECT username from users WHERE id = %s ''', (id,))
            return self.__cursor.fetchone()[0]
        except :
            return False

    def save_questionnaire(self, r_hash, responses, ocean):
        res = True
        try:
            data = (None, r_hash, *responses, ocean['o'], ocean['c'], ocean['e'], ocean['a'], ocean['n'])
            self.__cursor.execute(''' INSERT into questionnaire VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ''', data)
            self.__cursor.execute(''' UPDATE results SET survey = %s WHERE id = %s ''', (1, r_hash,))
            if self.__verbose:
                print("Questionnaire responses saved for hash %s" % s_hash)
        except:
            res = False
            print("Questionnaire responses could not be saved")
        finally:
            self.__conn.commit()
            return res