import React from "react";
import { Menu } from "semantic-ui-react";
import { withRouter } from "react-router-dom";

const BottomMenu = () => {
  return (
    <Menu secondary stackable>
      <Menu.Item
        name="Bilimsel Arkaplan"
        url="bilimsel-arkaplan"
        active={window.location.pathname === "/bilimsel-arkaplan"}
      />

      <Menu.Item
        name="Gizlilik Bildirimi"
        url="gizlilik-bildirimi"
        active={window.location.pathname === "/gizlilik-bildirimi"}
      />

      <Menu.Menu position="right">
        <Menu.Item
          name="İletişim"
          url="iletisim"
          active={window.location.pathname === "/iletisim"}
        />
      </Menu.Menu>
    </Menu>
  );
};

export default withRouter(BottomMenu);
