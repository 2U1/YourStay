import React from 'react';
import { Menu } from 'antd';
import { Link } from 'react-router-dom';

const SubMenu = Menu.SubMenu;
const MenuItemGroup = Menu.ItemGroup;

function LeftMenu(props) {
  return (
    <Menu mode={props.mode}>
    <SubMenu title={<span>Category</span>}>
      <MenuItemGroup title="Hotel">
        <Menu.Item key="setting:1" >
        <a href='/hotel'> Origin
        </a>
        </Menu.Item>
        <Menu.Item key="setting:2">
        <a href='/recommendhotel'> Recommend
          Score Page 
          </a>
        </Menu.Item>



        {/* <Menu.Item key="setting:2"></Menu.Item> */}
      </MenuItemGroup>
      {/* <MenuItemGroup title="Motel">
        <Menu.Item key="setting:3">Option 3</Menu.Item>
        <Menu.Item key="setting:4">Option 4</Menu.Item>
      </MenuItemGroup> */}
    </SubMenu>
  </Menu>
  )
}

export default LeftMenu