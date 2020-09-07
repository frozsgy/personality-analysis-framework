import React from "react";
import { Menu } from "semantic-ui-react";
import { withRouter } from "react-router-dom";

const BottomMenu = () => {
  
    return (
      <Menu secondary>
        <Menu.Item
            name="Akademik Arkaplan"
            url="akademik-arkaplan"
            active={window.location.pathname === "/akademik-arkaplan"}
            
        />

        <Menu.Item
            name="Gizlilik Bildirimi"
            url="gizlilik-bildirimi"
            active={window.location.pathname === "/gizlilik-bildirimi"}
            
        />

        <Menu.Menu position="right">
         
        </Menu.Menu>
      </Menu>
    );
  
}

export default withRouter(BottomMenu);
