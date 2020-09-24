import React from "react";
import { Menu } from "semantic-ui-react";
import { withRouter, useHistory } from "react-router-dom";

const BottomMenu = () => {
  const history = useHistory();
  return (
    <Menu secondary stackable>
      <Menu.Item
        name="Bilimsel Arkaplan"
        active={window.location.pathname === "/bilimsel-arkaplan"}
        onClick={() => history.push("bilimsel-arkaplan")}
      />

      <Menu.Item
        name="Gizlilik Bildirimi"
        active={window.location.pathname === "/gizlilik-bildirimi"}
        onClick={() => history.push("gizlilik-bildirimi")}
      />

      <Menu.Menu position="right">
        <Menu.Item
          name="İletişim"
          active={window.location.pathname === "/iletisim"}
          onClick={() => history.push("iletisim")}
        />
      </Menu.Menu>
    </Menu>
  );
};

export default withRouter(BottomMenu);
