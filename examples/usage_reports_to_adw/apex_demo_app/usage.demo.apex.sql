prompt --application/set_environment
set define off verify off feedback off
whenever sqlerror exit sql.sqlcode rollback
--------------------------------------------------------------------------------
--
-- ORACLE Application Express (APEX) export file
--
-- You should run the script connected to SQL*Plus as the Oracle user
-- APEX_200200 or as the owner (parsing schema) of the application.
--
-- NOTE: Calls to apex_application_install override the defaults below.
--
--------------------------------------------------------------------------------
begin
wwv_flow_api.import_begin (
 p_version_yyyy_mm_dd=>'2020.10.01'
,p_release=>'20.2.0.00.20'
,p_default_workspace_id=>9710643564672463
,p_default_application_id=>100
,p_default_id_offset=>0
,p_default_owner=>'USAGE'
);
end;
/
 
prompt APPLICATION 100 - OCI Usage and Cost Report
--
-- Application Export:
--   Application:     100
--   Name:            OCI Usage and Cost Report
--   Date and Time:   15:21 Monday March 29, 2021
--   Exported By:     ADIZOHAR
--   Flashback:       0
--   Export Type:     Application Export
--     Pages:                     10
--       Items:                  101
--       Computations:            28
--       Processes:                8
--       Regions:                 66
--       Buttons:                 10
--     Shared Components:
--       Logic:
--         App Settings:           1
--         Build Options:          1
--       Navigation:
--         Lists:                  3
--         Breadcrumbs:            1
--           Entries:              1
--       Security:
--         Authentication:         1
--         Authorization:          3
--         ACL Roles:              3
--       User Interface:
--         Themes:                 1
--         Templates:
--           Page:                 9
--           Region:              16
--           Label:                7
--           List:                12
--           Popup LOV:            1
--           Calendar:             1
--           Breadcrumb:           1
--           Button:               3
--           Report:              10
--         LOVs:                   3
--         Shortcuts:              1
--       Globalization:
--       Reports:
--       E-Mail:
--     Supporting Objects:  Excluded
--   Version:         20.2.0.00.20
--   Instance ID:     9710412995014033
--

prompt --application/delete_application
begin
wwv_flow_api.remove_flow(wwv_flow.g_flow_id);
end;
/
prompt --application/create_application
begin
wwv_flow_api.create_flow(
 p_id=>wwv_flow.g_flow_id
,p_owner=>nvl(wwv_flow_application_install.get_schema,'USAGE')
,p_name=>nvl(wwv_flow_application_install.get_application_name,'OCI Usage and Cost Report')
,p_alias=>nvl(wwv_flow_application_install.get_application_alias,'100')
,p_page_view_logging=>'YES'
,p_page_protection_enabled_y_n=>'Y'
,p_checksum_salt=>'875FACC9195C359EC344917E15564C1D485DD4068144173F315788BE04F6A9F4'
,p_bookmark_checksum_function=>'SH512'
,p_accept_old_checksums=>false
,p_compatibility_mode=>'19.2'
,p_flow_language=>'en'
,p_flow_language_derived_from=>'FLOW_PRIMARY_LANGUAGE'
,p_allow_feedback_yn=>'Y'
,p_direction_right_to_left=>'N'
,p_flow_image_prefix => nvl(wwv_flow_application_install.get_image_prefix,'')
,p_documentation_banner=>'Application created from create application wizard 2020.02.27.'
,p_authentication=>'PLUGIN'
,p_authentication_id=>wwv_flow_api.id(9714428553687881)
,p_application_tab_set=>1
,p_logo_type=>'T'
,p_logo_text=>'OCI Usage and Cost Report'
,p_app_builder_icon_name=>'app-icon.svg'
,p_public_user=>'APEX_PUBLIC_USER'
,p_proxy_server=>nvl(wwv_flow_application_install.get_proxy,'')
,p_no_proxy_domains=>nvl(wwv_flow_application_install.get_no_proxy_domains,'')
,p_flow_version=>'Release 21.04.04'
,p_flow_status=>'AVAILABLE_W_EDIT_LINK'
,p_flow_unavailable_text=>'This application is currently unavailable at this time.'
,p_exact_substitutions_only=>'Y'
,p_browser_cache=>'N'
,p_browser_frame=>'D'
,p_runtime_api_usage=>'T'
,p_security_scheme=>'MUST_NOT_BE_PUBLIC_USER'
,p_rejoin_existing_sessions=>'N'
,p_csv_encoding=>'Y'
,p_auto_time_zone=>'N'
,p_friendly_url=>'N'
,p_substitution_string_01=>'APP_NAME'
,p_substitution_value_01=>'OCI Usage and Cost Report'
,p_last_updated_by=>'ADIZOHAR'
,p_last_upd_yyyymmddhh24miss=>'20210329152118'
,p_file_prefix => nvl(wwv_flow_application_install.get_static_app_file_prefix,'')
,p_files_version=>3
,p_ui_type_name => null
,p_print_server_type=>'INSTANCE'
);
end;
/
prompt --application/shared_components/navigation/lists/desktop_navigation_menu
begin
wwv_flow_api.create_list(
 p_id=>wwv_flow_api.id(9715221966687890)
,p_name=>'Desktop Navigation Menu'
,p_list_status=>'PUBLIC'
);
wwv_flow_api.create_list_item(
 p_id=>wwv_flow_api.id(9855175484688380)
,p_list_item_display_sequence=>10
,p_list_item_link_text=>'Home'
,p_list_item_link_target=>'f?p=&APP_ID.:1:&APP_SESSION.::&DEBUG.:'
,p_list_item_icon=>'fa-home'
,p_list_item_current_type=>'TARGET_PAGE'
);
wwv_flow_api.create_list_item(
 p_id=>wwv_flow_api.id(9904311570733816)
,p_list_item_display_sequence=>30
,p_list_item_link_text=>'Current State'
,p_list_item_link_target=>'f?p=&APP_ID.:2:&SESSION.::&DEBUG.'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'2'
);
wwv_flow_api.create_list_item(
 p_id=>wwv_flow_api.id(9975684784919488)
,p_list_item_display_sequence=>40
,p_list_item_link_text=>'Usage Over Time'
,p_list_item_link_target=>'f?p=&APP_ID.:3:&SESSION.::&DEBUG.'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'3'
);
wwv_flow_api.create_list_item(
 p_id=>wwv_flow_api.id(11701489744773179)
,p_list_item_display_sequence=>50
,p_list_item_link_text=>'Cost Analysis'
,p_list_item_link_target=>'f?p=&APP_ID.:4:&SESSION.::&DEBUG.::::'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'4'
);
wwv_flow_api.create_list_item(
 p_id=>wwv_flow_api.id(12030298425075968)
,p_list_item_display_sequence=>60
,p_list_item_link_text=>'Cost Over Time'
,p_list_item_link_target=>'f?p=&APP_ID.:5:&SESSION.::&DEBUG.'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'5'
);
wwv_flow_api.create_list_item(
 p_id=>wwv_flow_api.id(16371791258522236)
,p_list_item_display_sequence=>80
,p_list_item_link_text=>'Rate Card'
,p_list_item_link_target=>'f?p=&APP_ID.:7:&SESSION.::&DEBUG.'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'7'
);
wwv_flow_api.create_list_item(
 p_id=>wwv_flow_api.id(12630315850041592)
,p_list_item_display_sequence=>90
,p_list_item_link_text=>'Data Statistics'
,p_list_item_link_target=>'f?p=&APP_ID.:6:&SESSION.::&DEBUG.::::'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'6'
);
end;
/
prompt --application/shared_components/navigation/lists/desktop_navigation_bar
begin
wwv_flow_api.create_list(
 p_id=>wwv_flow_api.id(9843375564688197)
,p_name=>'Desktop Navigation Bar'
,p_list_status=>'PUBLIC'
);
wwv_flow_api.create_list_item(
 p_id=>wwv_flow_api.id(9891645046688560)
,p_list_item_display_sequence=>10
,p_list_item_link_text=>'&APP_USER.'
,p_list_item_link_target=>'#'
,p_list_item_icon=>'fa-user'
,p_list_text_02=>'has-username'
,p_list_item_current_type=>'TARGET_PAGE'
);
wwv_flow_api.create_list_item(
 p_id=>wwv_flow_api.id(9892185251688560)
,p_list_item_display_sequence=>20
,p_list_item_link_text=>'---'
,p_list_item_link_target=>'separator'
,p_parent_list_item_id=>wwv_flow_api.id(9891645046688560)
,p_list_item_current_type=>'TARGET_PAGE'
);
wwv_flow_api.create_list_item(
 p_id=>wwv_flow_api.id(9892578174688561)
,p_list_item_display_sequence=>30
,p_list_item_link_text=>'Sign Out'
,p_list_item_link_target=>'&LOGOUT_URL.'
,p_list_item_icon=>'fa-sign-out'
,p_parent_list_item_id=>wwv_flow_api.id(9891645046688560)
,p_list_item_current_type=>'TARGET_PAGE'
);
end;
/
prompt --application/shared_components/navigation/lists/access_control
begin
wwv_flow_api.create_list(
 p_id=>wwv_flow_api.id(9894239269688568)
,p_name=>'Access Control'
,p_list_status=>'PUBLIC'
,p_required_patch=>wwv_flow_api.id(9845173009688250)
);
wwv_flow_api.create_list_item(
 p_id=>wwv_flow_api.id(9894627901688568)
,p_list_item_display_sequence=>10
,p_list_item_link_text=>'Users'
,p_list_item_link_target=>'f?p=&APP_ID.:10011:&SESSION.::&DEBUG.:RP:::'
,p_list_item_icon=>'fa-users'
,p_list_text_01=>'Change access control settings and disable access control'
,p_list_item_current_type=>'TARGET_PAGE'
);
end;
/
prompt --application/shared_components/files/app_icon_svg
begin
wwv_flow_api.g_varchar2_table := wwv_flow_api.empty_varchar2_table;
wwv_flow_api.g_varchar2_table(1) := '3C73766720786D6C6E733D22687474703A2F2F7777772E77332E6F72672F323030302F7376672220786D6C6E733A786C696E6B3D22687474703A2F2F7777772E77332E6F72672F313939392F786C696E6B222076696577426F783D223020302036342036';
wwv_flow_api.g_varchar2_table(2) := '34223E3C646566733E3C7374796C653E2E636C732D317B66696C6C3A75726C282372616469616C2D6772616469656E74293B7D2E636C732D327B6F7061636974793A302E313B7D2E636C732D332C2E636C732D347B66696C6C3A236666663B7D2E636C73';
wwv_flow_api.g_varchar2_table(3) := '2D337B6F7061636974793A302E363B7D3C2F7374796C653E3C72616469616C4772616469656E742069643D2272616469616C2D6772616469656E74222063783D223332222063793D222E30352220723D22363422206772616469656E74556E6974733D22';
wwv_flow_api.g_varchar2_table(4) := '7573657253706163654F6E557365223E3C73746F70206F66667365743D2230222073746F702D636F6C6F723D2223666666222073746F702D6F7061636974793D22302E3135222F3E3C73746F70206F66667365743D222E35222073746F702D636F6C6F72';
wwv_flow_api.g_varchar2_table(5) := '3D2223666666222073746F702D6F7061636974793D22302E31222F3E3C73746F70206F66667365743D2231222073746F702D636F6C6F723D2223666666222073746F702D6F7061636974793D2230222F3E3C2F72616469616C4772616469656E743E3C73';
wwv_flow_api.g_varchar2_table(6) := '796D626F6C2069643D22616D6269656E742D6C69676874696E67222076696577426F783D22302030203634203634223E3C7061746820636C6173733D22636C732D312220643D224D302030683634763634682D36347A222F3E3C2F73796D626F6C3E3C2F';
wwv_flow_api.g_varchar2_table(7) := '646566733E3C7469746C653E6261722D6C696E652D63686172743C2F7469746C653E3C726563742077696474683D22363422206865696768743D223634222066696C6C3D2223364538353938222F3E3C672069643D2269636F6E73223E3C706174682063';
wwv_flow_api.g_varchar2_table(8) := '6C6173733D22636C732D322220643D224D313920343668357631682D357A4D323620343668357631682D357A4D333320343668357631682D357A4D343020343668357631682D357A222F3E3C7061746820636C6173733D22636C732D332220643D224D31';
wwv_flow_api.g_varchar2_table(9) := '3920333868357638682D357A4D32362033326835763134682D357A4D33332033326835763134682D357A4D34302032376835763139682D357A222F3E3C6720636C6173733D22636C732D32223E3C636972636C652063783D2234322E35222063793D2232';
wwv_flow_api.g_varchar2_table(10) := '302E352220723D22312E35222F3E3C636972636C652063783D2233352E35222063793D2232352E352220723D22312E35222F3E3C636972636C652063783D2232382E35222063793D2232352E352220723D22312E35222F3E3C636972636C652063783D22';
wwv_flow_api.g_varchar2_table(11) := '32312E35222063793D2233312E352220723D22312E35222F3E3C7061746820643D224D32312E3832352033312E3837396C2D2E36352D2E37353820372E31342D362E31323168372E3032356C362E3836392D342E3930372E3538322E3831342D372E3133';
wwv_flow_api.g_varchar2_table(12) := '3120352E303933682D362E3937356C2D362E383620352E3837397A222F3E3C2F673E3C636972636C6520636C6173733D22636C732D34222063783D2234322E35222063793D2231392E352220723D22312E35222F3E3C636972636C6520636C6173733D22';
wwv_flow_api.g_varchar2_table(13) := '636C732D34222063783D2233352E35222063793D2232342E352220723D22312E35222F3E3C636972636C6520636C6173733D22636C732D34222063783D2232382E35222063793D2232342E352220723D22312E35222F3E3C636972636C6520636C617373';
wwv_flow_api.g_varchar2_table(14) := '3D22636C732D34222063783D2232312E35222063793D2233302E352220723D22312E35222F3E3C7061746820636C6173733D22636C732D342220643D224D32312E3832352033302E3837396C2D2E36352D2E37353820372E31342D362E31323168372E30';
wwv_flow_api.g_varchar2_table(15) := '32356C362E3836392D342E3930372E3538322E3831342D372E31333120352E303933682D362E3937356C2D362E383620352E3837397A222F3E3C2F673E3C7573652077696474683D22363422206865696768743D2236342220786C696E6B3A687265663D';
wwv_flow_api.g_varchar2_table(16) := '2223616D6269656E742D6C69676874696E67222069643D226C69676874696E67222F3E3C2F7376673E';
wwv_flow_api.create_app_static_file(
 p_id=>wwv_flow_api.id(9844603424688246)
,p_file_name=>'app-icon.svg'
,p_mime_type=>'image/svg+xml'
,p_file_charset=>'utf-8'
,p_file_content => wwv_flow_api.varchar2_to_blob(wwv_flow_api.g_varchar2_table)
);
end;
/
prompt --application/shared_components/files/app_icon_css
begin
wwv_flow_api.g_varchar2_table := wwv_flow_api.empty_varchar2_table;
wwv_flow_api.g_varchar2_table(1) := '2E6170702D69636F6E207B0A202020206261636B67726F756E642D696D6167653A2075726C286170702D69636F6E2E737667293B0A202020206261636B67726F756E642D7265706561743A206E6F2D7265706561743B0A202020206261636B67726F756E';
wwv_flow_api.g_varchar2_table(2) := '642D73697A653A20636F7665723B0A202020206261636B67726F756E642D706F736974696F6E3A203530253B0A202020206261636B67726F756E642D636F6C6F723A20233645383539383B0A7D';
wwv_flow_api.create_app_static_file(
 p_id=>wwv_flow_api.id(9844979456688249)
,p_file_name=>'app-icon.css'
,p_mime_type=>'text/css'
,p_file_charset=>'utf-8'
,p_file_content => wwv_flow_api.varchar2_to_blob(wwv_flow_api.g_varchar2_table)
);
end;
/
prompt --application/plugin_settings
begin
wwv_flow_api.create_plugin_setting(
 p_id=>wwv_flow_api.id(1182329746069638)
,p_plugin_type=>'ITEM TYPE'
,p_plugin=>'NATIVE_SINGLE_CHECKBOX'
,p_attribute_01=>'Y'
,p_attribute_02=>'N'
);
wwv_flow_api.create_plugin_setting(
 p_id=>wwv_flow_api.id(9712418602687875)
,p_plugin_type=>'REGION TYPE'
,p_plugin=>'NATIVE_DISPLAY_SELECTOR'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_plugin_setting(
 p_id=>wwv_flow_api.id(9712655311687877)
,p_plugin_type=>'REGION TYPE'
,p_plugin=>'NATIVE_CSS_CALENDAR'
);
wwv_flow_api.create_plugin_setting(
 p_id=>wwv_flow_api.id(9712999902687878)
,p_plugin_type=>'ITEM TYPE'
,p_plugin=>'NATIVE_RICH_TEXT_EDITOR'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_plugin_setting(
 p_id=>wwv_flow_api.id(9713244397687878)
,p_plugin_type=>'REGION TYPE'
,p_plugin=>'NATIVE_IR'
,p_attribute_01=>'IG'
);
wwv_flow_api.create_plugin_setting(
 p_id=>wwv_flow_api.id(9713516201687878)
,p_plugin_type=>'ITEM TYPE'
,p_plugin=>'NATIVE_YES_NO'
,p_attribute_01=>'Y'
,p_attribute_03=>'N'
,p_attribute_05=>'SWITCH'
);
wwv_flow_api.create_plugin_setting(
 p_id=>wwv_flow_api.id(9714184222687879)
,p_plugin_type=>'ITEM TYPE'
,p_plugin=>'NATIVE_COLOR_PICKER'
,p_attribute_01=>'modern'
);
wwv_flow_api.create_plugin_setting(
 p_id=>wwv_flow_api.id(16424473540395392)
,p_plugin_type=>'ITEM TYPE'
,p_plugin=>'NATIVE_STAR_RATING'
,p_attribute_01=>'fa-star'
,p_attribute_04=>'#VALUE#'
);
end;
/
prompt --application/shared_components/security/authorizations/administration_rights
begin
wwv_flow_api.create_security_scheme(
 p_id=>wwv_flow_api.id(9846864434688256)
,p_name=>'Administration Rights'
,p_scheme_type=>'NATIVE_IS_IN_GROUP'
,p_attribute_01=>'Administrator'
,p_attribute_02=>'A'
,p_error_message=>'Insufficient privileges, user is not an Administrator'
,p_caching=>'BY_USER_BY_PAGE_VIEW'
);
end;
/
prompt --application/shared_components/security/authorizations/reader_rights
begin
wwv_flow_api.create_security_scheme(
 p_id=>wwv_flow_api.id(9846978588688256)
,p_name=>'Reader Rights'
,p_scheme_type=>'NATIVE_FUNCTION_BODY'
,p_attribute_01=>wwv_flow_string.join(wwv_flow_t_varchar2(
'if nvl(apex_app_setting.get_value(',
'   p_name => ''ACCESS_CONTROL_SCOPE''),''x'') = ''ALL_USERS'' then',
'    -- allow user not in the ACL to access the application',
'    return true;',
'else',
'    -- require user to have at least one role',
'    return apex_acl.has_user_any_roles (',
'        p_application_id => :APP_ID, ',
'        p_user_name      => :APP_USER);',
'end if;'))
,p_error_message=>'You are not authorized to view this application, either because you have not been granted access, or your account has been locked. Please contact the application administrator.'
,p_caching=>'BY_USER_BY_SESSION'
);
end;
/
prompt --application/shared_components/security/authorizations/contribution_rights
begin
wwv_flow_api.create_security_scheme(
 p_id=>wwv_flow_api.id(9847099143688256)
,p_name=>'Contribution Rights'
,p_scheme_type=>'NATIVE_IS_IN_GROUP'
,p_attribute_01=>'Administrator,Contributor'
,p_attribute_02=>'A'
,p_error_message=>'Insufficient privileges, user is not a Contributor'
,p_caching=>'BY_USER_BY_PAGE_VIEW'
);
end;
/
prompt --application/shared_components/security/app_access_control/administrator
begin
wwv_flow_api.create_acl_role(
 p_id=>wwv_flow_api.id(9846484124688252)
,p_static_id=>'ADMINISTRATOR'
,p_name=>'Administrator'
,p_description=>'Role assigned to application administrators.'
);
end;
/
prompt --application/shared_components/security/app_access_control/contributor
begin
wwv_flow_api.create_acl_role(
 p_id=>wwv_flow_api.id(9846651600688256)
,p_static_id=>'CONTRIBUTOR'
,p_name=>'Contributor'
,p_description=>'Role assigned to application contributors.'
);
end;
/
prompt --application/shared_components/security/app_access_control/reader
begin
wwv_flow_api.create_acl_role(
 p_id=>wwv_flow_api.id(9846725360688256)
,p_static_id=>'READER'
,p_name=>'Reader'
,p_description=>'Role assigned to application readers.'
);
end;
/
prompt --application/shared_components/navigation/navigation_bar
begin
null;
end;
/
prompt --application/shared_components/logic/application_settings
begin
wwv_flow_api.create_app_setting(
 p_id=>wwv_flow_api.id(9848198626688270)
,p_name=>'ACCESS_CONTROL_SCOPE'
,p_value=>'ACL_ONLY'
,p_is_required=>'N'
,p_valid_values=>'ACL_ONLY, ALL_USERS'
,p_on_upgrade_keep_value=>true
,p_required_patch=>wwv_flow_api.id(9845173009688250)
,p_comments=>'The default access level given to authenticated users who are not in the access control list'
);
end;
/
prompt --application/shared_components/navigation/tabs/standard
begin
null;
end;
/
prompt --application/shared_components/navigation/tabs/parent
begin
null;
end;
/
prompt --application/shared_components/user_interface/lovs/access_roles
begin
wwv_flow_api.create_list_of_values(
 p_id=>wwv_flow_api.id(9870260534688478)
,p_lov_name=>'ACCESS_ROLES'
,p_lov_query=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select role_name d, role_id r',
'from APEX_APPL_ACL_ROLES where application_id = :APP_ID ',
'order by 1'))
,p_source_type=>'LEGACY_SQL'
,p_location=>'LOCAL'
);
end;
/
prompt --application/shared_components/user_interface/lovs/email_username_format
begin
wwv_flow_api.create_list_of_values(
 p_id=>wwv_flow_api.id(9877994421688486)
,p_lov_name=>'EMAIL_USERNAME_FORMAT'
,p_lov_query=>'.'||wwv_flow_api.id(9877994421688486)||'.'
,p_location=>'STATIC'
);
wwv_flow_api.create_static_lov_data(
 p_id=>wwv_flow_api.id(9878236831688487)
,p_lov_disp_sequence=>1
,p_lov_disp_value=>'Email Addresses'
,p_lov_return_value=>'EMAIL'
);
end;
/
prompt --application/shared_components/user_interface/lovs/login_remember_username
begin
wwv_flow_api.create_list_of_values(
 p_id=>wwv_flow_api.id(9850484666688331)
,p_lov_name=>'LOGIN_REMEMBER_USERNAME'
,p_lov_query=>'.'||wwv_flow_api.id(9850484666688331)||'.'
,p_location=>'STATIC'
);
wwv_flow_api.create_static_lov_data(
 p_id=>wwv_flow_api.id(9850859526688332)
,p_lov_disp_sequence=>10
,p_lov_disp_value=>'Remember username'
,p_lov_return_value=>'Y'
);
end;
/
prompt --application/pages/page_groups
begin
wwv_flow_api.create_page_group(
 p_id=>wwv_flow_api.id(9848481419688273)
,p_group_name=>'Administration'
);
end;
/
prompt --application/comments
begin
null;
end;
/
prompt --application/shared_components/navigation/breadcrumbs/breadcrumb
begin
wwv_flow_api.create_menu(
 p_id=>wwv_flow_api.id(9714771272687883)
,p_name=>'Breadcrumb'
);
wwv_flow_api.create_menu_option(
 p_id=>wwv_flow_api.id(9714932633687886)
,p_short_name=>'Home'
,p_link=>'f?p=&APP_ID.:1:&APP_SESSION.::&DEBUG.'
,p_page_id=>1
);
end;
/
prompt --application/shared_components/navigation/breadcrumbentry
begin
null;
end;
/
prompt --application/shared_components/user_interface/templates/page/left_side_column
begin
wwv_flow_api.create_template(
 p_id=>wwv_flow_api.id(9715583223687903)
,p_theme_id=>42
,p_name=>'Left Side Column'
,p_internal_name=>'LEFT_SIDE_COLUMN'
,p_is_popup=>false
,p_javascript_code_onload=>'apex.theme42.initializePage.leftSideCol();'
,p_header_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<!DOCTYPE html>',
'<html class="no-js #RTL_CLASS# page-&APP_PAGE_ID. app-&APP_ALIAS." lang="&BROWSER_LANGUAGE." #TEXT_DIRECTION#>',
'<head>',
'  <meta http-equiv="x-ua-compatible" content="IE=edge" />',
'  <meta charset="utf-8">',
'  <title>#TITLE#</title>',
'  #APEX_CSS#',
'  #THEME_CSS#',
'  #TEMPLATE_CSS#',
'  #THEME_STYLE_CSS#',
'  #APPLICATION_CSS#',
'  #PAGE_CSS#',
'  #FAVICONS#',
'  #HEAD#',
'  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
'</head>',
'<body class="t-PageBody t-PageBody--showLeft t-PageBody--hideActions no-anim #PAGE_CSS_CLASSES#" #TEXT_DIRECTION# #ONLOAD# id="t_PageBody">',
'<a href="#main" id="t_Body_skipToContent">&APP_TEXT$UI_PAGE_SKIP_TO_CONTENT.</a>',
'#FORM_OPEN#',
'<header class="t-Header" id="t_Header">',
'  #REGION_POSITION_07#',
'  <div class="t-Header-branding" role="banner">',
'    <div class="t-Header-controls">',
'      <button class="t-Button t-Button--icon t-Button--header t-Button--headerTree" aria-label="#EXPAND_COLLAPSE_NAV_LABEL#" title="#EXPAND_COLLAPSE_NAV_LABEL#" id="t_Button_navControl" type="button"><span class="t-Header-controlsIcon" aria-hidden="t'
||'rue"></span></button>',
'    </div>',
'    <div class="t-Header-logo">',
'      <a href="#HOME_LINK#" class="t-Header-logo-link">#LOGO#</a>',
'    </div>',
'    <div class="t-Header-navBar">#NAVIGATION_BAR#</div>',
'  </div>',
'  <div class="t-Header-nav">#TOP_GLOBAL_NAVIGATION_LIST##REGION_POSITION_06#</div>',
'</header>',
''))
,p_box=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body">',
'#SIDE_GLOBAL_NAVIGATION_LIST#',
'  <div class="t-Body-main">',
'    <div class="t-Body-title" id="t_Body_title">#REGION_POSITION_01#</div>',
'    <div class="t-Body-side" id="t_Body_side">#REGION_POSITION_02#</div>',
'    <div class="t-Body-content" id="t_Body_content">',
'      <main id="main" class="t-Body-mainContent">',
'        #SUCCESS_MESSAGE##NOTIFICATION_MESSAGE##GLOBAL_NOTIFICATION#',
'        <div class="t-Body-fullContent">#REGION_POSITION_08#</div>',
'        <div class="t-Body-contentInner">#BODY#</div>',
'      </main>',
'      <footer class="t-Footer" role="contentinfo">',
'        <div class="t-Footer-body">',
'          <div class="t-Footer-content">#REGION_POSITION_05#</div>',
'          <div class="t-Footer-apex">',
'            <div class="t-Footer-version">#APP_VERSION#</div>',
'            <div class="t-Footer-customize">#CUSTOMIZE#</div>',
'            #BUILT_WITH_LOVE_USING_APEX#',
'          </div>',
'        </div>',
'        <div class="t-Footer-top">',
'          <a href="#top" class="t-Footer-topButton" id="t_Footer_topButton"><span class="a-Icon icon-up-chevron"></span></a>',
'        </div>',
'      </footer>',
'    </div>',
'  </div>',
'</div>',
'<div class="t-Body-inlineDialogs">#REGION_POSITION_04#</div>'))
,p_footer_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#FORM_CLOSE#',
'#DEVELOPER_TOOLBAR#',
'#APEX_JAVASCRIPT#',
'#GENERATED_CSS#',
'#THEME_JAVASCRIPT#',
'#TEMPLATE_JAVASCRIPT#',
'#APPLICATION_JAVASCRIPT#',
'#PAGE_JAVASCRIPT#  ',
'#GENERATED_JAVASCRIPT#',
'</body>',
'</html>'))
,p_success_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--success t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Success" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-header">',
'          <h2 class="t-Alert-title">#SUCCESS_MESSAGE#</h2>',
'        </div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Success'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_notification_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--warning t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Notification" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-body">#MESSAGE#</div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Notification'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_navigation_bar=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<ul class="t-NavigationBar" data-mode="classic">',
'  <li class="t-NavigationBar-item">',
'    <span class="t-Button t-Button--icon t-Button--noUI t-Button--header t-Button--navBar t-Button--headerUser">',
'      <span class="t-Icon a-Icon icon-user"></span>',
'      <span class="t-Button-label">&APP_USER.</span>',
'    </span>',
'  </li>#BAR_BODY#',
'</ul>'))
,p_navbar_entry=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-NavigationBar-item">',
'  <a class="t-Button t-Button--icon t-Button--header t-Button--navBar" href="#LINK#">',
'    <span class="t-Icon #IMAGE#"></span>',
'    <span class="t-Button-label">#TEXT#</span>',
'  </a>',
'</li>'))
,p_region_table_cattributes=>' summary="" cellpadding="0" border="0" cellspacing="0" width="100%"'
,p_breadcrumb_def_reg_pos=>'REGION_POSITION_01'
,p_theme_class_id=>17
,p_error_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Alert t-Alert--danger t-Alert--wizard t-Alert--defaultIcons">',
'  <div class="t-Alert-wrap">',
'    <div class="t-Alert-icon">',
'      <span class="t-Icon"></span>',
'    </div>',
'    <div class="t-Alert-content">',
'      <div class="t-Alert-body">',
'        <h3>#MESSAGE#</h3>',
'        <p>#ADDITIONAL_INFO#</p>',
'        <div class="t-Alert-inset">#TECHNICAL_INFO#</div>',
'      </div>',
'    </div>',
'    <div class="t-Alert-buttons">',
'      <button onclick="#BACK_LINK#" class="t-Button t-Button--hot w50p t-Button--large" type="button">#OK#</button>',
'    </div>',
'  </div>',
'</div>'))
,p_grid_type=>'FIXED'
,p_grid_max_columns=>12
,p_grid_always_use_max_columns=>true
,p_grid_has_column_span=>true
,p_grid_always_emit=>true
,p_grid_emit_empty_leading_cols=>true
,p_grid_emit_empty_trail_cols=>false
,p_grid_default_label_col_span=>2
,p_grid_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="container">',
'#ROWS#',
'</div>'))
,p_grid_row_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="row">',
'#COLUMNS#',
'</div>'))
,p_grid_column_template=>'<div class="col col-#COLUMN_SPAN_NUMBER# #CSS_CLASSES#" #ATTRIBUTES#>#CONTENT#</div>'
,p_grid_first_column_attributes=>'alpha'
,p_grid_last_column_attributes=>'omega'
,p_dialog_js_init_code=>'apex.navigation.dialog(#PAGE_URL#,{title:#TITLE#,height:#DIALOG_HEIGHT#,width:#DIALOG_WIDTH#,maxWidth:#DIALOG_MAX_WIDTH#,modal:#IS_MODAL#,dialog:#DIALOG#,#DIALOG_ATTRIBUTES#},#DIALOG_CSS_CLASSES#,#TRIGGERING_ELEMENT#);'
,p_dialog_js_close_code=>'apex.navigation.dialog.close(#IS_MODAL#,#TARGET#);'
,p_dialog_js_cancel_code=>'apex.navigation.dialog.cancel(#IS_MODAL#);'
,p_dialog_browser_frame=>'MODAL'
,p_reference_id=>2525196570560608698
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9715827652687913)
,p_page_template_id=>wwv_flow_api.id(9715583223687903)
,p_name=>'Content Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>8
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9716105766687914)
,p_page_template_id=>wwv_flow_api.id(9715583223687903)
,p_name=>'Breadcrumb Bar'
,p_placeholder=>'REGION_POSITION_01'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9716489868687914)
,p_page_template_id=>wwv_flow_api.id(9715583223687903)
,p_name=>'Left Column'
,p_placeholder=>'REGION_POSITION_02'
,p_has_grid_support=>false
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>4
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9716738027687914)
,p_page_template_id=>wwv_flow_api.id(9715583223687903)
,p_name=>'Inline Dialogs'
,p_placeholder=>'REGION_POSITION_04'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9717047018687914)
,p_page_template_id=>wwv_flow_api.id(9715583223687903)
,p_name=>'Footer'
,p_placeholder=>'REGION_POSITION_05'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>8
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9717389192687914)
,p_page_template_id=>wwv_flow_api.id(9715583223687903)
,p_name=>'Page Navigation'
,p_placeholder=>'REGION_POSITION_06'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9717626782687915)
,p_page_template_id=>wwv_flow_api.id(9715583223687903)
,p_name=>'Page Header'
,p_placeholder=>'REGION_POSITION_07'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9717953082687915)
,p_page_template_id=>wwv_flow_api.id(9715583223687903)
,p_name=>'Before Content Body'
,p_placeholder=>'REGION_POSITION_08'
,p_has_grid_support=>true
,p_glv_new_row=>false
,p_max_fixed_grid_columns=>8
);
end;
/
prompt --application/shared_components/user_interface/templates/page/left_and_right_side_columns
begin
wwv_flow_api.create_template(
 p_id=>wwv_flow_api.id(9718391330687953)
,p_theme_id=>42
,p_name=>'Left and Right Side Columns'
,p_internal_name=>'LEFT_AND_RIGHT_SIDE_COLUMNS'
,p_is_popup=>false
,p_javascript_code_onload=>'apex.theme42.initializePage.bothSideCols();'
,p_header_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<!DOCTYPE html>',
'<html class="no-js #RTL_CLASS# page-&APP_PAGE_ID. app-&APP_ALIAS." lang="&BROWSER_LANGUAGE." #TEXT_DIRECTION#>',
'<head>',
'  <meta http-equiv="x-ua-compatible" content="IE=edge" />',
'  <meta charset="utf-8">  ',
'  <title>#TITLE#</title>',
'  #APEX_CSS#',
'  #THEME_CSS#',
'  #TEMPLATE_CSS#',
'  #THEME_STYLE_CSS#',
'  #APPLICATION_CSS#',
'  #PAGE_CSS#',
'  #FAVICONS#',
'  #HEAD#',
'  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>',
'</head>',
'<body class="t-PageBody t-PageBody--showLeft no-anim #PAGE_CSS_CLASSES#" #TEXT_DIRECTION# #ONLOAD# id="t_PageBody">',
'<a href="#main" id="t_Body_skipToContent">&APP_TEXT$UI_PAGE_SKIP_TO_CONTENT.</a>',
'#FORM_OPEN#',
'<header class="t-Header" id="t_Header">',
'  #REGION_POSITION_07#',
'  <div class="t-Header-branding" role="banner">',
'    <div class="t-Header-controls">',
'      <button class="t-Button t-Button--icon t-Button--header t-Button--headerTree" aria-label="#EXPAND_COLLAPSE_NAV_LABEL#" title="#EXPAND_COLLAPSE_NAV_LABEL#" id="t_Button_navControl" type="button"><span class="t-Header-controlsIcon" aria-hidden="t'
||'rue"></span></button>',
'    </div>',
'    <div class="t-Header-logo">',
'      <a href="#HOME_LINK#" class="t-Header-logo-link">#LOGO#</a>',
'    </div>',
'    <div class="t-Header-navBar">#NAVIGATION_BAR#</div>',
'  </div>',
'  <div class="t-Header-nav">',
'    #TOP_GLOBAL_NAVIGATION_LIST#',
'    #REGION_POSITION_06#',
'  </div>',
'</header>',
''))
,p_box=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body">',
'#SIDE_GLOBAL_NAVIGATION_LIST#',
'  <div class="t-Body-main">',
'    <div class="t-Body-title" id="t_Body_title">#REGION_POSITION_01#</div>',
'    <div class="t-Body-side" id="t_Body_side">#REGION_POSITION_02#</div>',
'    <div class="t-Body-content" id="t_Body_content">',
'      <main id="main" class="t-Body-mainContent">',
'        #SUCCESS_MESSAGE##NOTIFICATION_MESSAGE##GLOBAL_NOTIFICATION#',
'        <div class="t-Body-fullContent">#REGION_POSITION_08#</div>',
'        <div class="t-Body-contentInner">#BODY#</div>',
'      </main>',
'      <footer class="t-Footer" role="contentinfo">',
'        <div class="t-Footer-body">',
'          <div class="t-Footer-content">#REGION_POSITION_05#</div>',
'          <div class="t-Footer-apex">',
'            <div class="t-Footer-version">#APP_VERSION#</div>',
'            <div class="t-Footer-customize">#CUSTOMIZE#</div>',
'            #BUILT_WITH_LOVE_USING_APEX#',
'          </div>',
'        </div>',
'        <div class="t-Footer-top">',
'          <a href="#top" class="t-Footer-topButton" id="t_Footer_topButton"><span class="a-Icon icon-up-chevron"></span></a>',
'        </div>',
'      </footer>',
'    </div>',
'  </div>',
'  <div class="t-Body-actions" id="t_Body_actions">',
'    <button class="t-Body-actionsToggle" title="#EXPAND_COLLAPSE_SIDE_COL_LABEL#" id="t_Button_rightControlButton" type="button"><span class="t-Body-actionsControlsIcon" aria-hidden="true"></span></button>',
'    <div class="t-Body-actionsContent" role="complementary">#REGION_POSITION_03#</div>',
'  </div>',
'</div>',
'<div class="t-Body-inlineDialogs">#REGION_POSITION_04#</div>'))
,p_footer_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#FORM_CLOSE#',
'#DEVELOPER_TOOLBAR#',
'#APEX_JAVASCRIPT#',
'#GENERATED_CSS#',
'#THEME_JAVASCRIPT#',
'#TEMPLATE_JAVASCRIPT#',
'#APPLICATION_JAVASCRIPT#',
'#PAGE_JAVASCRIPT#  ',
'#GENERATED_JAVASCRIPT#',
'</body>',
'</html>'))
,p_success_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--success t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Success" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-header">',
'          <h2 class="t-Alert-title">#SUCCESS_MESSAGE#</h2>',
'        </div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Success'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_notification_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--warning t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Notification" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-body">#MESSAGE#</div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Notification'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_navigation_bar=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<ul class="t-NavigationBar" data-mode="classic">',
'  <li class="t-NavigationBar-item">',
'    <span class="t-Button t-Button--icon t-Button--noUI t-Button--header t-Button--navBar t-Button--headerUser">',
'      <span class="t-Icon a-Icon icon-user"></span>',
'      <span class="t-Button-label">&APP_USER.</span>',
'    </span>',
'  </li>#BAR_BODY#',
'</ul>'))
,p_navbar_entry=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-NavigationBar-item">',
'  <a class="t-Button t-Button--icon t-Button--header t-Button--navBar" href="#LINK#">',
'    <span class="t-Icon #IMAGE#"></span>',
'    <span class="t-Button-label">#TEXT#</span>',
'  </a>',
'</li>'))
,p_region_table_cattributes=>' summary="" cellpadding="0" border="0" cellspacing="0" width="100%"'
,p_sidebar_def_reg_pos=>'REGION_POSITION_03'
,p_breadcrumb_def_reg_pos=>'REGION_POSITION_01'
,p_theme_class_id=>17
,p_error_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Alert t-Alert--danger t-Alert--wizard t-Alert--defaultIcons">',
'  <div class="t-Alert-wrap">',
'    <div class="t-Alert-icon">',
'      <span class="t-Icon"></span>',
'    </div>',
'    <div class="t-Alert-content">',
'      <div class="t-Alert-body">',
'        <h3>#MESSAGE#</h3>',
'        <p>#ADDITIONAL_INFO#</p>',
'        <div class="t-Alert-inset">#TECHNICAL_INFO#</div>',
'      </div>',
'    </div>',
'    <div class="t-Alert-buttons">',
'      <button onclick="#BACK_LINK#" class="t-Button t-Button--hot w50p t-Button--large" type="button">#OK#</button>',
'    </div>',
'  </div>',
'</div>'))
,p_grid_type=>'FIXED'
,p_grid_max_columns=>12
,p_grid_always_use_max_columns=>true
,p_grid_has_column_span=>true
,p_grid_always_emit=>true
,p_grid_emit_empty_leading_cols=>true
,p_grid_emit_empty_trail_cols=>false
,p_grid_default_label_col_span=>2
,p_grid_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="container">',
'#ROWS#',
'</div>'))
,p_grid_row_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="row">',
'#COLUMNS#',
'</div>'))
,p_grid_column_template=>'<div class="col col-#COLUMN_SPAN_NUMBER# #CSS_CLASSES#" #ATTRIBUTES#>#CONTENT#</div>'
,p_grid_first_column_attributes=>'alpha'
,p_grid_last_column_attributes=>'omega'
,p_dialog_js_init_code=>'apex.navigation.dialog(#PAGE_URL#,{title:#TITLE#,height:#DIALOG_HEIGHT#,width:#DIALOG_WIDTH#,maxWidth:#DIALOG_MAX_WIDTH#,modal:#IS_MODAL#,dialog:#DIALOG#,#DIALOG_ATTRIBUTES#},#DIALOG_CSS_CLASSES#,#TRIGGERING_ELEMENT#);'
,p_dialog_js_close_code=>'apex.navigation.dialog.close(#IS_MODAL#,#TARGET#);'
,p_dialog_js_cancel_code=>'apex.navigation.dialog.cancel(#IS_MODAL#);'
,p_dialog_browser_frame=>'MODAL'
,p_reference_id=>2525203692562657055
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9718624492687954)
,p_page_template_id=>wwv_flow_api.id(9718391330687953)
,p_name=>'Content Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>6
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9718927700687954)
,p_page_template_id=>wwv_flow_api.id(9718391330687953)
,p_name=>'Breadcrumb Bar'
,p_placeholder=>'REGION_POSITION_01'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9719269251687954)
,p_page_template_id=>wwv_flow_api.id(9718391330687953)
,p_name=>'Left Column'
,p_placeholder=>'REGION_POSITION_02'
,p_has_grid_support=>false
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>3
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9719569131687954)
,p_page_template_id=>wwv_flow_api.id(9718391330687953)
,p_name=>'Right Column'
,p_placeholder=>'REGION_POSITION_03'
,p_has_grid_support=>false
,p_glv_new_row=>false
,p_max_fixed_grid_columns=>3
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9719891330687954)
,p_page_template_id=>wwv_flow_api.id(9718391330687953)
,p_name=>'Inline Dialogs'
,p_placeholder=>'REGION_POSITION_04'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9720135315687954)
,p_page_template_id=>wwv_flow_api.id(9718391330687953)
,p_name=>'Footer'
,p_placeholder=>'REGION_POSITION_05'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>6
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9720455411687955)
,p_page_template_id=>wwv_flow_api.id(9718391330687953)
,p_name=>'Page Navigation'
,p_placeholder=>'REGION_POSITION_06'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9720729588687955)
,p_page_template_id=>wwv_flow_api.id(9718391330687953)
,p_name=>'Page Header'
,p_placeholder=>'REGION_POSITION_07'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9721050296687955)
,p_page_template_id=>wwv_flow_api.id(9718391330687953)
,p_name=>'Before Content Body'
,p_placeholder=>'REGION_POSITION_08'
,p_has_grid_support=>true
,p_glv_new_row=>false
,p_max_fixed_grid_columns=>6
);
end;
/
prompt --application/shared_components/user_interface/templates/page/login
begin
wwv_flow_api.create_template(
 p_id=>wwv_flow_api.id(9721413857687955)
,p_theme_id=>42
,p_name=>'Login'
,p_internal_name=>'LOGIN'
,p_is_popup=>false
,p_javascript_code_onload=>'apex.theme42.initializePage.appLogin();'
,p_header_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<!DOCTYPE html>',
'<html class="no-js #RTL_CLASS# page-&APP_PAGE_ID. app-&APP_ALIAS." lang="&BROWSER_LANGUAGE." #TEXT_DIRECTION#>',
'<head>',
'  <meta http-equiv="x-ua-compatible" content="IE=edge" />',
'  <meta charset="utf-8">',
'  <title>#TITLE#</title>',
'  #APEX_CSS#',
'  #THEME_CSS#',
'  #TEMPLATE_CSS#',
'  #THEME_STYLE_CSS#',
'  #APPLICATION_CSS#',
'  #PAGE_CSS#',
'  #FAVICONS#',
'  #HEAD#',
'  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
'</head>',
'<body class="t-PageBody--login no-anim #PAGE_CSS_CLASSES#" #TEXT_DIRECTION# #ONLOAD#>',
'#FORM_OPEN#'))
,p_box=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body">',
'  #REGION_POSITION_01#',
'  #SUCCESS_MESSAGE##NOTIFICATION_MESSAGE##GLOBAL_NOTIFICATION#',
'  <div class="t-Body-wrap">',
'    <div class="t-Body-col t-Body-col--main">',
'      <div class="t-Login-container" role="main">#BODY#</div>',
'    </div>',
'  </div>',
'</div>'))
,p_footer_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#FORM_CLOSE#',
'#DEVELOPER_TOOLBAR#',
'#APEX_JAVASCRIPT#',
'#GENERATED_CSS#',
'#THEME_JAVASCRIPT#',
'#TEMPLATE_JAVASCRIPT#',
'#APPLICATION_JAVASCRIPT#',
'#PAGE_JAVASCRIPT#  ',
'#GENERATED_JAVASCRIPT#',
'</body>',
'</html>'))
,p_success_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--success t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Success" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-header">',
'          <h2 class="t-Alert-title">#SUCCESS_MESSAGE#</h2>',
'        </div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Success'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_notification_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--warning t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Notification" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-body">#MESSAGE#</div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Notification'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_region_table_cattributes=>' summary="" cellpadding="0" border="0" cellspacing="0" width="100%"'
,p_breadcrumb_def_reg_pos=>'REGION_POSITION_01'
,p_theme_class_id=>6
,p_error_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Alert t-Alert--danger t-Alert--wizard t-Alert--defaultIcons">',
'  <div class="t-Alert-wrap">',
'    <div class="t-Alert-icon">',
'      <span class="t-Icon"></span>',
'    </div>',
'    <div class="t-Alert-content">',
'      <div class="t-Alert-body">',
'        <h3>#MESSAGE#</h3>',
'        <p>#ADDITIONAL_INFO#</p>',
'        <div class="t-Alert-inset">#TECHNICAL_INFO#</div>',
'      </div>',
'    </div>',
'    <div class="t-Alert-buttons">',
'      <button onclick="#BACK_LINK#" class="t-Button t-Button--hot w50p t-Button--large" type="button">#OK#</button>',
'    </div>',
'  </div>',
'</div>'))
,p_grid_type=>'FIXED'
,p_grid_max_columns=>12
,p_grid_always_use_max_columns=>true
,p_grid_has_column_span=>true
,p_grid_always_emit=>true
,p_grid_emit_empty_leading_cols=>true
,p_grid_emit_empty_trail_cols=>false
,p_grid_default_label_col_span=>2
,p_grid_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="container">',
'#ROWS#',
'</div>'))
,p_grid_row_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="row">',
'#COLUMNS#',
'</div>'))
,p_grid_column_template=>'<div class="col col-#COLUMN_SPAN_NUMBER# #CSS_CLASSES#" #ATTRIBUTES#>#CONTENT#</div>'
,p_grid_first_column_attributes=>'alpha'
,p_grid_last_column_attributes=>'omega'
,p_dialog_js_init_code=>'apex.navigation.dialog(#PAGE_URL#,{title:#TITLE#,height:#DIALOG_HEIGHT#,width:#DIALOG_WIDTH#,maxWidth:#DIALOG_MAX_WIDTH#,modal:#IS_MODAL#,dialog:#DIALOG#,#DIALOG_ATTRIBUTES#},#DIALOG_CSS_CLASSES#,#TRIGGERING_ELEMENT#);'
,p_dialog_js_close_code=>'apex.navigation.dialog.close(#IS_MODAL#,#TARGET#);'
,p_dialog_js_cancel_code=>'apex.navigation.dialog.cancel(#IS_MODAL#);'
,p_dialog_browser_frame=>'MODAL'
,p_reference_id=>2099711150063350616
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9721763100687956)
,p_page_template_id=>wwv_flow_api.id(9721413857687955)
,p_name=>'Content Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9722084410687956)
,p_page_template_id=>wwv_flow_api.id(9721413857687955)
,p_name=>'Body Header'
,p_placeholder=>'REGION_POSITION_01'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
end;
/
prompt --application/shared_components/user_interface/templates/page/master_detail
begin
wwv_flow_api.create_template(
 p_id=>wwv_flow_api.id(9722224555687956)
,p_theme_id=>42
,p_name=>'Marquee'
,p_internal_name=>'MASTER_DETAIL'
,p_is_popup=>false
,p_javascript_file_urls=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#IMAGE_PREFIX#libraries/apex/#MIN_DIRECTORY#widget.stickyTableHeader#MIN#.js?v=#APEX_VERSION#',
'#IMAGE_PREFIX#libraries/apex/#MIN_DIRECTORY#widget.apexTabs#MIN#.js?v=#APEX_VERSION#'))
,p_javascript_code_onload=>'apex.theme42.initializePage.masterDetail();'
,p_header_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<!DOCTYPE html>',
'<html class="no-js #RTL_CLASS# page-&APP_PAGE_ID. app-&APP_ALIAS." lang="&BROWSER_LANGUAGE." #TEXT_DIRECTION#>',
'<head>',
'  <meta http-equiv="x-ua-compatible" content="IE=edge" />',
'  <meta charset="utf-8">',
'  <title>#TITLE#</title>',
'  #APEX_CSS#',
'  #THEME_CSS#',
'  #TEMPLATE_CSS#',
'  #THEME_STYLE_CSS#',
'  #APPLICATION_CSS#',
'  #PAGE_CSS#',
'  #FAVICONS#',
'  #HEAD#',
'  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
'</head>',
'<body class="t-PageBody t-PageBody--masterDetail t-PageBody--hideLeft no-anim #PAGE_CSS_CLASSES#" #TEXT_DIRECTION# #ONLOAD# id="t_PageBody">',
'<a href="#main" id="t_Body_skipToContent">&APP_TEXT$UI_PAGE_SKIP_TO_CONTENT.</a>',
'#FORM_OPEN#',
'<header class="t-Header" id="t_Header">',
'  #REGION_POSITION_07#',
'  <div class="t-Header-branding" role="banner">',
'    <div class="t-Header-controls">',
'      <button class="t-Button t-Button--icon t-Button--header t-Button--headerTree" aria-label="#EXPAND_COLLAPSE_NAV_LABEL#" title="#EXPAND_COLLAPSE_NAV_LABEL#" id="t_Button_navControl" type="button"><span class="t-Header-controlsIcon" aria-hidden="t'
||'rue"></span></button>',
'    </div>',
'    <div class="t-Header-logo">',
'      <a href="#HOME_LINK#" class="t-Header-logo-link">#LOGO#</a>',
'    </div>',
'    <div class="t-Header-navBar">',
'      #NAVIGATION_BAR#',
'    </div>',
'  </div>',
'  <div class="t-Header-nav">',
'    #TOP_GLOBAL_NAVIGATION_LIST#',
'    #REGION_POSITION_06#',
'  </div>',
'</header>'))
,p_box=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body">',
'  #SIDE_GLOBAL_NAVIGATION_LIST#',
'  <div class="t-Body-main">',
'    <div class="t-Body-title" id="t_Body_title">#REGION_POSITION_01#</div>',
'    <div class="t-Body-content" id="t_Body_content">',
'      <main id="main" class="t-Body-mainContent">',
'        #SUCCESS_MESSAGE##NOTIFICATION_MESSAGE##GLOBAL_NOTIFICATION#',
'        <div class="t-Body-fullContent">#REGION_POSITION_08#</div>',
'        <div class="t-Body-info" id="t_Body_info">#REGION_POSITION_02#</div>',
'        <div class="t-Body-contentInner" role="main">#BODY#</div>',
'      </main>',
'      <footer class="t-Footer" role="contentinfo">',
'        <div class="t-Footer-body">',
'          <div class="t-Footer-content">#REGION_POSITION_05#</div>',
'          <div class="t-Footer-apex">',
'            <div class="t-Footer-version">#APP_VERSION#</div>',
'            <div class="t-Footer-customize">#CUSTOMIZE#</div>',
'            #BUILT_WITH_LOVE_USING_APEX#',
'          </div>',
'        </div>',
'        <div class="t-Footer-top">',
'          <a href="#top" class="t-Footer-topButton" id="t_Footer_topButton"><span class="a-Icon icon-up-chevron"></span></a>',
'        </div>',
'      </footer>',
'    </div>',
'  </div>',
'  <div class="t-Body-actions" id="t_Body_actions">',
'    <button class="t-Body-actionsToggle" title="#EXPAND_COLLAPSE_SIDE_COL_LABEL#" id="t_Button_rightControlButton" type="button"><span class="t-Body-actionsControlsIcon" aria-hidden="true"></span></button>',
'    <div class="t-Body-actionsContent" role="complementary">#REGION_POSITION_03#</div>',
'  </div>',
'</div>',
'<div class="t-Body-inlineDialogs">#REGION_POSITION_04#</div>'))
,p_footer_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#FORM_CLOSE#',
'#DEVELOPER_TOOLBAR#',
'#APEX_JAVASCRIPT#',
'#GENERATED_CSS#',
'#THEME_JAVASCRIPT#',
'#TEMPLATE_JAVASCRIPT#',
'#APPLICATION_JAVASCRIPT#',
'#PAGE_JAVASCRIPT#  ',
'#GENERATED_JAVASCRIPT#',
'</body>',
'</html>'))
,p_success_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--success t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Success" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-header">',
'          <h2 class="t-Alert-title">#SUCCESS_MESSAGE#</h2>',
'        </div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Success'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_notification_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--warning t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Notification" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-body">#MESSAGE#</div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Notification'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_navigation_bar=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<ul class="t-NavigationBar" data-mode="classic">',
'  <li class="t-NavigationBar-item">',
'    <span class="t-Button t-Button--icon t-Button--noUI t-Button--header t-Button--navBar t-Button--headerUser">',
'      <span class="t-Icon a-Icon icon-user"></span>',
'      <span class="t-Button-label">&APP_USER.</span>',
'    </span>',
'  </li>#BAR_BODY#',
'</ul>'))
,p_navbar_entry=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-NavigationBar-item">',
'  <a class="t-Button t-Button--icon t-Button--header t-Button--navBar" href="#LINK#">',
'    <span class="t-Icon #IMAGE#"></span>',
'    <span class="t-Button-label">#TEXT#</span>',
'  </a>',
'</li>'))
,p_region_table_cattributes=>' summary="" cellpadding="0" border="0" cellspacing="0" width="100%"'
,p_sidebar_def_reg_pos=>'REGION_POSITION_03'
,p_breadcrumb_def_reg_pos=>'REGION_POSITION_01'
,p_theme_class_id=>17
,p_error_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Alert t-Alert--danger t-Alert--wizard t-Alert--defaultIcons">',
'  <div class="t-Alert-wrap">',
'    <div class="t-Alert-icon">',
'      <span class="t-Icon"></span>',
'    </div>',
'    <div class="t-Alert-content">',
'      <div class="t-Alert-body">',
'        <h3>#MESSAGE#</h3>',
'        <p>#ADDITIONAL_INFO#</p>',
'        <div class="t-Alert-inset">#TECHNICAL_INFO#</div>',
'      </div>',
'    </div>',
'    <div class="t-Alert-buttons">',
'      <button onclick="#BACK_LINK#" class="t-Button t-Button--hot w50p t-Button--large" type="button">#OK#</button>',
'    </div>',
'  </div>',
'</div>'))
,p_grid_type=>'FIXED'
,p_grid_max_columns=>12
,p_grid_always_use_max_columns=>true
,p_grid_has_column_span=>true
,p_grid_always_emit=>true
,p_grid_emit_empty_leading_cols=>true
,p_grid_emit_empty_trail_cols=>false
,p_grid_default_label_col_span=>2
,p_grid_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="container">',
'#ROWS#',
'</div>'))
,p_grid_row_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="row">',
'#COLUMNS#',
'</div>'))
,p_grid_column_template=>'<div class="col col-#COLUMN_SPAN_NUMBER# #CSS_CLASSES#" #ATTRIBUTES#>#CONTENT#</div>'
,p_grid_first_column_attributes=>'alpha'
,p_grid_last_column_attributes=>'omega'
,p_dialog_js_init_code=>'apex.navigation.dialog(#PAGE_URL#,{title:#TITLE#,height:#DIALOG_HEIGHT#,width:#DIALOG_WIDTH#,maxWidth:#DIALOG_MAX_WIDTH#,modal:#IS_MODAL#,dialog:#DIALOG#,#DIALOG_ATTRIBUTES#},#DIALOG_CSS_CLASSES#,#TRIGGERING_ELEMENT#);'
,p_dialog_js_close_code=>'apex.navigation.dialog.close(#IS_MODAL#,#TARGET#);'
,p_dialog_js_cancel_code=>'apex.navigation.dialog.cancel(#IS_MODAL#);'
,p_dialog_browser_frame=>'MODAL'
,p_reference_id=>1996914646461572319
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9722546132687957)
,p_page_template_id=>wwv_flow_api.id(9722224555687956)
,p_name=>'Content Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>8
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9722842598687957)
,p_page_template_id=>wwv_flow_api.id(9722224555687956)
,p_name=>'Breadcrumb Bar'
,p_placeholder=>'REGION_POSITION_01'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9723129026687958)
,p_page_template_id=>wwv_flow_api.id(9722224555687956)
,p_name=>'Master Detail'
,p_placeholder=>'REGION_POSITION_02'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>8
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9723463925687958)
,p_page_template_id=>wwv_flow_api.id(9722224555687956)
,p_name=>'Right Side Column'
,p_placeholder=>'REGION_POSITION_03'
,p_has_grid_support=>false
,p_glv_new_row=>false
,p_max_fixed_grid_columns=>4
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9723794722687958)
,p_page_template_id=>wwv_flow_api.id(9722224555687956)
,p_name=>'Inline Dialogs'
,p_placeholder=>'REGION_POSITION_04'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9724065120687958)
,p_page_template_id=>wwv_flow_api.id(9722224555687956)
,p_name=>'Footer'
,p_placeholder=>'REGION_POSITION_05'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>8
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9724374848687958)
,p_page_template_id=>wwv_flow_api.id(9722224555687956)
,p_name=>'Page Navigation'
,p_placeholder=>'REGION_POSITION_06'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9724649364687958)
,p_page_template_id=>wwv_flow_api.id(9722224555687956)
,p_name=>'Page Header'
,p_placeholder=>'REGION_POSITION_07'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9724996431687958)
,p_page_template_id=>wwv_flow_api.id(9722224555687956)
,p_name=>'Before Content Body'
,p_placeholder=>'REGION_POSITION_08'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>8
);
end;
/
prompt --application/shared_components/user_interface/templates/page/minimal_no_navigation
begin
wwv_flow_api.create_template(
 p_id=>wwv_flow_api.id(9725334349687959)
,p_theme_id=>42
,p_name=>'Minimal (No Navigation)'
,p_internal_name=>'MINIMAL_NO_NAVIGATION'
,p_is_popup=>false
,p_javascript_code_onload=>'apex.theme42.initializePage.noSideCol();'
,p_header_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<!DOCTYPE html>',
'<html class="no-js #RTL_CLASS# page-&APP_PAGE_ID. app-&APP_ALIAS." lang="&BROWSER_LANGUAGE." #TEXT_DIRECTION#>',
'<head>',
'  <meta http-equiv="x-ua-compatible" content="IE=edge" />',
'  <meta charset="utf-8">',
'  <title>#TITLE#</title>',
'  #APEX_CSS#',
'  #THEME_CSS#',
'  #TEMPLATE_CSS#',
'  #THEME_STYLE_CSS#',
'  #APPLICATION_CSS#',
'  #PAGE_CSS#  ',
'  #FAVICONS#',
'  #HEAD#',
'  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
'</head>',
'<body class="t-PageBody t-PageBody--hideLeft t-PageBody--hideActions no-anim #PAGE_CSS_CLASSES# t-PageBody--noNav" #TEXT_DIRECTION# #ONLOAD# id="t_PageBody">',
'<a href="#main" id="t_Body_skipToContent">&APP_TEXT$UI_PAGE_SKIP_TO_CONTENT.</a>',
'#FORM_OPEN#',
'<header class="t-Header" id="t_Header">',
'  #REGION_POSITION_07#',
'  <div class="t-Header-branding" role="banner">',
'    <div class="t-Header-controls">',
'      <button class="t-Button t-Button--icon t-Button--header t-Button--headerTree" aria-label="#EXPAND_COLLAPSE_NAV_LABEL#" title="#EXPAND_COLLAPSE_NAV_LABEL#" id="t_Button_navControl" type="button"><span class="t-Icon fa fa-bars" aria-hidden="true"'
||'></span></button>',
'    </div>',
'    <div class="t-Header-logo">',
'      <a href="#HOME_LINK#" class="t-Header-logo-link">#LOGO#</a>',
'    </div>',
'    <div class="t-Header-navBar">',
'      #NAVIGATION_BAR#',
'    </div>',
'  </div>',
'</header>',
'    '))
,p_box=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body">',
'  <div class="t-Body-main">',
'    <div class="t-Body-title" id="t_Body_title">#REGION_POSITION_01#</div>',
'    <div class="t-Body-content" id="t_Body_content">',
'      <main id="main" class="t-Body-mainContent">',
'        #SUCCESS_MESSAGE##NOTIFICATION_MESSAGE##GLOBAL_NOTIFICATION#',
'        <div class="t-Body-fullContent">#REGION_POSITION_08#</div>',
'        <div class="t-Body-contentInner">#BODY#</div>',
'      </main>',
'      <footer class="t-Footer" role="contentinfo">',
'        <div class="t-Footer-body">',
'          <div class="t-Footer-content">#REGION_POSITION_05#</div>',
'          <div class="t-Footer-apex">',
'            <div class="t-Footer-version">#APP_VERSION#</div>',
'            <div class="t-Footer-customize">#CUSTOMIZE#</div>',
'            #BUILT_WITH_LOVE_USING_APEX#',
'          </div>',
'        </div>',
'        <div class="t-Footer-top">',
'          <a href="#top" class="t-Footer-topButton" id="t_Footer_topButton"><span class="a-Icon icon-up-chevron"></span></a>',
'        </div>',
'      </footer>',
'    </div>',
'  </div>',
'</div>',
'<div class="t-Body-inlineDialogs">#REGION_POSITION_04#</div>'))
,p_footer_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#FORM_CLOSE#',
'#DEVELOPER_TOOLBAR#',
'#APEX_JAVASCRIPT#',
'#GENERATED_CSS#',
'#THEME_JAVASCRIPT#',
'#TEMPLATE_JAVASCRIPT#',
'#APPLICATION_JAVASCRIPT#',
'#PAGE_JAVASCRIPT#  ',
'#GENERATED_JAVASCRIPT#',
'</body>',
'</html>',
''))
,p_success_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--success t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Success" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-header">',
'          <h2 class="t-Alert-title">#SUCCESS_MESSAGE#</h2>',
'        </div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_notification_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--warning t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Notification" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-body">#MESSAGE#</div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_navigation_bar=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<ul class="t-NavigationBar t-NavigationBar--classic" data-mode="classic">',
'  <li class="t-NavigationBar-item">',
'    <span class="t-Button t-Button--icon t-Button--noUI t-Button--header t-Button--navBar t-Button--headerUser">',
'      <span class="t-Icon a-Icon icon-user"></span>',
'      <span class="t-Button-label">&APP_USER.</span>',
'    </span>',
'  </li>#BAR_BODY#',
'</ul>'))
,p_navbar_entry=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-NavigationBar-item">',
'  <a class="t-Button t-Button--icon t-Button--header" href="#LINK#">',
'    <span class="t-Icon #IMAGE#"></span>',
'    <span class="t-Button-label">#TEXT#</span>',
'  </a>',
'</li>'))
,p_region_table_cattributes=>' summary="" cellpadding="0" border="0" cellspacing="0" width="100%"'
,p_breadcrumb_def_reg_pos=>'REGION_POSITION_01'
,p_theme_class_id=>4
,p_error_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Alert t-Alert--danger t-Alert--wizard t-Alert--defaultIcons">',
'  <div class="t-Alert-wrap">',
'    <div class="t-Alert-icon">',
'      <span class="t-Icon"></span>',
'    </div>',
'    <div class="t-Alert-content">',
'      <div class="t-Alert-body">',
'        <h3>#MESSAGE#</h3>',
'        <p>#ADDITIONAL_INFO#</p>',
'        <div class="t-Alert-inset">#TECHNICAL_INFO#</div>',
'      </div>',
'    </div>',
'    <div class="t-Alert-buttons">',
'      <button onclick="#BACK_LINK#" class="t-Button t-Button--hot w50p t-Button--large" type="button">#OK#</button>',
'    </div>',
'  </div>',
'</div>'))
,p_grid_type=>'FIXED'
,p_grid_max_columns=>12
,p_grid_always_use_max_columns=>true
,p_grid_has_column_span=>true
,p_grid_always_emit=>true
,p_grid_emit_empty_leading_cols=>true
,p_grid_emit_empty_trail_cols=>false
,p_grid_default_label_col_span=>2
,p_grid_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="container">',
'#ROWS#',
'</div>'))
,p_grid_row_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="row">',
'#COLUMNS#',
'</div>'))
,p_grid_column_template=>'<div class="col col-#COLUMN_SPAN_NUMBER# #CSS_CLASSES#" #ATTRIBUTES#>#CONTENT#</div>'
,p_grid_first_column_attributes=>'alpha'
,p_grid_last_column_attributes=>'omega'
,p_dialog_js_init_code=>'apex.navigation.dialog(#PAGE_URL#,{title:#TITLE#,height:#DIALOG_HEIGHT#,width:#DIALOG_WIDTH#,maxWidth:#DIALOG_MAX_WIDTH#,modal:#IS_MODAL#,dialog:#DIALOG#,#DIALOG_ATTRIBUTES#},#DIALOG_CSS_CLASSES#,#TRIGGERING_ELEMENT#);'
,p_dialog_js_close_code=>'apex.navigation.dialog.close(#IS_MODAL#,#TARGET#);'
,p_dialog_js_cancel_code=>'apex.navigation.dialog.cancel(#IS_MODAL#);'
,p_dialog_browser_frame=>'MODAL'
,p_reference_id=>2977628563533209425
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9725604166687959)
,p_page_template_id=>wwv_flow_api.id(9725334349687959)
,p_name=>'Content Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9725918301687959)
,p_page_template_id=>wwv_flow_api.id(9725334349687959)
,p_name=>'Breadcrumb Bar'
,p_placeholder=>'REGION_POSITION_01'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9726290966687959)
,p_page_template_id=>wwv_flow_api.id(9725334349687959)
,p_name=>'Inline Dialogs'
,p_placeholder=>'REGION_POSITION_04'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9726561630687959)
,p_page_template_id=>wwv_flow_api.id(9725334349687959)
,p_name=>'Footer'
,p_placeholder=>'REGION_POSITION_05'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9726855394687959)
,p_page_template_id=>wwv_flow_api.id(9725334349687959)
,p_name=>'Page Navigation'
,p_placeholder=>'REGION_POSITION_06'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9727131454687960)
,p_page_template_id=>wwv_flow_api.id(9725334349687959)
,p_name=>'Page Header'
,p_placeholder=>'REGION_POSITION_07'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9727432821687960)
,p_page_template_id=>wwv_flow_api.id(9725334349687959)
,p_name=>'Before Content Body'
,p_placeholder=>'REGION_POSITION_08'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
end;
/
prompt --application/shared_components/user_interface/templates/page/modal_dialog
begin
wwv_flow_api.create_template(
 p_id=>wwv_flow_api.id(9727847199687960)
,p_theme_id=>42
,p_name=>'Modal Dialog'
,p_internal_name=>'MODAL_DIALOG'
,p_is_popup=>true
,p_javascript_code_onload=>'apex.theme42.initializePage.modalDialog();'
,p_header_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<!DOCTYPE html>',
'<html class="no-js #RTL_CLASS# page-&APP_PAGE_ID. app-&APP_ALIAS." lang="&BROWSER_LANGUAGE." #TEXT_DIRECTION#>',
'<head>',
'  <meta http-equiv="x-ua-compatible" content="IE=edge" />',
'  <meta charset="utf-8">',
'  <title>#TITLE#</title>',
'  #APEX_CSS#',
'  #THEME_CSS#',
'  #TEMPLATE_CSS#',
'  #THEME_STYLE_CSS#',
'  #APPLICATION_CSS#',
'  #PAGE_CSS#',
'  #FAVICONS#',
'  #HEAD#',
'  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
'</head>',
'<body class="t-Dialog-page t-Dialog-page--standard #DIALOG_CSS_CLASSES# #PAGE_CSS_CLASSES#" #TEXT_DIRECTION# #ONLOAD#>',
'#FORM_OPEN#'))
,p_box=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Dialog" role="dialog" aria-label="#TITLE#">',
'  <div class="t-Dialog-header">#REGION_POSITION_01#</div>',
'  <div class="t-Dialog-bodyWrapperOut">',
'    <div class="t-Dialog-bodyWrapperIn">',
'      <div class="t-Dialog-body" role="main">',
'        #SUCCESS_MESSAGE##NOTIFICATION_MESSAGE##GLOBAL_NOTIFICATION#',
'        #BODY#',
'      </div>',
'    </div>',
'  </div>',
'  <div class="t-Dialog-footer">#REGION_POSITION_03#</div>',
'</div>'))
,p_footer_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#FORM_CLOSE#',
'#DEVELOPER_TOOLBAR#',
'#APEX_JAVASCRIPT#',
'#GENERATED_CSS#',
'#THEME_JAVASCRIPT#',
'#TEMPLATE_JAVASCRIPT#',
'#APPLICATION_JAVASCRIPT#',
'#PAGE_JAVASCRIPT#  ',
'#GENERATED_JAVASCRIPT#',
'</body>',
'</html>'))
,p_success_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--success t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Success" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-header">',
'          <h2 class="t-Alert-title">#SUCCESS_MESSAGE#</h2>',
'        </div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Success'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_notification_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--warning t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Notification" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-body">#MESSAGE#</div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Notification'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_region_table_cattributes=>' summary="" cellpadding="0" border="0" cellspacing="0" width="100%"'
,p_breadcrumb_def_reg_pos=>'REGION_POSITION_01'
,p_theme_class_id=>3
,p_error_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Alert t-Alert--danger t-Alert--wizard t-Alert--defaultIcons">',
'  <div class="t-Alert-wrap">',
'    <div class="t-Alert-icon">',
'      <span class="t-Icon"></span>',
'    </div>',
'    <div class="t-Alert-content">',
'      <div class="t-Alert-body">',
'        <h3>#MESSAGE#</h3>',
'        <p>#ADDITIONAL_INFO#</p>',
'        <div class="t-Alert-inset">#TECHNICAL_INFO#</div>',
'      </div>',
'    </div>',
'    <div class="t-Alert-buttons">',
'      <button onclick="#BACK_LINK#" class="t-Button t-Button--hot w50p t-Button--large" type="button">#OK#</button>',
'    </div>',
'  </div>',
'</div>'))
,p_grid_type=>'FIXED'
,p_grid_max_columns=>12
,p_grid_always_use_max_columns=>true
,p_grid_has_column_span=>true
,p_grid_always_emit=>true
,p_grid_emit_empty_leading_cols=>true
,p_grid_emit_empty_trail_cols=>false
,p_grid_default_label_col_span=>2
,p_grid_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="container">',
'#ROWS#',
'</div>'))
,p_grid_row_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="row">',
'#COLUMNS#',
'</div>'))
,p_grid_column_template=>'<div class="col col-#COLUMN_SPAN_NUMBER# #CSS_CLASSES#" #ATTRIBUTES#>#CONTENT#</div>'
,p_grid_first_column_attributes=>'alpha'
,p_grid_last_column_attributes=>'omega'
,p_dialog_js_init_code=>'apex.navigation.dialog(#PAGE_URL#,{title:#TITLE#,height:#DIALOG_HEIGHT#,width:#DIALOG_WIDTH#,maxWidth:#DIALOG_MAX_WIDTH#,modal:#IS_MODAL#,dialog:#DIALOG#,#DIALOG_ATTRIBUTES#},''t-Dialog-page--standard ''+#DIALOG_CSS_CLASSES#,#TRIGGERING_ELEMENT#);'
,p_dialog_js_close_code=>'apex.navigation.dialog.close(#IS_MODAL#,#TARGET#);'
,p_dialog_js_cancel_code=>'apex.navigation.dialog.cancel(#IS_MODAL#);'
,p_dialog_height=>'auto'
,p_dialog_width=>'720'
,p_dialog_max_width=>'960'
,p_dialog_browser_frame=>'MODAL'
,p_reference_id=>2098960803539086924
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9728139624687960)
,p_page_template_id=>wwv_flow_api.id(9727847199687960)
,p_name=>'Content Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9728425155687960)
,p_page_template_id=>wwv_flow_api.id(9727847199687960)
,p_name=>'Dialog Header'
,p_placeholder=>'REGION_POSITION_01'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9728722541687961)
,p_page_template_id=>wwv_flow_api.id(9727847199687960)
,p_name=>'Dialog Footer'
,p_placeholder=>'REGION_POSITION_03'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
end;
/
prompt --application/shared_components/user_interface/templates/page/right_side_column
begin
wwv_flow_api.create_template(
 p_id=>wwv_flow_api.id(9729332661687961)
,p_theme_id=>42
,p_name=>'Right Side Column'
,p_internal_name=>'RIGHT_SIDE_COLUMN'
,p_is_popup=>false
,p_javascript_code_onload=>'apex.theme42.initializePage.rightSideCol();'
,p_header_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<!DOCTYPE html>',
'<html class="no-js #RTL_CLASS# page-&APP_PAGE_ID. app-&APP_ALIAS." lang="&BROWSER_LANGUAGE." #TEXT_DIRECTION#>',
'<head>',
'  <meta http-equiv="x-ua-compatible" content="IE=edge" />',
'  <meta charset="utf-8"> ',
'  <title>#TITLE#</title>',
'  #APEX_CSS#',
'  #THEME_CSS#',
'  #TEMPLATE_CSS#',
'  #THEME_STYLE_CSS#',
'  #APPLICATION_CSS#',
'  #PAGE_CSS#',
'  #FAVICONS#',
'  #HEAD#',
'  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
'</head>',
'<body class="t-PageBody t-PageBody--hideLeft no-anim #PAGE_CSS_CLASSES#" #TEXT_DIRECTION# #ONLOAD# id="t_PageBody">',
'<a href="#main" id="t_Body_skipToContent">&APP_TEXT$UI_PAGE_SKIP_TO_CONTENT.</a>',
'#FORM_OPEN#',
'<header class="t-Header" id="t_Header">',
'  #REGION_POSITION_07#',
'  <div class="t-Header-branding" role="banner">',
'    <div class="t-Header-controls">',
'      <button class="t-Button t-Button--icon t-Button--header t-Button--headerTree" aria-label="#EXPAND_COLLAPSE_NAV_LABEL#" title="#EXPAND_COLLAPSE_NAV_LABEL#" id="t_Button_navControl" type="button"><span class="t-Header-controlsIcon" aria-hidden="t'
||'rue"></span></button>',
'    </div>',
'    <div class="t-Header-logo">',
'      <a href="#HOME_LINK#" class="t-Header-logo-link">#LOGO#</a>',
'    </div>',
'    <div class="t-Header-navBar">#NAVIGATION_BAR#</div>',
'  </div>',
'  <div class="t-Header-nav">',
'    #TOP_GLOBAL_NAVIGATION_LIST#',
'    #REGION_POSITION_06#',
'  </div>',
'</header>'))
,p_box=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body">',
'  #SIDE_GLOBAL_NAVIGATION_LIST#',
'  <div class="t-Body-main">',
'    <div class="t-Body-title" id="t_Body_title">#REGION_POSITION_01#</div>',
'    <div class="t-Body-content" id="t_Body_content">',
'      <main id="main" class="t-Body-mainContent">',
'        #SUCCESS_MESSAGE##NOTIFICATION_MESSAGE##GLOBAL_NOTIFICATION#',
'        <div class="t-Body-fullContent">#REGION_POSITION_08#</div>',
'        <div class="t-Body-contentInner">#BODY#</div>',
'      </main>',
'      <footer class="t-Footer" role="contentinfo">',
'        <div class="t-Footer-body">',
'          <div class="t-Footer-content">#REGION_POSITION_05#</div>',
'          <div class="t-Footer-apex">',
'            <div class="t-Footer-version">#APP_VERSION#</div>',
'            <div class="t-Footer-customize">#CUSTOMIZE#</div>',
'            #BUILT_WITH_LOVE_USING_APEX#',
'          </div>',
'        </div>',
'        <div class="t-Footer-top">',
'          <a href="#top" class="t-Footer-topButton" id="t_Footer_topButton"><span class="a-Icon icon-up-chevron"></span></a>',
'        </div>',
'      </footer>',
'    </div>',
'  </div>',
'  <div class="t-Body-actions" id="t_Body_actions">',
'    <button class="t-Body-actionsToggle" aria-label="#EXPAND_COLLAPSE_SIDE_COL_LABEL#" title="#EXPAND_COLLAPSE_SIDE_COL_LABEL#" id="t_Button_rightControlButton" type="button"><span class="t-Body-actionsControlsIcon" aria-hidden="true"></span></button'
||'>',
'    <div class="t-Body-actionsContent" role="complementary">#REGION_POSITION_03#</div>',
'  </div>',
'</div>',
'<div class="t-Body-inlineDialogs">#REGION_POSITION_04#</div>'))
,p_footer_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#FORM_CLOSE#',
'#DEVELOPER_TOOLBAR#',
'#APEX_JAVASCRIPT#',
'#GENERATED_CSS#',
'#THEME_JAVASCRIPT#',
'#TEMPLATE_JAVASCRIPT#',
'#APPLICATION_JAVASCRIPT#',
'#PAGE_JAVASCRIPT#  ',
'#GENERATED_JAVASCRIPT#',
'</body>',
'</html>'))
,p_success_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--success t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Success" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-header">',
'          <h2 class="t-Alert-title">#SUCCESS_MESSAGE#</h2>',
'        </div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Success'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_notification_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--warning t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Notification" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-body">#MESSAGE#</div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Notification'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_navigation_bar=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<ul class="t-NavigationBar" data-mode="classic">',
'  <li class="t-NavigationBar-item">',
'    <span class="t-Button t-Button--icon t-Button--noUI t-Button--header t-Button--navBar t-Button--headerUser">',
'      <span class="t-Icon a-Icon icon-user"></span>',
'      <span class="t-Button-label">&APP_USER.</span>',
'    </span>',
'  </li>#BAR_BODY#',
'</ul>'))
,p_navbar_entry=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-NavigationBar-item">',
'  <a class="t-Button t-Button--icon t-Button--header t-Button--navBar" href="#LINK#">',
'    <span class="t-Icon #IMAGE#"></span>',
'    <span class="t-Button-label">#TEXT#</span>',
'  </a>',
'</li>'))
,p_region_table_cattributes=>' summary="" cellpadding="0" border="0" cellspacing="0" width="100%"'
,p_sidebar_def_reg_pos=>'REGION_POSITION_03'
,p_breadcrumb_def_reg_pos=>'REGION_POSITION_01'
,p_theme_class_id=>17
,p_error_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Alert t-Alert--danger t-Alert--wizard t-Alert--defaultIcons">',
'  <div class="t-Alert-wrap">',
'    <div class="t-Alert-icon">',
'      <span class="t-Icon"></span>',
'    </div>',
'    <div class="t-Alert-content">',
'      <div class="t-Alert-body">',
'        <h3>#MESSAGE#</h3>',
'        <p>#ADDITIONAL_INFO#</p>',
'        <div class="t-Alert-inset">#TECHNICAL_INFO#</div>',
'      </div>',
'    </div>',
'    <div class="t-Alert-buttons">',
'      <button onclick="#BACK_LINK#" class="t-Button t-Button--hot w50p t-Button--large" type="button">#OK#</button>',
'    </div>',
'  </div>',
'</div>'))
,p_grid_type=>'FIXED'
,p_grid_max_columns=>12
,p_grid_always_use_max_columns=>true
,p_grid_has_column_span=>true
,p_grid_always_emit=>true
,p_grid_emit_empty_leading_cols=>true
,p_grid_emit_empty_trail_cols=>false
,p_grid_default_label_col_span=>2
,p_grid_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="container">',
'#ROWS#',
'</div>'))
,p_grid_row_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="row">',
'#COLUMNS#',
'</div>'))
,p_grid_column_template=>'<div class="col col-#COLUMN_SPAN_NUMBER# #CSS_CLASSES#" #ATTRIBUTES#>#CONTENT#</div>'
,p_grid_first_column_attributes=>'alpha'
,p_grid_last_column_attributes=>'omega'
,p_dialog_js_init_code=>'apex.navigation.dialog(#PAGE_URL#,{title:#TITLE#,height:#DIALOG_HEIGHT#,width:#DIALOG_WIDTH#,maxWidth:#DIALOG_MAX_WIDTH#,modal:#IS_MODAL#,dialog:#DIALOG#,#DIALOG_ATTRIBUTES#},#DIALOG_CSS_CLASSES#,#TRIGGERING_ELEMENT#);'
,p_dialog_js_close_code=>'apex.navigation.dialog.close(#IS_MODAL#,#TARGET#);'
,p_dialog_js_cancel_code=>'apex.navigation.dialog.cancel(#IS_MODAL#);'
,p_dialog_browser_frame=>'MODAL'
,p_reference_id=>2525200116240651575
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9729647909687961)
,p_page_template_id=>wwv_flow_api.id(9729332661687961)
,p_name=>'Content Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>8
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9729955665687962)
,p_page_template_id=>wwv_flow_api.id(9729332661687961)
,p_name=>'Breadcrumb Bar'
,p_placeholder=>'REGION_POSITION_01'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9730266614687962)
,p_page_template_id=>wwv_flow_api.id(9729332661687961)
,p_name=>'Right Column'
,p_placeholder=>'REGION_POSITION_03'
,p_has_grid_support=>false
,p_glv_new_row=>false
,p_max_fixed_grid_columns=>4
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9730519037687962)
,p_page_template_id=>wwv_flow_api.id(9729332661687961)
,p_name=>'Inline Dialogs'
,p_placeholder=>'REGION_POSITION_04'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9730827788687962)
,p_page_template_id=>wwv_flow_api.id(9729332661687961)
,p_name=>'Footer'
,p_placeholder=>'REGION_POSITION_05'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>8
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9731101276687962)
,p_page_template_id=>wwv_flow_api.id(9729332661687961)
,p_name=>'Page Navigation'
,p_placeholder=>'REGION_POSITION_06'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9731407000687962)
,p_page_template_id=>wwv_flow_api.id(9729332661687961)
,p_name=>'Page Header'
,p_placeholder=>'REGION_POSITION_07'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9731763477687962)
,p_page_template_id=>wwv_flow_api.id(9729332661687961)
,p_name=>'Before Content Body'
,p_placeholder=>'REGION_POSITION_08'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>8
);
end;
/
prompt --application/shared_components/user_interface/templates/page/standard
begin
wwv_flow_api.create_template(
 p_id=>wwv_flow_api.id(9732194808687963)
,p_theme_id=>42
,p_name=>'Standard'
,p_internal_name=>'STANDARD'
,p_is_popup=>false
,p_javascript_code_onload=>'apex.theme42.initializePage.noSideCol();'
,p_header_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<!DOCTYPE html>',
'<html class="no-js #RTL_CLASS# page-&APP_PAGE_ID. app-&APP_ALIAS." lang="&BROWSER_LANGUAGE." #TEXT_DIRECTION#>',
'<head>',
'  <meta http-equiv="x-ua-compatible" content="IE=edge" />',
'  <meta charset="utf-8">',
'  <title>#TITLE#</title>',
'  #APEX_CSS#',
'  #THEME_CSS#',
'  #TEMPLATE_CSS#',
'  #THEME_STYLE_CSS#',
'  #APPLICATION_CSS#',
'  #PAGE_CSS#',
'  #FAVICONS#',
'  #HEAD#',
'  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
'</head>',
'<body class="t-PageBody t-PageBody--hideLeft t-PageBody--hideActions no-anim #PAGE_CSS_CLASSES#" #TEXT_DIRECTION# #ONLOAD# id="t_PageBody">',
'<a href="#main" id="t_Body_skipToContent">&APP_TEXT$UI_PAGE_SKIP_TO_CONTENT.</a>',
'#FORM_OPEN#',
'<header class="t-Header" id="t_Header">',
'  #REGION_POSITION_07#',
'  <div class="t-Header-branding" role="banner">',
'    <div class="t-Header-controls">',
'      <button class="t-Button t-Button--icon t-Button--header t-Button--headerTree" aria-label="#EXPAND_COLLAPSE_NAV_LABEL#" title="#EXPAND_COLLAPSE_NAV_LABEL#" id="t_Button_navControl" type="button"><span class="t-Header-controlsIcon" aria-hidden="t'
||'rue"></span></button>',
'    </div>',
'    <div class="t-Header-logo">',
'      <a href="#HOME_LINK#" class="t-Header-logo-link">#LOGO#</a>',
'    </div>',
'    <div class="t-Header-navBar">#NAVIGATION_BAR#</div>',
'  </div>',
'  <div class="t-Header-nav">',
'    #TOP_GLOBAL_NAVIGATION_LIST#',
'    #REGION_POSITION_06#',
'  </div>',
'</header>',
''))
,p_box=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body">',
'  #SIDE_GLOBAL_NAVIGATION_LIST#',
'  <div class="t-Body-main">',
'    <div class="t-Body-title" id="t_Body_title">#REGION_POSITION_01#</div>',
'    <div class="t-Body-content" id="t_Body_content">',
'      <main id="main" class="t-Body-mainContent">',
'        #SUCCESS_MESSAGE##NOTIFICATION_MESSAGE##GLOBAL_NOTIFICATION#',
'        <div class="t-Body-fullContent">#REGION_POSITION_08#</div>',
'        <div class="t-Body-contentInner">#BODY#</div>',
'      </main>',
'      <footer class="t-Footer" role="contentinfo">',
'        <div class="t-Footer-body">',
'          <div class="t-Footer-content">#REGION_POSITION_05#</div>',
'          <div class="t-Footer-apex">',
'            <div class="t-Footer-version">#APP_VERSION#</div>',
'            <div class="t-Footer-customize">#CUSTOMIZE#</div>',
'            #BUILT_WITH_LOVE_USING_APEX#',
'          </div>',
'        </div>',
'        <div class="t-Footer-top">',
'          <a href="#top" class="t-Footer-topButton" id="t_Footer_topButton"><span class="a-Icon icon-up-chevron"></span></a>',
'        </div>',
'      </footer>',
'    </div>',
'  </div>',
'</div>',
'<div class="t-Body-inlineDialogs">#REGION_POSITION_04#</div>'))
,p_footer_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#FORM_CLOSE#',
'#DEVELOPER_TOOLBAR#',
'#APEX_JAVASCRIPT#',
'#GENERATED_CSS#',
'#THEME_JAVASCRIPT#',
'#TEMPLATE_JAVASCRIPT#',
'#APPLICATION_JAVASCRIPT#',
'#PAGE_JAVASCRIPT#  ',
'#GENERATED_JAVASCRIPT#',
'</body>',
'</html>',
''))
,p_success_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--success t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Success" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-header">',
'          <h2 class="t-Alert-title">#SUCCESS_MESSAGE#</h2>',
'        </div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_notification_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--warning t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Notification" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-body">#MESSAGE#</div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_navigation_bar=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<ul class="t-NavigationBar t-NavigationBar--classic" data-mode="classic">',
'  <li class="t-NavigationBar-item">',
'    <span class="t-Button t-Button--icon t-Button--noUI t-Button--header t-Button--navBar t-Button--headerUser">',
'      <span class="t-Icon a-Icon icon-user"></span>',
'      <span class="t-Button-label">&APP_USER.</span>',
'    </span>',
'  </li>#BAR_BODY#',
'</ul>'))
,p_navbar_entry=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-NavigationBar-item">',
'  <a class="t-Button t-Button--icon t-Button--header" href="#LINK#">',
'    <span class="t-Icon #IMAGE#"></span>',
'    <span class="t-Button-label">#TEXT#</span>',
'  </a>',
'</li>'))
,p_region_table_cattributes=>' summary="" cellpadding="0" border="0" cellspacing="0" width="100%"'
,p_breadcrumb_def_reg_pos=>'REGION_POSITION_01'
,p_theme_class_id=>1
,p_error_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Alert t-Alert--danger t-Alert--wizard t-Alert--defaultIcons">',
'  <div class="t-Alert-wrap">',
'    <div class="t-Alert-icon">',
'      <span class="t-Icon"></span>',
'    </div>',
'    <div class="t-Alert-content">',
'      <div class="t-Alert-body">',
'        <h3>#MESSAGE#</h3>',
'        <p>#ADDITIONAL_INFO#</p>',
'        <div class="t-Alert-inset">#TECHNICAL_INFO#</div>',
'      </div>',
'    </div>',
'    <div class="t-Alert-buttons">',
'      <button onclick="#BACK_LINK#" class="t-Button t-Button--hot w50p t-Button--large" type="button">#OK#</button>',
'    </div>',
'  </div>',
'</div>'))
,p_grid_type=>'FIXED'
,p_grid_max_columns=>12
,p_grid_always_use_max_columns=>true
,p_grid_has_column_span=>true
,p_grid_always_emit=>true
,p_grid_emit_empty_leading_cols=>true
,p_grid_emit_empty_trail_cols=>false
,p_grid_default_label_col_span=>2
,p_grid_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="container">',
'#ROWS#',
'</div>'))
,p_grid_row_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="row">',
'#COLUMNS#',
'</div>'))
,p_grid_column_template=>'<div class="col col-#COLUMN_SPAN_NUMBER# #CSS_CLASSES#" #ATTRIBUTES#>#CONTENT#</div>'
,p_grid_first_column_attributes=>'alpha'
,p_grid_last_column_attributes=>'omega'
,p_dialog_js_init_code=>'apex.navigation.dialog(#PAGE_URL#,{title:#TITLE#,height:#DIALOG_HEIGHT#,width:#DIALOG_WIDTH#,maxWidth:#DIALOG_MAX_WIDTH#,modal:#IS_MODAL#,dialog:#DIALOG#,#DIALOG_ATTRIBUTES#},#DIALOG_CSS_CLASSES#,#TRIGGERING_ELEMENT#);'
,p_dialog_js_close_code=>'apex.navigation.dialog.close(#IS_MODAL#,#TARGET#);'
,p_dialog_js_cancel_code=>'apex.navigation.dialog.cancel(#IS_MODAL#);'
,p_dialog_browser_frame=>'MODAL'
,p_reference_id=>4070909157481059304
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9732476854687963)
,p_page_template_id=>wwv_flow_api.id(9732194808687963)
,p_name=>'Content Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9732790826687963)
,p_page_template_id=>wwv_flow_api.id(9732194808687963)
,p_name=>'Breadcrumb Bar'
,p_placeholder=>'REGION_POSITION_01'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9733022431687963)
,p_page_template_id=>wwv_flow_api.id(9732194808687963)
,p_name=>'Inline Dialogs'
,p_placeholder=>'REGION_POSITION_04'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9733345988687963)
,p_page_template_id=>wwv_flow_api.id(9732194808687963)
,p_name=>'Footer'
,p_placeholder=>'REGION_POSITION_05'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9733688930687963)
,p_page_template_id=>wwv_flow_api.id(9732194808687963)
,p_name=>'Page Navigation'
,p_placeholder=>'REGION_POSITION_06'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9733939538687963)
,p_page_template_id=>wwv_flow_api.id(9732194808687963)
,p_name=>'Page Header'
,p_placeholder=>'REGION_POSITION_07'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9734276546687964)
,p_page_template_id=>wwv_flow_api.id(9732194808687963)
,p_name=>'Before Content Body'
,p_placeholder=>'REGION_POSITION_08'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
end;
/
prompt --application/shared_components/user_interface/templates/page/wizard_modal_dialog
begin
wwv_flow_api.create_template(
 p_id=>wwv_flow_api.id(9734610063687964)
,p_theme_id=>42
,p_name=>'Wizard Modal Dialog'
,p_internal_name=>'WIZARD_MODAL_DIALOG'
,p_is_popup=>true
,p_javascript_code_onload=>'apex.theme42.initializePage.wizardModal();'
,p_header_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<!DOCTYPE html>',
'<html class="no-js #RTL_CLASS# page-&APP_PAGE_ID. app-&APP_ALIAS." lang="&BROWSER_LANGUAGE." #TEXT_DIRECTION#>',
'<head>',
'  <meta http-equiv="x-ua-compatible" content="IE=edge" />',
'  <meta charset="utf-8">',
'  <title>#TITLE#</title>',
'  #APEX_CSS#',
'  #THEME_CSS#',
'  #TEMPLATE_CSS#',
'  #THEME_STYLE_CSS#',
'  #APPLICATION_CSS#',
'  #PAGE_CSS#',
'  #FAVICONS#',
'  #HEAD#',
'  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
'</head>',
'<body class="t-Dialog-page t-Dialog-page--wizard #DIALOG_CSS_CLASSES# #PAGE_CSS_CLASSES#" #TEXT_DIRECTION# #ONLOAD#>',
'#FORM_OPEN#'))
,p_box=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Dialog" role="dialog" aria-label="#TITLE#">',
'  <div class="t-Dialog-header">#REGION_POSITION_01#</div>',
'  <div class="t-Dialog-bodyWrapperOut">',
'    <div class="t-Dialog-bodyWrapperIn">',
'      <div class="t-Dialog-body" role="main">',
'        #SUCCESS_MESSAGE##NOTIFICATION_MESSAGE##GLOBAL_NOTIFICATION#',
'        #BODY#',
'      </div>',
'    </div>',
'  </div>',
'  <div class="t-Dialog-footer">#REGION_POSITION_03#</div>',
'</div>'))
,p_footer_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#FORM_CLOSE#',
'#DEVELOPER_TOOLBAR#',
'#APEX_JAVASCRIPT#',
'#GENERATED_CSS#',
'#THEME_JAVASCRIPT#',
'#TEMPLATE_JAVASCRIPT#',
'#APPLICATION_JAVASCRIPT#',
'#PAGE_JAVASCRIPT#  ',
'#GENERATED_JAVASCRIPT#',
'</body>',
'</html>'))
,p_success_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--success t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Success" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-header">',
'          <h2 class="t-Alert-title">#SUCCESS_MESSAGE#</h2>',
'        </div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Success'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_notification_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-alert">',
'  <div class="t-Alert t-Alert--defaultIcons t-Alert--warning t-Alert--horizontal t-Alert--page t-Alert--colorBG" id="t_Alert_Notification" role="alert">',
'    <div class="t-Alert-wrap">',
'      <div class="t-Alert-icon">',
'        <span class="t-Icon"></span>',
'      </div>',
'      <div class="t-Alert-content">',
'        <div class="t-Alert-body">#MESSAGE#</div>',
'      </div>',
'      <div class="t-Alert-buttons">',
'        <button class="t-Button t-Button--noUI t-Button--icon t-Button--closeAlert" onclick="apex.jQuery(''#t_Alert_Notification'').remove();" type="button" title="#CLOSE_NOTIFICATION#"><span class="t-Icon icon-close"></span></button>',
'      </div>',
'    </div>',
'  </div>',
'</div>'))
,p_region_table_cattributes=>' summary="" cellpadding="0" border="0" cellspacing="0" width="100%"'
,p_theme_class_id=>3
,p_error_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Alert t-Alert--danger t-Alert--wizard t-Alert--defaultIcons">',
'  <div class="t-Alert-wrap">',
'    <div class="t-Alert-icon">',
'      <span class="t-Icon"></span>',
'    </div>',
'    <div class="t-Alert-content">',
'      <div class="t-Alert-body">',
'        <h3>#MESSAGE#</h3>',
'        <p>#ADDITIONAL_INFO#</p>',
'        <div class="t-Alert-inset">#TECHNICAL_INFO#</div>',
'      </div>',
'    </div>',
'    <div class="t-Alert-buttons">',
'      <button onclick="#BACK_LINK#" class="t-Button t-Button--hot w50p t-Button--large" type="button">#OK#</button>',
'    </div>',
'  </div>',
'</div>'))
,p_grid_type=>'FIXED'
,p_grid_max_columns=>12
,p_grid_always_use_max_columns=>true
,p_grid_has_column_span=>true
,p_grid_always_emit=>true
,p_grid_emit_empty_leading_cols=>true
,p_grid_emit_empty_trail_cols=>false
,p_grid_default_label_col_span=>2
,p_grid_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="container">',
'#ROWS#',
'</div>'))
,p_grid_row_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="row">',
'#COLUMNS#',
'</div>'))
,p_grid_column_template=>'<div class="col col-#COLUMN_SPAN_NUMBER# #CSS_CLASSES#" #ATTRIBUTES#>#CONTENT#</div>'
,p_grid_first_column_attributes=>'alpha'
,p_grid_last_column_attributes=>'omega'
,p_dialog_js_init_code=>'apex.navigation.dialog(#PAGE_URL#,{title:#TITLE#,height:#DIALOG_HEIGHT#,width:#DIALOG_WIDTH#,maxWidth:#DIALOG_MAX_WIDTH#,modal:#IS_MODAL#,dialog:#DIALOG#,#DIALOG_ATTRIBUTES#},''t-Dialog-page--wizard ''+#DIALOG_CSS_CLASSES#,#TRIGGERING_ELEMENT#);'
,p_dialog_js_close_code=>'apex.navigation.dialog.close(#IS_MODAL#,#TARGET#);'
,p_dialog_js_cancel_code=>'apex.navigation.dialog.cancel(#IS_MODAL#);'
,p_dialog_height=>'auto'
,p_dialog_width=>'720'
,p_dialog_max_width=>'960'
,p_dialog_browser_frame=>'MODAL'
,p_reference_id=>2120348229686426515
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9734918029687965)
,p_page_template_id=>wwv_flow_api.id(9734610063687964)
,p_name=>'Wizard Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9735201763687965)
,p_page_template_id=>wwv_flow_api.id(9734610063687964)
,p_name=>'Wizard Progress Bar'
,p_placeholder=>'REGION_POSITION_01'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_page_tmpl_display_point(
 p_id=>wwv_flow_api.id(9735527768687971)
,p_page_template_id=>wwv_flow_api.id(9734610063687964)
,p_name=>'Wizard Buttons'
,p_placeholder=>'REGION_POSITION_03'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
end;
/
prompt --application/shared_components/user_interface/templates/button/icon
begin
wwv_flow_api.create_button_templates(
 p_id=>wwv_flow_api.id(9820400204688092)
,p_template_name=>'Icon'
,p_internal_name=>'ICON'
,p_template=>'<button class="t-Button t-Button--noLabel t-Button--icon #BUTTON_CSS_CLASSES#" #BUTTON_ATTRIBUTES# onclick="#JAVASCRIPT#" type="button" id="#BUTTON_ID#" title="#LABEL#" aria-label="#LABEL#"><span class="t-Icon #ICON_CSS_CLASSES#" aria-hidden="true"><'
||'/span></button>'
,p_hot_template=>'<button class="t-Button t-Button--noLabel t-Button--icon #BUTTON_CSS_CLASSES# t-Button--hot" #BUTTON_ATTRIBUTES# onclick="#JAVASCRIPT#" type="button" id="#BUTTON_ID#" title="#LABEL#" aria-label="#LABEL#"><span class="t-Icon #ICON_CSS_CLASSES#" aria-h'
||'idden="true"></span></button>'
,p_reference_id=>2347660919680321258
,p_translate_this_template=>'N'
,p_theme_class_id=>5
,p_theme_id=>42
);
end;
/
prompt --application/shared_components/user_interface/templates/button/text
begin
wwv_flow_api.create_button_templates(
 p_id=>wwv_flow_api.id(9821119233688096)
,p_template_name=>'Text'
,p_internal_name=>'TEXT'
,p_template=>'<button onclick="#JAVASCRIPT#" class="t-Button #BUTTON_CSS_CLASSES#" type="button" #BUTTON_ATTRIBUTES# id="#BUTTON_ID#"><span class="t-Button-label">#LABEL#</span></button>'
,p_hot_template=>'<button onclick="#JAVASCRIPT#" class="t-Button t-Button--hot #BUTTON_CSS_CLASSES#" type="button" #BUTTON_ATTRIBUTES# id="#BUTTON_ID#"><span class="t-Button-label">#LABEL#</span></button>'
,p_reference_id=>4070916158035059322
,p_translate_this_template=>'N'
,p_theme_class_id=>1
,p_theme_id=>42
);
end;
/
prompt --application/shared_components/user_interface/templates/button/text_with_icon
begin
wwv_flow_api.create_button_templates(
 p_id=>wwv_flow_api.id(9821219757688096)
,p_template_name=>'Text with Icon'
,p_internal_name=>'TEXT_WITH_ICON'
,p_template=>'<button class="t-Button t-Button--icon #BUTTON_CSS_CLASSES#" #BUTTON_ATTRIBUTES# onclick="#JAVASCRIPT#" type="button" id="#BUTTON_ID#"><span class="t-Icon t-Icon--left #ICON_CSS_CLASSES#" aria-hidden="true"></span><span class="t-Button-label">#LABEL#'
||'</span><span class="t-Icon t-Icon--right #ICON_CSS_CLASSES#" aria-hidden="true"></span></button>'
,p_hot_template=>'<button class="t-Button t-Button--icon #BUTTON_CSS_CLASSES# t-Button--hot" #BUTTON_ATTRIBUTES# onclick="#JAVASCRIPT#" type="button" id="#BUTTON_ID#"><span class="t-Icon t-Icon--left #ICON_CSS_CLASSES#" aria-hidden="true"></span><span class="t-Button-'
||'label">#LABEL#</span><span class="t-Icon t-Icon--right #ICON_CSS_CLASSES#" aria-hidden="true"></span></button>'
,p_reference_id=>2081382742158699622
,p_translate_this_template=>'N'
,p_theme_class_id=>4
,p_preset_template_options=>'t-Button--iconRight'
,p_theme_id=>42
);
end;
/
prompt --application/shared_components/user_interface/templates/region/alert
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9736107349687972)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Alert #REGION_CSS_CLASSES#" id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES#>',
'  <div class="t-Alert-wrap">',
'    <div class="t-Alert-icon">',
'      <span class="t-Icon #ICON_CSS_CLASSES#"></span>',
'    </div>',
'    <div class="t-Alert-content">',
'      <div class="t-Alert-header">',
'        <h2 class="t-Alert-title" id="#REGION_STATIC_ID#_heading">#TITLE#</h2>',
'      </div>',
'      <div class="t-Alert-body">#BODY#</div>',
'    </div>',
'    <div class="t-Alert-buttons">#PREVIOUS##CLOSE##CREATE##NEXT#</div>',
'  </div>',
'</div>'))
,p_page_plug_template_name=>'Alert'
,p_internal_name=>'ALERT'
,p_plug_table_bgcolor=>'#ffffff'
,p_theme_id=>42
,p_theme_class_id=>21
,p_preset_template_options=>'t-Alert--horizontal:t-Alert--defaultIcons:t-Alert--warning'
,p_plug_heading_bgcolor=>'#ffffff'
,p_plug_font_size=>'-1'
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>2039236646100190748
,p_translate_this_template=>'N'
,p_template_comment=>'Red Theme'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9736472427687980)
,p_plug_template_id=>wwv_flow_api.id(9736107349687972)
,p_name=>'Region Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
end;
/
prompt --application/shared_components/user_interface/templates/region/blank_with_attributes
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9739874064687990)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES# class="#REGION_CSS_CLASSES#"> ',
'#PREVIOUS##BODY##SUB_REGIONS##NEXT#',
'</div>'))
,p_page_plug_template_name=>'Blank with Attributes'
,p_internal_name=>'BLANK_WITH_ATTRIBUTES'
,p_theme_id=>42
,p_theme_class_id=>7
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>4499993862448380551
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/region/blank_with_attributes_no_grid
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9740024261687991)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES# class="#REGION_CSS_CLASSES#"> ',
'#PREVIOUS##BODY##SUB_REGIONS##NEXT#',
'</div>'))
,p_page_plug_template_name=>'Blank with Attributes (No Grid)'
,p_internal_name=>'BLANK_WITH_ATTRIBUTES_NO_GRID'
,p_theme_id=>42
,p_theme_class_id=>7
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>3369790999010910123
,p_translate_this_template=>'N'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9740398579687991)
,p_plug_template_id=>wwv_flow_api.id(9740024261687991)
,p_name=>'Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9740677612687991)
,p_plug_template_id=>wwv_flow_api.id(9740024261687991)
,p_name=>'Sub Regions'
,p_placeholder=>'SUB_REGIONS'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
end;
/
prompt --application/shared_components/user_interface/templates/region/buttons_container
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9740827754687991)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-ButtonRegion t-Form--floatLeft #REGION_CSS_CLASSES#" id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES#>',
'  <div class="t-ButtonRegion-wrap">',
'    <div class="t-ButtonRegion-col t-ButtonRegion-col--left"><div class="t-ButtonRegion-buttons">#PREVIOUS##CLOSE##DELETE#</div></div>',
'    <div class="t-ButtonRegion-col t-ButtonRegion-col--content">',
'      <h2 class="t-ButtonRegion-title" id="#REGION_STATIC_ID#_heading">#TITLE#</h2>',
'      #BODY#',
'      <div class="t-ButtonRegion-buttons">#CHANGE#</div>',
'    </div>',
'    <div class="t-ButtonRegion-col t-ButtonRegion-col--right"><div class="t-ButtonRegion-buttons">#EDIT##CREATE##NEXT#</div></div>',
'  </div>',
'</div>'))
,p_page_plug_template_name=>'Buttons Container'
,p_internal_name=>'BUTTONS_CONTAINER'
,p_plug_table_bgcolor=>'#ffffff'
,p_theme_id=>42
,p_theme_class_id=>17
,p_plug_heading_bgcolor=>'#ffffff'
,p_plug_font_size=>'-1'
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>2124982336649579661
,p_translate_this_template=>'N'
,p_template_comment=>'Red Theme'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9741120094687991)
,p_plug_template_id=>wwv_flow_api.id(9740827754687991)
,p_name=>'Region Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9741416471687992)
,p_plug_template_id=>wwv_flow_api.id(9740827754687991)
,p_name=>'Sub Regions'
,p_placeholder=>'SUB_REGIONS'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
end;
/
prompt --application/shared_components/user_interface/templates/region/carousel_container
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9743063117687993)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Region t-Region--carousel #REGION_CSS_CLASSES#" id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES#>',
' <div class="t-Region-header">',
'  <div class="t-Region-headerItems t-Region-headerItems--title">',
'    <span class="t-Region-headerIcon"><span class="t-Icon #ICON_CSS_CLASSES#" aria-hidden="true"></span></span>',
'    <h2 class="t-Region-title" id="#REGION_STATIC_ID#_heading">#TITLE#</h2>',
'  </div>',
'  <div class="t-Region-headerItems t-Region-headerItems--buttons">#COPY##EDIT#<span class="js-maximizeButtonContainer"></span></div>',
' </div>',
' <div class="t-Region-bodyWrap">',
'   <div class="t-Region-buttons t-Region-buttons--top">',
'    <div class="t-Region-buttons-left">#PREVIOUS#</div>',
'    <div class="t-Region-buttons-right">#NEXT#</div>',
'   </div>',
'   <div class="t-Region-body">',
'     #BODY#',
'   <div class="t-Region-carouselRegions">',
'     #SUB_REGIONS#',
'   </div>',
'   </div>',
'   <div class="t-Region-buttons t-Region-buttons--bottom">',
'    <div class="t-Region-buttons-left">#CLOSE##HELP#</div>',
'    <div class="t-Region-buttons-right">#DELETE##CHANGE##CREATE#</div>',
'   </div>',
' </div>',
'</div>'))
,p_sub_plug_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div data-label="#SUB_REGION_TITLE#" id="SR_#SUB_REGION_ID#">',
'  #SUB_REGION#',
'</div>'))
,p_page_plug_template_name=>'Carousel Container'
,p_internal_name=>'CAROUSEL_CONTAINER'
,p_javascript_file_urls=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#IMAGE_PREFIX#libraries/apex/#MIN_DIRECTORY#widget.apexTabs#MIN#.js?v=#APEX_VERSION#',
'#IMAGE_PREFIX#plugins/com.oracle.apex.carousel/1.1/com.oracle.apex.carousel#MIN#.js?v=#APEX_VERSION#'))
,p_plug_table_bgcolor=>'#ffffff'
,p_theme_id=>42
,p_theme_class_id=>5
,p_default_template_options=>'t-Region--showCarouselControls'
,p_preset_template_options=>'t-Region--hiddenOverflow'
,p_plug_heading_bgcolor=>'#ffffff'
,p_plug_font_size=>'-1'
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>2865840475322558786
,p_translate_this_template=>'N'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9743325431687993)
,p_plug_template_id=>wwv_flow_api.id(9743063117687993)
,p_name=>'Region Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9743620839687993)
,p_plug_template_id=>wwv_flow_api.id(9743063117687993)
,p_name=>'Slides'
,p_placeholder=>'SUB_REGIONS'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
end;
/
prompt --application/shared_components/user_interface/templates/region/collapsible
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9750220677688000)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Region t-Region--hideShow #REGION_CSS_CLASSES#" id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES#>',
' <div class="t-Region-header">',
'  <div class="t-Region-headerItems  t-Region-headerItems--controls"><button class="t-Button t-Button--icon t-Button--hideShow" type="button"></button></div>',
'  <div class="t-Region-headerItems t-Region-headerItems--title">',
'    <h2 class="t-Region-title">#TITLE#</h2>',
'  </div>',
'  <div class="t-Region-headerItems t-Region-headerItems--buttons">#EDIT#</div>',
' </div>',
' <div class="t-Region-bodyWrap">',
'   <div class="t-Region-buttons t-Region-buttons--top">',
'    <div class="t-Region-buttons-left">#CLOSE#</div>',
'    <div class="t-Region-buttons-right">#CREATE#</div>',
'   </div>',
'   <div class="t-Region-body">',
'     #COPY#',
'     #BODY#',
'     #SUB_REGIONS#',
'     #CHANGE#',
'   </div>',
'   <div class="t-Region-buttons t-Region-buttons--bottom">',
'    <div class="t-Region-buttons-left">#PREVIOUS#</div>',
'    <div class="t-Region-buttons-right">#NEXT#</div>',
'   </div>',
' </div>',
'</div>'))
,p_page_plug_template_name=>'Collapsible'
,p_internal_name=>'COLLAPSIBLE'
,p_plug_table_bgcolor=>'#ffffff'
,p_theme_id=>42
,p_theme_class_id=>1
,p_preset_template_options=>'is-expanded:t-Region--scrollBody'
,p_plug_heading_bgcolor=>'#ffffff'
,p_plug_font_size=>'-1'
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>2662888092628347716
,p_translate_this_template=>'N'
,p_template_comment=>'Red Theme'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9750544457688000)
,p_plug_template_id=>wwv_flow_api.id(9750220677688000)
,p_name=>'Region Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9750821924688001)
,p_plug_template_id=>wwv_flow_api.id(9750220677688000)
,p_name=>'Sub Regions'
,p_placeholder=>'SUB_REGIONS'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
end;
/
prompt --application/shared_components/user_interface/templates/region/content_block
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9755638233688011)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-ContentBlock #REGION_CSS_CLASSES#" id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES#>',
'  <div class="t-ContentBlock-header">',
'    <div class="t-ContentBlock-headerItems t-ContentBlock-headerItems--title">',
'      <span class="t-ContentBlock-headerIcon"><span class="t-Icon #ICON_CSS_CLASSES#" aria-hidden="true"></span></span>',
'      <h1 class="t-ContentBlock-title" id="#REGION_STATIC_ID#_heading">#TITLE#</h1>',
'      #EDIT#',
'    </div>',
'    <div class="t-ContentBlock-headerItems t-ContentBlock-headerItems--buttons">#CHANGE#</div>',
'  </div>',
'  <div class="t-ContentBlock-body">#BODY#</div>',
'  <div class="t-ContentBlock-buttons">#PREVIOUS##NEXT#</div>',
'</div>',
''))
,p_page_plug_template_name=>'Content Block'
,p_internal_name=>'CONTENT_BLOCK'
,p_theme_id=>42
,p_theme_class_id=>21
,p_preset_template_options=>'t-ContentBlock--h1'
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>2320668864738842174
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/region/hero
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9757663101688013)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-HeroRegion #REGION_CSS_CLASSES#" id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES#>',
'  <div class="t-HeroRegion-wrap">',
'    <div class="t-HeroRegion-col t-HeroRegion-col--left"><span class="t-HeroRegion-icon t-Icon #ICON_CSS_CLASSES#"></span></div>',
'    <div class="t-HeroRegion-col t-HeroRegion-col--content">',
'      <h1 class="t-HeroRegion-title">#TITLE#</h1>',
'      #BODY#',
'    </div>',
'    <div class="t-HeroRegion-col t-HeroRegion-col--right"><div class="t-HeroRegion-form">#SUB_REGIONS#</div><div class="t-HeroRegion-buttons">#NEXT#</div></div>',
'  </div>',
'</div>'))
,p_page_plug_template_name=>'Hero'
,p_internal_name=>'HERO'
,p_theme_id=>42
,p_theme_class_id=>22
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>2672571031438297268
,p_translate_this_template=>'N'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9757925689688013)
,p_plug_template_id=>wwv_flow_api.id(9757663101688013)
,p_name=>'Region Body'
,p_placeholder=>'#BODY#'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
end;
/
prompt --application/shared_components/user_interface/templates/region/inline_dialog
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9759783899688016)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div id="#REGION_STATIC_ID#_parent">',
'<div id="#REGION_STATIC_ID#"  class="t-DialogRegion #REGION_CSS_CLASSES# js-regionDialog" #REGION_ATTRIBUTES# style="display:none" title="#TITLE#">',
'  <div class="t-DialogRegion-wrap">',
'    <div class="t-DialogRegion-bodyWrapperOut"><div class="t-DialogRegion-bodyWrapperIn"><div class="t-DialogRegion-body">#BODY#</div></div></div>',
'    <div class="t-DialogRegion-buttons">',
'       <div class="t-ButtonRegion t-ButtonRegion--dialogRegion">',
'         <div class="t-ButtonRegion-wrap">',
'           <div class="t-ButtonRegion-col t-ButtonRegion-col--left"><div class="t-ButtonRegion-buttons">#PREVIOUS##DELETE##CLOSE#</div></div>',
'           <div class="t-ButtonRegion-col t-ButtonRegion-col--right"><div class="t-ButtonRegion-buttons">#EDIT##CREATE##NEXT#</div></div>',
'         </div>',
'       </div>',
'    </div>',
'  </div>',
'</div>',
'</div>'))
,p_page_plug_template_name=>'Inline Dialog'
,p_internal_name=>'INLINE_DIALOG'
,p_theme_id=>42
,p_theme_class_id=>24
,p_default_template_options=>'js-modal:js-draggable:js-resizable'
,p_preset_template_options=>'js-dialog-size600x400'
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>2671226943886536762
,p_translate_this_template=>'N'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9760090652688016)
,p_plug_template_id=>wwv_flow_api.id(9759783899688016)
,p_name=>'Region Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
);
end;
/
prompt --application/shared_components/user_interface/templates/region/inline_popup
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9762017927688018)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div id="#REGION_STATIC_ID#_parent">',
'<div id="#REGION_STATIC_ID#"  class="t-DialogRegion #REGION_CSS_CLASSES# js-regionPopup" #REGION_ATTRIBUTES# style="display:none" title="#TITLE#">',
'  <div class="t-DialogRegion-wrap">',
'    <div class="t-DialogRegion-bodyWrapperOut"><div class="t-DialogRegion-bodyWrapperIn"><div class="t-DialogRegion-body">#BODY#</div></div></div>',
'    <div class="t-DialogRegion-buttons">',
'       <div class="t-ButtonRegion t-ButtonRegion--dialogRegion">',
'         <div class="t-ButtonRegion-wrap">',
'           <div class="t-ButtonRegion-col t-ButtonRegion-col--left"><div class="t-ButtonRegion-buttons">#PREVIOUS##DELETE##CLOSE#</div></div>',
'           <div class="t-ButtonRegion-col t-ButtonRegion-col--right"><div class="t-ButtonRegion-buttons">#EDIT##CREATE##NEXT#</div></div>',
'         </div>',
'       </div>',
'    </div>',
'  </div>',
'</div>',
'</div>'))
,p_page_plug_template_name=>'Inline Popup'
,p_internal_name=>'INLINE_POPUP'
,p_theme_id=>42
,p_theme_class_id=>24
,p_preset_template_options=>'js-dialog-size600x400'
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>1483922538999385230
,p_translate_this_template=>'N'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9762348405688018)
,p_plug_template_id=>wwv_flow_api.id(9762017927688018)
,p_name=>'Region Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
);
end;
/
prompt --application/shared_components/user_interface/templates/region/interactive_report
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9763915989688019)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES# class="t-IRR-region #REGION_CSS_CLASSES#">',
'  <h2 class="u-VisuallyHidden" id="#REGION_STATIC_ID#_heading">#TITLE#</h2>',
'#PREVIOUS##BODY##SUB_REGIONS##NEXT#',
'</div>'))
,p_page_plug_template_name=>'Interactive Report'
,p_internal_name=>'INTERACTIVE_REPORT'
,p_theme_id=>42
,p_theme_class_id=>9
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>2099079838218790610
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/region/login
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9764594135688020)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Login-region t-Form--stretchInputs t-Form--labelsAbove #REGION_CSS_CLASSES#" id="#REGION_ID#" #REGION_ATTRIBUTES#>',
'  <div class="t-Login-header">',
'    <span class="t-Login-logo #ICON_CSS_CLASSES#"></span>',
'    <h1 class="t-Login-title" id="#REGION_STATIC_ID#_heading">#TITLE#</h1>',
'  </div>',
'  <div class="t-Login-body">',
'    #BODY#',
'  </div>',
'  <div class="t-Login-buttons">',
'    #NEXT#',
'  </div>',
'  <div class="t-Login-links">',
'    #EDIT##CREATE#',
'  </div>',
'  #SUB_REGIONS#',
'</div>'))
,p_page_plug_template_name=>'Login'
,p_internal_name=>'LOGIN'
,p_theme_id=>42
,p_theme_class_id=>23
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>2672711194551076376
,p_translate_this_template=>'N'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9764819752688020)
,p_plug_template_id=>wwv_flow_api.id(9764594135688020)
,p_name=>'Content Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
end;
/
prompt --application/shared_components/user_interface/templates/region/standard
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9765042323688020)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Region #REGION_CSS_CLASSES#" id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES#>',
' <div class="t-Region-header">',
'  <div class="t-Region-headerItems t-Region-headerItems--title">',
'    <span class="t-Region-headerIcon"><span class="t-Icon #ICON_CSS_CLASSES#" aria-hidden="true"></span></span>',
'    <h2 class="t-Region-title" id="#REGION_STATIC_ID#_heading">#TITLE#</h2>',
'  </div>',
'  <div class="t-Region-headerItems t-Region-headerItems--buttons">#COPY##EDIT#<span class="js-maximizeButtonContainer"></span></div>',
' </div>',
' <div class="t-Region-bodyWrap">',
'   <div class="t-Region-buttons t-Region-buttons--top">',
'    <div class="t-Region-buttons-left">#PREVIOUS#</div>',
'    <div class="t-Region-buttons-right">#NEXT#</div>',
'   </div>',
'   <div class="t-Region-body">',
'     #BODY#',
'     #SUB_REGIONS#',
'   </div>',
'   <div class="t-Region-buttons t-Region-buttons--bottom">',
'    <div class="t-Region-buttons-left">#CLOSE##HELP#</div>',
'    <div class="t-Region-buttons-right">#DELETE##CHANGE##CREATE#</div>',
'   </div>',
' </div>',
'</div>',
''))
,p_page_plug_template_name=>'Standard'
,p_internal_name=>'STANDARD'
,p_plug_table_bgcolor=>'#ffffff'
,p_theme_id=>42
,p_theme_class_id=>8
,p_preset_template_options=>'t-Region--scrollBody'
,p_plug_heading_bgcolor=>'#ffffff'
,p_plug_font_size=>'-1'
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>4070912133526059312
,p_translate_this_template=>'N'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9765309431688020)
,p_plug_template_id=>wwv_flow_api.id(9765042323688020)
,p_name=>'Region Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9765609193688020)
,p_plug_template_id=>wwv_flow_api.id(9765042323688020)
,p_name=>'Sub Regions'
,p_placeholder=>'SUB_REGIONS'
,p_has_grid_support=>true
,p_glv_new_row=>true
,p_max_fixed_grid_columns=>12
);
end;
/
prompt --application/shared_components/user_interface/templates/region/tabs_container
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9771800871688026)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-TabsRegion #REGION_CSS_CLASSES# apex-tabs-region" #REGION_ATTRIBUTES# id="#REGION_STATIC_ID#">',
'  #BODY#',
'  <div class="t-TabsRegion-items">',
'    #SUB_REGIONS#',
'  </div>',
'</div>'))
,p_sub_plug_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div data-label="#SUB_REGION_TITLE#" id="SR_#SUB_REGION_ID#">',
'  #SUB_REGION#',
'</div>'))
,p_page_plug_template_name=>'Tabs Container'
,p_internal_name=>'TABS_CONTAINER'
,p_javascript_file_urls=>'#IMAGE_PREFIX#libraries/apex/#MIN_DIRECTORY#widget.apexTabs#MIN#.js?v=#APEX_VERSION#'
,p_theme_id=>42
,p_theme_class_id=>5
,p_preset_template_options=>'t-TabsRegion-mod--simple'
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>3221725015618492759
,p_translate_this_template=>'N'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9772182257688027)
,p_plug_template_id=>wwv_flow_api.id(9771800871688026)
,p_name=>'Region Body'
,p_placeholder=>'BODY'
,p_has_grid_support=>true
,p_glv_new_row=>true
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9772495952688027)
,p_plug_template_id=>wwv_flow_api.id(9771800871688026)
,p_name=>'Tabs'
,p_placeholder=>'SUB_REGIONS'
,p_has_grid_support=>false
,p_glv_new_row=>true
);
end;
/
prompt --application/shared_components/user_interface/templates/region/title_bar
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9774426068688028)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES# class="t-BreadcrumbRegion #REGION_CSS_CLASSES#"> ',
'  <div class="t-BreadcrumbRegion-body">',
'    <div class="t-BreadcrumbRegion-breadcrumb">',
'      #BODY#',
'    </div>',
'    <div class="t-BreadcrumbRegion-title">',
'      <h1 class="t-BreadcrumbRegion-titleText">#TITLE#</h1>',
'    </div>',
'  </div>',
'  <div class="t-BreadcrumbRegion-buttons">#PREVIOUS##CLOSE##DELETE##HELP##CHANGE##EDIT##COPY##CREATE##NEXT#</div>',
'</div>'))
,p_page_plug_template_name=>'Title Bar'
,p_internal_name=>'TITLE_BAR'
,p_theme_id=>42
,p_theme_class_id=>6
,p_default_template_options=>'t-BreadcrumbRegion--showBreadcrumb'
,p_preset_template_options=>'t-BreadcrumbRegion--useBreadcrumbTitle'
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>2530016523834132090
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/region/wizard_container
begin
wwv_flow_api.create_plug_template(
 p_id=>wwv_flow_api.id(9775498010688029)
,p_layout=>'TABLE'
,p_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Wizard #REGION_CSS_CLASSES#" id="#REGION_STATIC_ID#" #REGION_ATTRIBUTES#>',
'  <div class="t-Wizard-header">',
'    <h1 class="t-Wizard-title">#TITLE#</h1>',
'    <div class="u-Table t-Wizard-controls">',
'      <div class="u-Table-fit t-Wizard-buttons">#PREVIOUS##CLOSE#</div>',
'      <div class="u-Table-fill t-Wizard-steps">',
'        #BODY#',
'      </div>',
'      <div class="u-Table-fit t-Wizard-buttons">#NEXT#</div>',
'    </div>',
'  </div>',
'  <div class="t-Wizard-body">',
'    #SUB_REGIONS#',
'  </div>',
'</div>'))
,p_page_plug_template_name=>'Wizard Container'
,p_internal_name=>'WIZARD_CONTAINER'
,p_theme_id=>42
,p_theme_class_id=>8
,p_preset_template_options=>'t-Wizard--hideStepsXSmall'
,p_default_label_alignment=>'RIGHT'
,p_default_field_alignment=>'LEFT'
,p_reference_id=>2117602213152591491
,p_translate_this_template=>'N'
);
wwv_flow_api.create_plug_tmpl_display_point(
 p_id=>wwv_flow_api.id(9775724996688029)
,p_plug_template_id=>wwv_flow_api.id(9775498010688029)
,p_name=>'Wizard Sub Regions'
,p_placeholder=>'SUB_REGIONS'
,p_has_grid_support=>true
,p_glv_new_row=>true
);
end;
/
prompt --application/shared_components/user_interface/templates/list/badge_list
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9797511594688059)
,p_list_template_current=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-BadgeList-item #A02#">',
'  <a class="t-BadgeList-wrap u-color #A04#" href="#LINK#" #A03#>',
'  <span class="t-BadgeList-label">#TEXT#</span>',
'  <span class="t-BadgeList-value">#A01#</span>',
'  </a>',
'</li>'))
,p_list_template_noncurrent=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-BadgeList-item #A02#">',
'  <a class="t-BadgeList-wrap u-color #A04#" href="#LINK#" #A03#>',
'  <span class="t-BadgeList-label">#TEXT#</span>',
'  <span class="t-BadgeList-value">#A01#</span>',
'  </a>',
'</li>'))
,p_list_template_name=>'Badge List'
,p_internal_name=>'BADGE_LIST'
,p_theme_id=>42
,p_theme_class_id=>3
,p_preset_template_options=>'t-BadgeList--large:t-BadgeList--cols t-BadgeList--3cols:t-BadgeList--circular'
,p_list_template_before_rows=>'<ul class="t-BadgeList #COMPONENT_CSS_CLASSES#">'
,p_list_template_after_rows=>'</ul>'
,p_a01_label=>'Value'
,p_a02_label=>'List item CSS Classes'
,p_a03_label=>'Link Attributes'
,p_a04_label=>'Link Classes'
,p_reference_id=>2062482847268086664
,p_list_template_comment=>wwv_flow_string.join(wwv_flow_t_varchar2(
'A01: Large Number',
'A02: List Item Classes',
'A03: Link Attributes'))
);
end;
/
prompt --application/shared_components/user_interface/templates/list/cards
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9801570396688067)
,p_list_template_current=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-Cards-item is-active #A04#">',
'  <div class="t-Card">',
'    <a href="#LINK#" class="t-Card-wrap" #A05#>',
'      <div class="t-Card-icon u-color #A06#"><span class="t-Icon #ICON_CSS_CLASSES#"><span class="t-Card-initials" role="presentation">#A03#</span></span></div>',
'      <div class="t-Card-titleWrap"><h3 class="t-Card-title">#TEXT#</h3><h4 class="t-Card-subtitle">#A07#</h4></div>',
'      <div class="t-Card-body">',
'        <div class="t-Card-desc">#A01#</div>',
'        <div class="t-Card-info">#A02#</div>',
'      </div>',
'      <span class="t-Card-colorFill u-color #A06#"></span>',
'    </a>',
'  </div>',
'</li>'))
,p_list_template_noncurrent=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-Cards-item #A04#">',
'  <div class="t-Card">',
'    <a href="#LINK#" class="t-Card-wrap" #A05#>',
'      <div class="t-Card-icon u-color #A06#"><span class="t-Icon #ICON_CSS_CLASSES#"><span class="t-Card-initials" role="presentation">#A03#</span></span></div>',
'      <div class="t-Card-titleWrap"><h3 class="t-Card-title">#TEXT#</h3><h4 class="t-Card-subtitle">#A07#</h4></div>',
'      <div class="t-Card-body">',
'        <div class="t-Card-desc">#A01#</div>',
'        <div class="t-Card-info">#A02#</div>',
'      </div>',
'      <span class="t-Card-colorFill u-color #A06#"></span>',
'    </a>',
'  </div>',
'</li>'))
,p_list_template_name=>'Cards'
,p_internal_name=>'CARDS'
,p_theme_id=>42
,p_theme_class_id=>4
,p_preset_template_options=>'t-Cards--animColorFill:t-Cards--3cols:t-Cards--basic'
,p_list_template_before_rows=>'<ul class="t-Cards #COMPONENT_CSS_CLASSES#">'
,p_list_template_after_rows=>'</ul>'
,p_a01_label=>'Description'
,p_a02_label=>'Secondary Information'
,p_a03_label=>'Initials'
,p_a04_label=>'List Item CSS Classes'
,p_a05_label=>'Link Attributes'
,p_a06_label=>'Card Color Class'
,p_a07_label=>'Subtitle'
,p_reference_id=>2885322685880632508
);
end;
/
prompt --application/shared_components/user_interface/templates/list/links_list
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9807187050688071)
,p_list_template_current=>'<li class="t-LinksList-item is-current #A03#"><a href="#LINK#" class="t-LinksList-link" #A02#><span class="t-LinksList-icon"><span class="t-Icon #ICON_CSS_CLASSES#"></span></span><span class="t-LinksList-label">#TEXT#</span><span class="t-LinksList-b'
||'adge">#A01#</span></a></li>'
,p_list_template_noncurrent=>'<li class="t-LinksList-item #A03#"><a href="#LINK#" class="t-LinksList-link" #A02#><span class="t-LinksList-icon"><span class="t-Icon #ICON_CSS_CLASSES#"></span></span><span class="t-LinksList-label">#TEXT#</span><span class="t-LinksList-badge">#A01#'
||'</span></a></li>'
,p_list_template_name=>'Links List'
,p_internal_name=>'LINKS_LIST'
,p_theme_id=>42
,p_theme_class_id=>18
,p_list_template_before_rows=>'<ul class="t-LinksList #COMPONENT_CSS_CLASSES#" id="#LIST_ID#">'
,p_list_template_after_rows=>'</ul>'
,p_before_sub_list=>'<ul class="t-LinksList-list">'
,p_after_sub_list=>'</ul>'
,p_sub_list_item_current=>'<li class="t-LinksList-item is-current #A03#"><a href="#LINK#" class="t-LinksList-link" #A02#><span class="t-LinksList-icon"><span class="t-Icon #ICON_CSS_CLASSES#"></span></span><span class="t-LinksList-label">#TEXT#</span><span class="t-LinksList-b'
||'adge">#A01#</span></a></li>'
,p_sub_list_item_noncurrent=>'<li class="t-LinksList-item #A03#"><a href="#LINK#" class="t-LinksList-link" #A02#><span class="t-LinksList-icon"><span class="t-Icon #ICON_CSS_CLASSES#"></span></span><span class="t-LinksList-label">#TEXT#</span><span class="t-LinksList-badge">#A01#'
||'</span></a></li>'
,p_item_templ_curr_w_child=>'<li class="t-LinksList-item is-current is-expanded #A03#"><a href="#LINK#" class="t-LinksList-link" #A02#><span class="t-LinksList-icon"><span class="t-Icon #ICON_CSS_CLASSES#"></span></span><span class="t-LinksList-label">#TEXT#</span><span class="t'
||'-LinksList-badge">#A01#</span></a>#SUB_LISTS#</li>'
,p_item_templ_noncurr_w_child=>'<li class="t-LinksList-item #A03#"><a href="#LINK#" class="t-LinksList-link" #A02#><span class="t-LinksList-icon"><span class="t-Icon #ICON_CSS_CLASSES#"></span></span><span class="t-LinksList-label">#TEXT#</span><span class="t-LinksList-badge">#A01#'
||'</span></a></li>'
,p_a01_label=>'Badge Value'
,p_a02_label=>'Link Attributes'
,p_a03_label=>'List Item CSS Classes'
,p_reference_id=>4070914341144059318
);
end;
/
prompt --application/shared_components/user_interface/templates/list/media_list
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9808756458688073)
,p_list_template_current=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-MediaList-item is-active #A04#">',
'    <a href="#LINK#" class="t-MediaList-itemWrap #A05#" #A03#>',
'        <div class="t-MediaList-iconWrap">',
'            <span class="t-MediaList-icon u-color #A06#"><span class="t-Icon #ICON_CSS_CLASSES#" #IMAGE_ATTR#></span></span>',
'        </div>',
'        <div class="t-MediaList-body">',
'            <h3 class="t-MediaList-title">#TEXT#</h3>',
'            <p class="t-MediaList-desc">#A01#</p>',
'        </div>',
'        <div class="t-MediaList-badgeWrap">',
'            <span class="t-MediaList-badge">#A02#</span>',
'        </div>',
'    </a>',
'</li>'))
,p_list_template_noncurrent=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-MediaList-item  #A04#">',
'    <a href="#LINK#" class="t-MediaList-itemWrap #A05#" #A03#>',
'        <div class="t-MediaList-iconWrap">',
'            <span class="t-MediaList-icon u-color #A06#"><span class="t-Icon #ICON_CSS_CLASSES#" #IMAGE_ATTR#></span></span>',
'        </div>',
'        <div class="t-MediaList-body">',
'            <h3 class="t-MediaList-title">#TEXT#</h3>',
'            <p class="t-MediaList-desc">#A01#</p>',
'        </div>',
'        <div class="t-MediaList-badgeWrap">',
'            <span class="t-MediaList-badge">#A02#</span>',
'        </div>',
'    </a>',
'</li>'))
,p_list_template_name=>'Media List'
,p_internal_name=>'MEDIA_LIST'
,p_theme_id=>42
,p_theme_class_id=>5
,p_default_template_options=>'t-MediaList--showIcons:t-MediaList--showDesc'
,p_list_template_before_rows=>'<ul class="t-MediaList #COMPONENT_CSS_CLASSES#">'
,p_list_template_after_rows=>'</ul>'
,p_a01_label=>'Description'
,p_a02_label=>'Badge Value'
,p_a03_label=>'Link Attributes'
,p_a04_label=>'List Item CSS Classes'
,p_a05_label=>'Link Class'
,p_a06_label=>'Icon Color Class'
,p_reference_id=>2066548068783481421
);
end;
/
prompt --application/shared_components/user_interface/templates/list/menu_bar
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9811531114688075)
,p_list_template_current=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_list_template_noncurrent=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_list_template_name=>'Menu Bar'
,p_internal_name=>'MENU_BAR'
,p_javascript_code_onload=>wwv_flow_string.join(wwv_flow_t_varchar2(
'var e = apex.jQuery("##PARENT_STATIC_ID#_menubar", apex.gPageContext$);',
'if (e.hasClass("js-addActions")) {',
'  apex.actions.addFromMarkup( e );',
'}',
'e.menu({',
'  behaveLikeTabs: e.hasClass("js-tabLike"),',
'  menubarShowSubMenuIcon: e.hasClass("js-showSubMenuIcons") || null,',
'  iconType: ''fa'',',
'  slide: e.hasClass("js-slide"),',
'  menubar: true,',
'  menubarOverflow: true',
'});'))
,p_theme_id=>42
,p_theme_class_id=>20
,p_default_template_options=>'js-showSubMenuIcons'
,p_list_template_before_rows=>'<div class="t-MenuBar #COMPONENT_CSS_CLASSES#" id="#PARENT_STATIC_ID#_menubar"><ul style="display:none">'
,p_list_template_after_rows=>'</ul></div>'
,p_before_sub_list=>'<ul>'
,p_after_sub_list=>'</ul></li>'
,p_sub_list_item_current=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_sub_list_item_noncurrent=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_item_templ_curr_w_child=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_item_templ_noncurr_w_child=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_sub_templ_curr_w_child=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_sub_templ_noncurr_w_child=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_reference_id=>2008709236185638887
);
end;
/
prompt --application/shared_components/user_interface/templates/list/menu_popup
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9812503983688076)
,p_list_template_current=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>',
''))
,p_list_template_noncurrent=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>',
''))
,p_list_template_name=>'Menu Popup'
,p_internal_name=>'MENU_POPUP'
,p_javascript_code_onload=>wwv_flow_string.join(wwv_flow_t_varchar2(
'var e = apex.jQuery("##PARENT_STATIC_ID#_menu", apex.gPageContext$);',
'if (e.hasClass("js-addActions")) {',
'  apex.actions.addFromMarkup( e );',
'}',
'e.menu({ slide: e.hasClass("js-slide"), iconType: ''fa''});'))
,p_theme_id=>42
,p_theme_class_id=>20
,p_list_template_before_rows=>'<div id="#PARENT_STATIC_ID#_menu" class="#COMPONENT_CSS_CLASSES#" style="display:none;"><ul>'
,p_list_template_after_rows=>'</ul></div>'
,p_before_sub_list=>'<ul>'
,p_after_sub_list=>'</ul></li>'
,p_sub_list_item_current=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_sub_list_item_noncurrent=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_item_templ_curr_w_child=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_item_templ_noncurr_w_child=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_sub_templ_curr_w_child=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_sub_templ_noncurr_w_child=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_a01_label=>'Data ID'
,p_a02_label=>'Disabled (True/False)'
,p_a03_label=>'Hidden (True/False)'
,p_a04_label=>'Title Attribute'
,p_a05_label=>'Shortcut'
,p_reference_id=>3492264004432431646
);
end;
/
prompt --application/shared_components/user_interface/templates/list/navigation_bar
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9812990164688077)
,p_list_template_current=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-NavigationBar-item is-active #A02#">',
'  <a class="t-Button t-Button--icon t-Button--header t-Button--navBar" href="#LINK#">',
'      <span class="t-Icon #ICON_CSS_CLASSES#"></span><span class="t-Button-label">#TEXT_ESC_SC#</span><span class="t-Button-badge">#A01#</span>',
'  </a>',
'</li>'))
,p_list_template_noncurrent=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-NavigationBar-item #A02#">',
'  <a class="t-Button t-Button--icon t-Button--header t-Button--navBar" href="#LINK#">',
'    <span class="t-Icon #ICON_CSS_CLASSES#"></span><span class="t-Button-label">#TEXT_ESC_SC#</span><span class="t-Button-badge">#A01#</span>',
'  </a>',
'</li>'))
,p_list_template_name=>'Navigation Bar'
,p_internal_name=>'NAVIGATION_BAR'
,p_theme_id=>42
,p_theme_class_id=>20
,p_list_template_before_rows=>'<ul class="t-NavigationBar #COMPONENT_CSS_CLASSES#" id="#LIST_ID#">'
,p_list_template_after_rows=>'</ul>'
,p_before_sub_list=>'<div class="t-NavigationBar-menu" style="display: none" id="menu_#PARENT_LIST_ITEM_ID#"><ul>'
,p_after_sub_list=>'</ul></div></li>'
,p_sub_list_item_current=>'<li data-current="true" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#">#TEXT_ESC_SC#</a></li>'
,p_sub_list_item_noncurrent=>'<li data-current="false" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#">#TEXT_ESC_SC#</a></li>'
,p_item_templ_curr_w_child=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-NavigationBar-item is-active #A02#">',
'  <button class="t-Button t-Button--icon t-Button t-Button--header t-Button--navBar js-menuButton" type="button" id="#LIST_ITEM_ID#" data-menu="menu_#LIST_ITEM_ID#">',
'      <span class="t-Icon #ICON_CSS_CLASSES#"></span><span class="t-Button-label">#TEXT_ESC_SC#</span><span class="t-Button-badge">#A01#</span><span class="a-Icon icon-down-arrow"></span>',
'  </button>'))
,p_item_templ_noncurr_w_child=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-NavigationBar-item #A02#">',
'  <button class="t-Button t-Button--icon t-Button t-Button--header t-Button--navBar js-menuButton" type="button" id="#LIST_ITEM_ID#" data-menu="menu_#LIST_ITEM_ID#">',
'      <span class="t-Icon #ICON_CSS_CLASSES#"></span><span class="t-Button-label">#TEXT_ESC_SC#</span><span class="t-Button-badge">#A01#</span><span class="a-Icon icon-down-arrow"></span>',
'  </button>'))
,p_sub_templ_curr_w_child=>'<li data-current="true" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#">#TEXT_ESC_SC#</a></li>'
,p_sub_templ_noncurr_w_child=>'<li data-current="false" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#">#TEXT_ESC_SC#</a></li>'
,p_a01_label=>'Badge Value'
,p_a02_label=>'List  Item CSS Classes'
,p_reference_id=>2846096252961119197
);
end;
/
prompt --application/shared_components/user_interface/templates/list/side_navigation_menu
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9813182182688077)
,p_list_template_current=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_list_template_noncurrent=>'<li data-id="#A01#" data-disabled="#A02#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_list_template_name=>'Side Navigation Menu'
,p_internal_name=>'SIDE_NAVIGATION_MENU'
,p_javascript_file_urls=>'#IMAGE_PREFIX#libraries/apex/#MIN_DIRECTORY#widget.treeView#MIN#.js?v=#APEX_VERSION#'
,p_javascript_code_onload=>'apex.jQuery(''body'').addClass(''t-PageBody--leftNav'');'
,p_theme_id=>42
,p_theme_class_id=>19
,p_preset_template_options=>'t-TreeNav--styleA'
,p_list_template_before_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Body-nav" id="t_Body_nav" role="navigation" aria-label="&APP_TITLE!ATTR.">',
'<div class="t-TreeNav #COMPONENT_CSS_CLASSES#" id="t_TreeNav" data-id="#PARENT_STATIC_ID#_tree" aria-label="&APP_TITLE!ATTR."><ul style="display:none">'))
,p_list_template_after_rows=>'</ul></div></div>'
,p_before_sub_list=>'<ul>'
,p_after_sub_list=>'</ul></li>'
,p_sub_list_item_current=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_sub_list_item_noncurrent=>'<li data-id="#A01#" data-disabled="#A02#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_item_templ_curr_w_child=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_item_templ_noncurr_w_child=>'<li data-id="#A01#" data-disabled="#A02#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_sub_templ_curr_w_child=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_sub_templ_noncurr_w_child=>'<li data-id="#A01#" data-disabled="#A02#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_a01_label=>'ID Attribute'
,p_a02_label=>'Disabled True/False'
,p_a04_label=>'Title'
,p_reference_id=>2466292414354694776
);
end;
/
prompt --application/shared_components/user_interface/templates/list/tabs
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9814107555688078)
,p_list_template_current=>'<li class="t-Tabs-item is-active"><a href="#LINK#" class="t-Tabs-link"><span class="t-Icon #ICON_CSS_CLASSES#"></span><span class="t-Tabs-label">#TEXT#</span></a></li>'
,p_list_template_noncurrent=>'<li class="t-Tabs-item"><a href="#LINK#" class="t-Tabs-link"><span class="t-Icon #ICON_CSS_CLASSES#"></span><span class="t-Tabs-label">#TEXT#</span></a></li>'
,p_list_template_name=>'Tabs'
,p_internal_name=>'TABS'
,p_javascript_file_urls=>'#IMAGE_PREFIX#libraries/apex/#MIN_DIRECTORY#widget.apexTabs#MIN#.js?v=#APEX_VERSION#'
,p_theme_id=>42
,p_theme_class_id=>7
,p_preset_template_options=>'t-Tabs--simple'
,p_list_template_before_rows=>'<ul class="t-Tabs #COMPONENT_CSS_CLASSES#">'
,p_list_template_after_rows=>'</ul>'
,p_reference_id=>3288206686691809997
);
end;
/
prompt --application/shared_components/user_interface/templates/list/top_navigation_menu
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9815734538688080)
,p_list_template_current=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_list_template_noncurrent=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_list_template_name=>'Top Navigation Menu'
,p_internal_name=>'TOP_NAVIGATION_MENU'
,p_javascript_code_onload=>wwv_flow_string.join(wwv_flow_t_varchar2(
'var e = apex.jQuery("##PARENT_STATIC_ID#_menubar", apex.gPageContext$);',
'if (e.hasClass("js-addActions")) {',
'  if ( apex.actions ) {',
'    apex.actions.addFromMarkup( e );',
'  } else {',
'    apex.debug.warn("Include actions.js to support menu shortcuts");',
'  }',
'}',
'e.menu({',
'  behaveLikeTabs: e.hasClass("js-tabLike"),',
'  menubarShowSubMenuIcon: e.hasClass("js-showSubMenuIcons") || null,',
'  slide: e.hasClass("js-slide"),',
'  menubar: true,',
'  menubarOverflow: true',
'});'))
,p_theme_id=>42
,p_theme_class_id=>20
,p_default_template_options=>'js-tabLike'
,p_list_template_before_rows=>'<div class="t-Header-nav-list #COMPONENT_CSS_CLASSES#" id="#PARENT_STATIC_ID#_menubar"><ul style="display:none">'
,p_list_template_after_rows=>'</ul></div>'
,p_before_sub_list=>'<ul>'
,p_after_sub_list=>'</ul></li>'
,p_sub_list_item_current=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_sub_list_item_noncurrent=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a></li>'
,p_item_templ_curr_w_child=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_item_templ_noncurr_w_child=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_sub_templ_curr_w_child=>'<li data-current="true" data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_sub_templ_noncurr_w_child=>'<li data-id="#A01#" data-disabled="#A02#" data-hide="#A03#" data-shortcut="#A05#" data-icon="#ICON_CSS_CLASSES#"><a href="#LINK#" title="#A04#">#TEXT_ESC_SC#</a>'
,p_a01_label=>'ID Attribute'
,p_a02_label=>'Disabled True / False'
,p_a03_label=>'Hide'
,p_a04_label=>'Title Attribute'
,p_a05_label=>'Shortcut Key'
,p_reference_id=>2525307901300239072
);
end;
/
prompt --application/shared_components/user_interface/templates/list/top_navigation_tabs
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9816752314688081)
,p_list_template_current=>'<li class="t-NavTabs-item #A03# is-active" id="#A01#"><a href="#LINK#" class="t-NavTabs-link #A04# " title="#TEXT_ESC_SC#"><span class="t-Icon #ICON_CSS_CLASSES#" aria-hidden="true"></span><span class="t-NavTabs-label">#TEXT_ESC_SC#</span><span class'
||'="t-NavTabs-badge #A05#">#A02#</span></a></li>'
,p_list_template_noncurrent=>'<li class="t-NavTabs-item #A03#" id="#A01#"><a href="#LINK#" class="t-NavTabs-link #A04# " title="#TEXT_ESC_SC#"><span class="t-Icon #ICON_CSS_CLASSES#" aria-hidden="true"></span><span class="t-NavTabs-label">#TEXT_ESC_SC#</span><span class="t-NavTab'
||'s-badge #A05#">#A02#</span></a></li>'
,p_list_template_name=>'Top Navigation Tabs'
,p_internal_name=>'TOP_NAVIGATION_TABS'
,p_theme_id=>42
,p_theme_class_id=>7
,p_preset_template_options=>'t-NavTabs--inlineLabels-lg:t-NavTabs--displayLabels-sm'
,p_list_template_before_rows=>'<ul class="t-NavTabs #COMPONENT_CSS_CLASSES#" id="#PARENT_STATIC_ID#_navtabs">'
,p_list_template_after_rows=>'</ul>'
,p_a01_label=>'List Item ID'
,p_a02_label=>'Badge Value'
,p_a03_label=>'List Item Class'
,p_a04_label=>'Link Class'
,p_a05_label=>'Badge Class'
,p_reference_id=>1453011561172885578
);
end;
/
prompt --application/shared_components/user_interface/templates/list/wizard_progress
begin
wwv_flow_api.create_list_template(
 p_id=>wwv_flow_api.id(9818313839688082)
,p_list_template_current=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-WizardSteps-step is-active" id="#LIST_ITEM_ID#"><div class="t-WizardSteps-wrap" data-link="#LINK#"><span class="t-WizardSteps-marker"></span><span class="t-WizardSteps-label">#TEXT# <span class="t-WizardSteps-labelState"></span></span></'
||'div></li>',
''))
,p_list_template_noncurrent=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-WizardSteps-step" id="#LIST_ITEM_ID#"><div class="t-WizardSteps-wrap" data-link="#LINK#"><span class="t-WizardSteps-marker"></span><span class="t-WizardSteps-label">#TEXT# <span class="t-WizardSteps-labelState"></span></span></div></li>',
''))
,p_list_template_name=>'Wizard Progress'
,p_internal_name=>'WIZARD_PROGRESS'
,p_javascript_code_onload=>'apex.theme.initWizardProgressBar();'
,p_theme_id=>42
,p_theme_class_id=>17
,p_preset_template_options=>'t-WizardSteps--displayLabels'
,p_list_template_before_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<h2 class="u-VisuallyHidden">#CURRENT_PROGRESS#</h2>',
'<ul class="t-WizardSteps #COMPONENT_CSS_CLASSES#" id="#LIST_ID#">'))
,p_list_template_after_rows=>'</ul>'
,p_reference_id=>2008702338707394488
);
end;
/
prompt --application/shared_components/user_interface/templates/report/alerts
begin
wwv_flow_api.create_row_template(
 p_id=>wwv_flow_api.id(9776758426688034)
,p_row_template_name=>'Alerts'
,p_internal_name=>'ALERTS'
,p_row_template1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Alert t-Alert--horizontal t-Alert--colorBG t-Alert--defaultIcons t-Alert--#ALERT_TYPE#" role="alert">',
'  <div class="t-Alert-wrap">',
'    <div class="t-Alert-icon">',
'      <span class="t-Icon"></span>',
'    </div>',
'    <div class="t-Alert-content">',
'      <div class="t-Alert-header">',
'        <h2 class="t-Alert-title">#ALERT_TITLE#</h2>',
'      </div>',
'      <div class="t-Alert-body">',
'        #ALERT_DESC#',
'      </div>',
'    </div>',
'    <div class="t-Alert-buttons">',
'      #ALERT_ACTION#',
'    </div>',
'  </div>',
'</div>'))
,p_row_template_before_rows=>'<div class="t-Alerts #COMPONENT_CSS_CLASSES#" #REPORT_ATTRIBUTES# id="#REGION_STATIC_ID#_alerts" data-region-id="#REGION_STATIC_ID#">'
,p_row_template_after_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</div>',
'<table class="t-Report-pagination" role="presentation">#PAGINATION#</table>'))
,p_row_template_type=>'NAMED_COLUMNS'
,p_row_template_display_cond1=>'0'
,p_row_template_display_cond2=>'0'
,p_row_template_display_cond3=>'0'
,p_row_template_display_cond4=>'0'
,p_pagination_template=>'<span class="t-Report-paginationText">#TEXT#</span>'
,p_next_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS#',
'</a>'))
,p_next_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT_SET#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS_SET#',
'</a>'))
,p_theme_id=>42
,p_theme_class_id=>14
,p_reference_id=>2881456138952347027
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/report/badge_list
begin
wwv_flow_api.create_row_template(
 p_id=>wwv_flow_api.id(9776923303688037)
,p_row_template_name=>'Badge List'
,p_internal_name=>'BADGE_LIST'
,p_row_template1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-BadgeList-item">',
' <span class="t-BadgeList-wrap u-color">',
'  <span class="t-BadgeList-label">#COLUMN_HEADER#</span>',
'  <span class="t-BadgeList-value">#COLUMN_VALUE#</span>',
' </span>',
'</li>'))
,p_row_template_before_rows=>'<ul class="t-BadgeList #COMPONENT_CSS_CLASSES#" data-region-id="#REGION_STATIC_ID#">'
,p_row_template_after_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</ul>',
'<table class="t-Report-pagination" role="presentation">#PAGINATION#</table>'))
,p_row_template_type=>'GENERIC_COLUMNS'
,p_row_template_display_cond1=>'0'
,p_row_template_display_cond2=>'0'
,p_row_template_display_cond3=>'0'
,p_row_template_display_cond4=>'0'
,p_pagination_template=>'<span class="t-Report-paginationText">#TEXT#</span>'
,p_next_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS#',
'</a>'))
,p_next_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT_SET#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS_SET#',
'</a>'))
,p_theme_id=>42
,p_theme_class_id=>6
,p_preset_template_options=>'t-BadgeList--large:t-BadgeList--fixed:t-BadgeList--circular'
,p_reference_id=>2103197159775914759
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/report/cards
begin
wwv_flow_api.create_row_template(
 p_id=>wwv_flow_api.id(9780977451688041)
,p_row_template_name=>'Cards'
,p_internal_name=>'CARDS'
,p_row_template1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-Cards-item #CARD_MODIFIERS#">',
'  <div class="t-Card">',
'    <a href="#CARD_LINK#" class="t-Card-wrap">',
'      <div class="t-Card-icon u-color #CARD_COLOR#"><span class="t-Icon fa #CARD_ICON#"><span class="t-Card-initials" role="presentation">#CARD_INITIALS#</span></span></div>',
'      <div class="t-Card-titleWrap"><h3 class="t-Card-title">#CARD_TITLE#</h3><h4 class="t-Card-subtitle">#CARD_SUBTITLE#</h4></div>',
'      <div class="t-Card-body">',
'        <div class="t-Card-desc">#CARD_TEXT#</div>',
'        <div class="t-Card-info">#CARD_SUBTEXT#</div>',
'      </div>',
'      <span class="t-Card-colorFill u-color #CARD_COLOR#"></span>',
'    </a>',
'  </div>',
'</li>'))
,p_row_template_condition1=>':CARD_LINK is not null'
,p_row_template2=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-Cards-item #CARD_MODIFIERS#">',
'  <div class="t-Card">',
'    <div class="t-Card-wrap">',
'      <div class="t-Card-icon u-color #CARD_COLOR#"><span class="t-Icon fa #CARD_ICON#"><span class="t-Card-initials" role="presentation">#CARD_INITIALS#</span></span></div>',
'      <div class="t-Card-titleWrap"><h3 class="t-Card-title">#CARD_TITLE#</h3><h4 class="t-Card-subtitle">#CARD_SUBTITLE#</h4></div>',
'      <div class="t-Card-body">',
'        <div class="t-Card-desc">#CARD_TEXT#</div>',
'        <div class="t-Card-info">#CARD_SUBTEXT#</div>',
'      </div>',
'      <span class="t-Card-colorFill u-color #CARD_COLOR#"></span>',
'    </div>',
'  </div>',
'</li>'))
,p_row_template_before_rows=>'<ul class="t-Cards #COMPONENT_CSS_CLASSES#" #REPORT_ATTRIBUTES# id="#REGION_STATIC_ID#_cards" data-region-id="#REGION_STATIC_ID#">'
,p_row_template_after_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</ul>',
'<table class="t-Report-pagination" role="presentation">#PAGINATION#</table>'))
,p_row_template_type=>'NAMED_COLUMNS'
,p_row_template_display_cond1=>'NOT_CONDITIONAL'
,p_row_template_display_cond2=>'0'
,p_row_template_display_cond3=>'0'
,p_row_template_display_cond4=>'NOT_CONDITIONAL'
,p_pagination_template=>'<span class="t-Report-paginationText">#TEXT#</span>'
,p_next_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS#',
'</a>'))
,p_next_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT_SET#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS_SET#',
'</a>'))
,p_theme_id=>42
,p_theme_class_id=>7
,p_preset_template_options=>'t-Cards--animColorFill:t-Cards--3cols:t-Cards--basic'
,p_reference_id=>2973535649510699732
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/report/comments
begin
wwv_flow_api.create_row_template(
 p_id=>wwv_flow_api.id(9786327444688048)
,p_row_template_name=>'Comments'
,p_internal_name=>'COMMENTS'
,p_row_template1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-Comments-item #COMMENT_MODIFIERS#">',
'    <div class="t-Comments-icon">',
'        <div class="t-Comments-userIcon #ICON_MODIFIER#" aria-hidden="true">#USER_ICON#</div>',
'    </div>',
'    <div class="t-Comments-body">',
'        <div class="t-Comments-info">',
'            #USER_NAME# <span class="t-Comments-date">#COMMENT_DATE#</span> <span class="t-Comments-actions">#ACTIONS#</span>',
'        </div>',
'        <div class="t-Comments-comment">',
'            #COMMENT_TEXT##ATTRIBUTE_1##ATTRIBUTE_2##ATTRIBUTE_3##ATTRIBUTE_4#',
'        </div>',
'    </div>',
'</li>'))
,p_row_template_before_rows=>'<ul class="t-Comments #COMPONENT_CSS_CLASSES#" #REPORT_ATTRIBUTES# id="#REGION_STATIC_ID#_report" data-region-id="#REGION_STATIC_ID#">'
,p_row_template_after_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</ul>',
'<table class="t-Report-pagination" role="presentation">#PAGINATION#</table>'))
,p_row_template_type=>'NAMED_COLUMNS'
,p_row_template_display_cond1=>'0'
,p_row_template_display_cond2=>'NOT_CONDITIONAL'
,p_row_template_display_cond3=>'0'
,p_row_template_display_cond4=>'0'
,p_pagination_template=>'<span class="t-Report-paginationText">#TEXT#</span>'
,p_next_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS#',
'</a>'))
,p_next_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT_SET#<span class="a-Icon icon-right-arrow"></span>',
'</a>',
''))
,p_previous_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS_SET#',
'</a>'))
,p_theme_id=>42
,p_theme_class_id=>7
,p_preset_template_options=>'t-Comments--chat'
,p_reference_id=>2611722012730764232
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/report/media_list
begin
wwv_flow_api.create_row_template(
 p_id=>wwv_flow_api.id(9787594913688049)
,p_row_template_name=>'Media List'
,p_internal_name=>'MEDIA_LIST'
,p_row_template1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-MediaList-item #LIST_CLASS#">',
'    <a href="#LINK#" class="t-MediaList-itemWrap #LINK_CLASS#" #LINK_ATTR#>',
'        <div class="t-MediaList-iconWrap">',
'            <span class="t-MediaList-icon u-color #ICON_COLOR_CLASS#"><span class="t-Icon #ICON_CLASS#"></span></span>',
'        </div>',
'        <div class="t-MediaList-body">',
'            <h3 class="t-MediaList-title">#LIST_TITLE#</h3>',
'            <p class="t-MediaList-desc">#LIST_TEXT#</p>',
'        </div>',
'        <div class="t-MediaList-badgeWrap">',
'            <span class="t-MediaList-badge">#LIST_BADGE#</span>',
'        </div>',
'    </a>',
'</li>'))
,p_row_template_before_rows=>'<ul class="t-MediaList #COMPONENT_CSS_CLASSES#" #REPORT_ATTRIBUTES# id="#REGION_STATIC_ID#_report" data-region-id="#REGION_STATIC_ID#">'
,p_row_template_after_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</ul>',
'<table class="t-Report-pagination" role="presentation">#PAGINATION#</table>'))
,p_row_template_type=>'NAMED_COLUMNS'
,p_row_template_display_cond1=>'0'
,p_row_template_display_cond2=>'0'
,p_row_template_display_cond3=>'0'
,p_row_template_display_cond4=>'0'
,p_pagination_template=>'<span class="t-Report-paginationText">#TEXT#</span>'
,p_next_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS#',
'</a>'))
,p_next_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT_SET#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS_SET#',
'</a>'))
,p_theme_id=>42
,p_theme_class_id=>1
,p_default_template_options=>'t-MediaList--showDesc:t-MediaList--showIcons'
,p_preset_template_options=>'t-MediaList--stack'
,p_reference_id=>2092157460408299055
,p_translate_this_template=>'N'
,p_row_template_comment=>' (SELECT link_text, link_target, detail1, detail2, last_modified)'
);
end;
/
prompt --application/shared_components/user_interface/templates/report/search_results
begin
wwv_flow_api.create_row_template(
 p_id=>wwv_flow_api.id(9790586282688052)
,p_row_template_name=>'Search Results'
,p_internal_name=>'SEARCH_RESULTS'
,p_row_template1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'  <li class="t-SearchResults-item">',
'    <h3 class="t-SearchResults-title"><a href="#SEARCH_LINK#">#SEARCH_TITLE#</a></h3>',
'    <div class="t-SearchResults-info">',
'      <p class="t-SearchResults-desc">#SEARCH_DESC#</p>',
'      <span class="t-SearchResults-misc">#LABEL_01#: #VALUE_01#</span>',
'    </div>',
'  </li>'))
,p_row_template_condition1=>':LABEL_02 is null'
,p_row_template2=>wwv_flow_string.join(wwv_flow_t_varchar2(
'  <li class="t-SearchResults-item">',
'    <h3 class="t-SearchResults-title"><a href="#SEARCH_LINK#">#SEARCH_TITLE#</a></h3>',
'    <div class="t-SearchResults-info">',
'      <p class="t-SearchResults-desc">#SEARCH_DESC#</p>',
'      <span class="t-SearchResults-misc">#LABEL_01#: #VALUE_01#</span>',
'      <span class="t-SearchResults-misc">#LABEL_02#: #VALUE_02#</span>',
'    </div>',
'  </li>'))
,p_row_template_condition2=>':LABEL_03 is null'
,p_row_template3=>wwv_flow_string.join(wwv_flow_t_varchar2(
'  <li class="t-SearchResults-item">',
'    <h3 class="t-SearchResults-title"><a href="#SEARCH_LINK#">#SEARCH_TITLE#</a></h3>',
'    <div class="t-SearchResults-info">',
'      <p class="t-SearchResults-desc">#SEARCH_DESC#</p>',
'      <span class="t-SearchResults-misc">#LABEL_01#: #VALUE_01#</span>',
'      <span class="t-SearchResults-misc">#LABEL_02#: #VALUE_02#</span>',
'      <span class="t-SearchResults-misc">#LABEL_03#: #VALUE_03#</span>',
'    </div>',
'  </li>'))
,p_row_template_condition3=>':LABEL_04 is null'
,p_row_template4=>wwv_flow_string.join(wwv_flow_t_varchar2(
'  <li class="t-SearchResults-item">',
'    <h3 class="t-SearchResults-title"><a href="#SEARCH_LINK#">#SEARCH_TITLE#</a></h3>',
'    <div class="t-SearchResults-info">',
'      <p class="t-SearchResults-desc">#SEARCH_DESC#</p>',
'      <span class="t-SearchResults-misc">#LABEL_01#: #VALUE_01#</span>',
'      <span class="t-SearchResults-misc">#LABEL_02#: #VALUE_02#</span>',
'      <span class="t-SearchResults-misc">#LABEL_03#: #VALUE_03#</span>',
'      <span class="t-SearchResults-misc">#LABEL_04#: #VALUE_04#</span>',
'    </div>',
'  </li>'))
,p_row_template_before_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-SearchResults #COMPONENT_CSS_CLASSES#" #REPORT_ATTRIBUTES# id="#REGION_STATIC_ID#_report" data-region-id="#REGION_STATIC_ID#">',
'<ul class="t-SearchResults-list">'))
,p_row_template_after_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</ul>',
'<table class="t-Report-pagination" role="presentation">#PAGINATION#</table>',
'</div>'))
,p_row_template_type=>'NAMED_COLUMNS'
,p_row_template_display_cond1=>'NOT_CONDITIONAL'
,p_row_template_display_cond2=>'NOT_CONDITIONAL'
,p_row_template_display_cond3=>'NOT_CONDITIONAL'
,p_row_template_display_cond4=>'NOT_CONDITIONAL'
,p_pagination_template=>'<span class="t-Report-paginationText">#TEXT#</span>'
,p_next_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS#',
'</a>'))
,p_next_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT_SET#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS_SET#',
'</a>'))
,p_theme_id=>42
,p_theme_class_id=>1
,p_reference_id=>4070913431524059316
,p_translate_this_template=>'N'
,p_row_template_comment=>' (SELECT link_text, link_target, detail1, detail2, last_modified)'
);
end;
/
prompt --application/shared_components/user_interface/templates/report/standard
begin
wwv_flow_api.create_row_template(
 p_id=>wwv_flow_api.id(9790776953688052)
,p_row_template_name=>'Standard'
,p_internal_name=>'STANDARD'
,p_row_template1=>'<td class="t-Report-cell" #ALIGNMENT# headers="#COLUMN_HEADER_NAME#">#COLUMN_VALUE#</td>'
,p_row_template_before_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Report #COMPONENT_CSS_CLASSES#" id="report_#REGION_STATIC_ID#" #REPORT_ATTRIBUTES# data-region-id="#REGION_STATIC_ID#">',
'  <div class="t-Report-wrap">',
'    <table class="t-Report-pagination" role="presentation">#TOP_PAGINATION#</table>',
'    <div class="t-Report-tableWrap">',
'    <table class="t-Report-report" aria-label="#REGION_TITLE#">'))
,p_row_template_after_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'      </tbody>',
'    </table>',
'    </div>',
'    <div class="t-Report-links">#EXTERNAL_LINK##CSV_LINK#</div>',
'    <table class="t-Report-pagination t-Report-pagination--bottom" role="presentation">#PAGINATION#</table>',
'  </div>',
'</div>'))
,p_row_template_type=>'GENERIC_COLUMNS'
,p_before_column_heading=>'<thead>'
,p_column_heading_template=>'<th class="t-Report-colHead" #ALIGNMENT# id="#COLUMN_HEADER_NAME#" #COLUMN_WIDTH#>#COLUMN_HEADER#</th>'
,p_after_column_heading=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</thead>',
'<tbody>'))
,p_row_template_display_cond1=>'0'
,p_row_template_display_cond2=>'0'
,p_row_template_display_cond3=>'0'
,p_row_template_display_cond4=>'0'
,p_pagination_template=>'<span class="t-Report-paginationText">#TEXT#</span>'
,p_next_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS#',
'</a>'))
,p_next_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT_SET#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS_SET#',
'</a>'))
,p_theme_id=>42
,p_theme_class_id=>4
,p_preset_template_options=>'t-Report--altRowsDefault:t-Report--rowHighlight'
,p_reference_id=>2537207537838287671
,p_translate_this_template=>'N'
);
begin
wwv_flow_api.create_row_template_patch(
 p_id=>wwv_flow_api.id(9790776953688052)
,p_row_template_before_first=>'<tr>'
,p_row_template_after_last=>'</tr>'
);
exception when others then null;
end;
end;
/
prompt --application/shared_components/user_interface/templates/report/timeline
begin
wwv_flow_api.create_row_template(
 p_id=>wwv_flow_api.id(9793319708688054)
,p_row_template_name=>'Timeline'
,p_internal_name=>'TIMELINE'
,p_row_template1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-Timeline-item #EVENT_MODIFIERS#" #EVENT_ATTRIBUTES#>',
'  <div class="t-Timeline-wrap">',
'    <div class="t-Timeline-user">',
'      <div class="t-Timeline-avatar #USER_COLOR#">',
'        #USER_AVATAR#',
'      </div>',
'      <div class="t-Timeline-userinfo">',
'        <span class="t-Timeline-username">#USER_NAME#</span>',
'        <span class="t-Timeline-date">#EVENT_DATE#</span>',
'      </div>',
'    </div>',
'    <div class="t-Timeline-content">',
'      <div class="t-Timeline-typeWrap">',
'        <div class="t-Timeline-type #EVENT_STATUS#">',
'          <span class="t-Icon #EVENT_ICON#"></span>',
'          <span class="t-Timeline-typename">#EVENT_TYPE#</span>',
'        </div>',
'      </div>',
'      <div class="t-Timeline-body">',
'        <h3 class="t-Timeline-title">#EVENT_TITLE#</h3>',
'        <p class="t-Timeline-desc">#EVENT_DESC#</p>',
'      </div>',
'    </div>',
'  </div>',
'</li>'))
,p_row_template_condition1=>':EVENT_LINK is null'
,p_row_template2=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<li class="t-Timeline-item #EVENT_MODIFIERS#" #EVENT_ATTRIBUTES#>',
'  <a href="#EVENT_LINK#" class="t-Timeline-wrap">',
'    <div class="t-Timeline-user">',
'      <div class="t-Timeline-avatar #USER_COLOR#">',
'        #USER_AVATAR#',
'      </div>',
'      <div class="t-Timeline-userinfo">',
'        <span class="t-Timeline-username">#USER_NAME#</span>',
'        <span class="t-Timeline-date">#EVENT_DATE#</span>',
'      </div>',
'    </div>',
'    <div class="t-Timeline-content">',
'      <div class="t-Timeline-typeWrap">',
'        <div class="t-Timeline-type #EVENT_STATUS#">',
'          <span class="t-Icon #EVENT_ICON#"></span>',
'          <span class="t-Timeline-typename">#EVENT_TYPE#</span>',
'        </div>',
'      </div>',
'      <div class="t-Timeline-body">',
'        <h3 class="t-Timeline-title">#EVENT_TITLE#</h3>',
'        <p class="t-Timeline-desc">#EVENT_DESC#</p>',
'      </div>',
'    </div>',
'  </a>',
'</li>'))
,p_row_template_before_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<ul class="t-Timeline #COMPONENT_CSS_CLASSES#" #REPORT_ATTRIBUTES# id="#REGION_STATIC_ID#_timeline" data-region-id="#REGION_STATIC_ID#">',
''))
,p_row_template_after_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</ul>',
'<table class="t-Report-pagination" role="presentation">#PAGINATION#</table>'))
,p_row_template_type=>'NAMED_COLUMNS'
,p_row_template_display_cond1=>'NOT_CONDITIONAL'
,p_row_template_display_cond2=>'0'
,p_row_template_display_cond3=>'0'
,p_row_template_display_cond4=>'NOT_CONDITIONAL'
,p_pagination_template=>'<span class="t-Report-paginationText">#TEXT#</span>'
,p_next_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS#',
'</a>'))
,p_next_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT_SET#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS_SET#',
'</a>'))
,p_theme_id=>42
,p_theme_class_id=>7
,p_reference_id=>1513373588340069864
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/report/value_attribute_pairs_column
begin
wwv_flow_api.create_row_template(
 p_id=>wwv_flow_api.id(9793749257688055)
,p_row_template_name=>'Value Attribute Pairs - Column'
,p_internal_name=>'VALUE_ATTRIBUTE_PAIRS_COLUMN'
,p_row_template1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<dt class="t-AVPList-label">',
'  #COLUMN_HEADER#',
'</dt>',
'<dd class="t-AVPList-value">',
'  #COLUMN_VALUE#',
'</dd>'))
,p_row_template_before_rows=>'<dl class="t-AVPList #COMPONENT_CSS_CLASSES#" #REPORT_ATTRIBUTES# data-region-id="#REGION_STATIC_ID#">'
,p_row_template_after_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</dl>',
'<table class="t-Report-pagination" role="presentation">#PAGINATION#</table>'))
,p_row_template_type=>'GENERIC_COLUMNS'
,p_row_template_display_cond1=>'0'
,p_row_template_display_cond2=>'0'
,p_row_template_display_cond3=>'0'
,p_row_template_display_cond4=>'0'
,p_pagination_template=>'<span class="t-Report-paginationText">#TEXT#</span>'
,p_next_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS#',
'</a>'))
,p_next_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT_SET#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS_SET#',
'</a>'))
,p_theme_id=>42
,p_theme_class_id=>6
,p_preset_template_options=>'t-AVPList--leftAligned'
,p_reference_id=>2099068636272681754
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/report/value_attribute_pairs_row
begin
wwv_flow_api.create_row_template(
 p_id=>wwv_flow_api.id(9795721115688056)
,p_row_template_name=>'Value Attribute Pairs - Row'
,p_internal_name=>'VALUE_ATTRIBUTE_PAIRS_ROW'
,p_row_template1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<dt class="t-AVPList-label">',
'  #1#',
'</dt>',
'<dd class="t-AVPList-value">',
'  #2#',
'</dd>'))
,p_row_template_before_rows=>'<dl class="t-AVPList #COMPONENT_CSS_CLASSES#" #REPORT_ATTRIBUTES# id="report_#REGION_STATIC_ID#" data-region-id="#REGION_STATIC_ID#">'
,p_row_template_after_rows=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</dl>',
'<table class="t-Report-pagination" role="presentation">#PAGINATION#</table>'))
,p_row_template_type=>'NAMED_COLUMNS'
,p_row_template_display_cond1=>'0'
,p_row_template_display_cond2=>'0'
,p_row_template_display_cond3=>'0'
,p_row_template_display_cond4=>'0'
,p_pagination_template=>'<span class="t-Report-paginationText">#TEXT#</span>'
,p_next_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_page_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS#',
'</a>'))
,p_next_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--next">',
'  #PAGINATION_NEXT_SET#<span class="a-Icon icon-right-arrow"></span>',
'</a>'))
,p_previous_set_template=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<a href="#LINK#" class="t-Button t-Button--small t-Button--noUI t-Report-paginationLink t-Report-paginationLink--prev">',
'  <span class="a-Icon icon-left-arrow"></span>#PAGINATION_PREVIOUS_SET#',
'</a>'))
,p_theme_id=>42
,p_theme_class_id=>7
,p_preset_template_options=>'t-AVPList--leftAligned'
,p_reference_id=>2099068321678681753
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/label/hidden
begin
wwv_flow_api.create_field_template(
 p_id=>wwv_flow_api.id(9819754494688084)
,p_template_name=>'Hidden'
,p_internal_name=>'HIDDEN'
,p_template_body1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Form-labelContainer t-Form-labelContainer--hiddenLabel col col-#LABEL_COLUMN_SPAN_NUMBER#">',
'<label for="#CURRENT_ITEM_NAME#" id="#LABEL_ID#" class="t-Form-label u-VisuallyHidden">'))
,p_template_body2=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</label>',
'</div>'))
,p_before_item=>'<div class="t-Form-fieldContainer t-Form-fieldContainer--hiddenLabel rel-col #ITEM_CSS_CLASSES#" id="#CURRENT_ITEM_CONTAINER_ID#">'
,p_after_item=>'</div>'
,p_item_pre_text=>'<span class="t-Form-itemText t-Form-itemText--pre">#CURRENT_ITEM_PRE_TEXT#</span>'
,p_item_post_text=>'<span class="t-Form-itemText t-Form-itemText--post">#CURRENT_ITEM_POST_TEXT#</span>'
,p_before_element=>'<div class="t-Form-inputContainer col col-#ITEM_COLUMN_SPAN_NUMBER#"><div class="t-Form-itemWrapper">#ITEM_PRE_TEXT#'
,p_after_element=>'#ITEM_POST_TEXT##HELP_TEMPLATE#</div>#INLINE_HELP_TEMPLATE##ERROR_TEMPLATE#</div>'
,p_help_link=>'<button class="t-Form-helpButton js-itemHelp" data-itemhelp="#CURRENT_ITEM_ID#" title="#CURRENT_ITEM_HELP_LABEL#" aria-label="#CURRENT_ITEM_HELP_LABEL#" tabindex="-1" type="button"><span class="a-Icon icon-help" aria-hidden="true"></span></button>'
,p_inline_help_text=>'<span class="t-Form-inlineHelp">#CURRENT_ITEM_INLINE_HELP_TEXT#</span>'
,p_error_template=>'<span class="t-Form-error">#ERROR_MESSAGE#</span>'
,p_theme_id=>42
,p_theme_class_id=>13
,p_reference_id=>2039339104148359505
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/label/optional
begin
wwv_flow_api.create_field_template(
 p_id=>wwv_flow_api.id(9819866831688087)
,p_template_name=>'Optional'
,p_internal_name=>'OPTIONAL'
,p_template_body1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Form-labelContainer col col-#LABEL_COLUMN_SPAN_NUMBER#">',
'<label for="#CURRENT_ITEM_NAME#" id="#LABEL_ID#" class="t-Form-label">'))
,p_template_body2=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</label>',
'</div>',
''))
,p_before_item=>'<div class="t-Form-fieldContainer rel-col #ITEM_CSS_CLASSES#" id="#CURRENT_ITEM_CONTAINER_ID#">'
,p_after_item=>'</div>'
,p_item_pre_text=>'<span class="t-Form-itemText t-Form-itemText--pre">#CURRENT_ITEM_PRE_TEXT#</span>'
,p_item_post_text=>'<span class="t-Form-itemText t-Form-itemText--post">#CURRENT_ITEM_POST_TEXT#</span>'
,p_before_element=>'<div class="t-Form-inputContainer col col-#ITEM_COLUMN_SPAN_NUMBER#"><div class="t-Form-itemWrapper">#ITEM_PRE_TEXT#'
,p_after_element=>'#ITEM_POST_TEXT##HELP_TEMPLATE#</div>#INLINE_HELP_TEMPLATE##ERROR_TEMPLATE#</div>'
,p_help_link=>'<button class="t-Form-helpButton js-itemHelp" data-itemhelp="#CURRENT_ITEM_ID#" title="#CURRENT_ITEM_HELP_LABEL#" aria-label="#CURRENT_ITEM_HELP_LABEL#" tabindex="-1" type="button"><span class="a-Icon icon-help" aria-hidden="true"></span></button>'
,p_inline_help_text=>'<span class="t-Form-inlineHelp">#CURRENT_ITEM_INLINE_HELP_TEXT#</span>'
,p_error_template=>'<span class="t-Form-error">#ERROR_MESSAGE#</span>'
,p_theme_id=>42
,p_theme_class_id=>3
,p_reference_id=>2317154212072806530
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/label/optional_above
begin
wwv_flow_api.create_field_template(
 p_id=>wwv_flow_api.id(9819909393688087)
,p_template_name=>'Optional - Above'
,p_internal_name=>'OPTIONAL_ABOVE'
,p_template_body1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Form-labelContainer">',
'<label for="#CURRENT_ITEM_NAME#" id="#LABEL_ID#" class="t-Form-label">'))
,p_template_body2=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</label>#HELP_TEMPLATE#',
'</div>'))
,p_before_item=>'<div class="t-Form-fieldContainer t-Form-fieldContainer--stacked #ITEM_CSS_CLASSES#" id="#CURRENT_ITEM_CONTAINER_ID#">'
,p_after_item=>'</div>'
,p_item_pre_text=>'<span class="t-Form-itemText t-Form-itemText--pre">#CURRENT_ITEM_PRE_TEXT#</span>'
,p_item_post_text=>'<span class="t-Form-itemText t-Form-itemText--post">#CURRENT_ITEM_POST_TEXT#</span>'
,p_before_element=>'<div class="t-Form-inputContainer"><div class="t-Form-itemWrapper">#ITEM_PRE_TEXT#'
,p_after_element=>'#ITEM_POST_TEXT#</div>#INLINE_HELP_TEMPLATE##ERROR_TEMPLATE#</div>'
,p_help_link=>'<button class="t-Form-helpButton js-itemHelp" data-itemhelp="#CURRENT_ITEM_ID#" title="#CURRENT_ITEM_HELP_LABEL#" aria-label="#CURRENT_ITEM_HELP_LABEL#" tabindex="-1" type="button"><span class="a-Icon icon-help" aria-hidden="true"></span></button>'
,p_inline_help_text=>'<span class="t-Form-inlineHelp">#CURRENT_ITEM_INLINE_HELP_TEXT#</span>'
,p_error_template=>'<span class="t-Form-error">#ERROR_MESSAGE#</span>'
,p_theme_id=>42
,p_theme_class_id=>3
,p_reference_id=>3030114864004968404
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/label/optional_floating
begin
wwv_flow_api.create_field_template(
 p_id=>wwv_flow_api.id(9820028477688087)
,p_template_name=>'Optional - Floating'
,p_internal_name=>'OPTIONAL_FLOATING'
,p_template_body1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Form-labelContainer">',
'<label for="#CURRENT_ITEM_NAME#" id="#LABEL_ID#" class="t-Form-label">'))
,p_template_body2=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</label>',
'</div>'))
,p_before_item=>'<div class="t-Form-fieldContainer t-Form-fieldContainer--floatingLabel #ITEM_CSS_CLASSES#" id="#CURRENT_ITEM_CONTAINER_ID#">'
,p_after_item=>'</div>'
,p_item_pre_text=>'<span class="t-Form-itemText t-Form-itemText--pre">#CURRENT_ITEM_PRE_TEXT#</span>'
,p_item_post_text=>'<span class="t-Form-itemText t-Form-itemText--post">#CURRENT_ITEM_POST_TEXT#</span>'
,p_before_element=>'<div class="t-Form-inputContainer"><div class="t-Form-itemWrapper">#ITEM_PRE_TEXT#'
,p_after_element=>'#ITEM_POST_TEXT##HELP_TEMPLATE#</div>#INLINE_HELP_TEMPLATE##ERROR_TEMPLATE#</div>'
,p_help_link=>'<button class="t-Form-helpButton js-itemHelp" data-itemhelp="#CURRENT_ITEM_ID#" title="#CURRENT_ITEM_HELP_LABEL#" aria-label="#CURRENT_ITEM_HELP_LABEL#" tabindex="-1" type="button"><span class="a-Icon icon-help" aria-hidden="true"></span></button>'
,p_inline_help_text=>'<span class="t-Form-inlineHelp">#CURRENT_ITEM_INLINE_HELP_TEXT#</span>'
,p_error_template=>'<span class="t-Form-error">#ERROR_MESSAGE#</span>'
,p_theme_id=>42
,p_theme_class_id=>3
,p_reference_id=>1607675164727151865
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/label/required
begin
wwv_flow_api.create_field_template(
 p_id=>wwv_flow_api.id(9820138681688087)
,p_template_name=>'Required'
,p_internal_name=>'REQUIRED'
,p_template_body1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Form-labelContainer col col-#LABEL_COLUMN_SPAN_NUMBER#">',
'  <label for="#CURRENT_ITEM_NAME#" id="#LABEL_ID#" class="t-Form-label">'))
,p_template_body2=>wwv_flow_string.join(wwv_flow_t_varchar2(
' <span class="u-VisuallyHidden">(#VALUE_REQUIRED#)</span></label>',
'</div>'))
,p_before_item=>'<div class="t-Form-fieldContainer is-required rel-col #ITEM_CSS_CLASSES#" id="#CURRENT_ITEM_CONTAINER_ID#">'
,p_after_item=>'</div>'
,p_item_pre_text=>'<span class="t-Form-itemText t-Form-itemText--pre">#CURRENT_ITEM_PRE_TEXT#</span>'
,p_item_post_text=>'<span class="t-Form-itemText t-Form-itemText--post">#CURRENT_ITEM_POST_TEXT#</span>'
,p_before_element=>'<div class="t-Form-inputContainer col col-#ITEM_COLUMN_SPAN_NUMBER#"><div class="t-Form-itemWrapper">#ITEM_PRE_TEXT#'
,p_after_element=>'#ITEM_POST_TEXT##HELP_TEMPLATE#</div>#INLINE_HELP_TEMPLATE##ERROR_TEMPLATE#</div>'
,p_help_link=>'<button class="t-Form-helpButton js-itemHelp" data-itemhelp="#CURRENT_ITEM_ID#" title="#CURRENT_ITEM_HELP_LABEL#" aria-label="#CURRENT_ITEM_HELP_LABEL#" tabindex="-1" type="button"><span class="a-Icon icon-help" aria-hidden="true"></span></button>'
,p_inline_help_text=>'<span class="t-Form-inlineHelp">#CURRENT_ITEM_INLINE_HELP_TEXT#</span>'
,p_error_template=>'<span class="t-Form-error">#ERROR_MESSAGE#</span>'
,p_theme_id=>42
,p_theme_class_id=>4
,p_reference_id=>2525313812251712801
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/label/required_above
begin
wwv_flow_api.create_field_template(
 p_id=>wwv_flow_api.id(9820264563688088)
,p_template_name=>'Required - Above'
,p_internal_name=>'REQUIRED_ABOVE'
,p_template_body1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Form-labelContainer">',
'  <label for="#CURRENT_ITEM_NAME#" id="#LABEL_ID#" class="t-Form-label">'))
,p_template_body2=>wwv_flow_string.join(wwv_flow_t_varchar2(
' <span class="u-VisuallyHidden">(#VALUE_REQUIRED#)</span></label> #HELP_TEMPLATE#',
'</div>'))
,p_before_item=>'<div class="t-Form-fieldContainer t-Form-fieldContainer--stacked is-required #ITEM_CSS_CLASSES#" id="#CURRENT_ITEM_CONTAINER_ID#">'
,p_after_item=>'</div>'
,p_item_pre_text=>'<span class="t-Form-itemText t-Form-itemText--pre">#CURRENT_ITEM_PRE_TEXT#</span>'
,p_item_post_text=>'<span class="t-Form-itemText t-Form-itemText--post">#CURRENT_ITEM_POST_TEXT#</span>'
,p_before_element=>'<div class="t-Form-inputContainer"><div class="t-Form-itemWrapper">#ITEM_PRE_TEXT#'
,p_after_element=>'#ITEM_POST_TEXT#</div>#INLINE_HELP_TEMPLATE##ERROR_TEMPLATE#</div>'
,p_help_link=>'<button class="t-Form-helpButton js-itemHelp" data-itemhelp="#CURRENT_ITEM_ID#" title="#CURRENT_ITEM_HELP_LABEL#" aria-label="#CURRENT_ITEM_HELP_LABEL#" tabindex="-1" type="button"><span class="a-Icon icon-help" aria-hidden="true"></span></button>'
,p_inline_help_text=>'<span class="t-Form-inlineHelp">#CURRENT_ITEM_INLINE_HELP_TEXT#</span>'
,p_error_template=>'<span class="t-Form-error">#ERROR_MESSAGE#</span>'
,p_theme_id=>42
,p_theme_class_id=>4
,p_reference_id=>3030115129444970113
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/label/required_floating
begin
wwv_flow_api.create_field_template(
 p_id=>wwv_flow_api.id(9820300113688088)
,p_template_name=>'Required - Floating'
,p_internal_name=>'REQUIRED_FLOATING'
,p_template_body1=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-Form-labelContainer">',
'  <label for="#CURRENT_ITEM_NAME#" id="#LABEL_ID#" class="t-Form-label">'))
,p_template_body2=>wwv_flow_string.join(wwv_flow_t_varchar2(
' <span class="u-VisuallyHidden">(#VALUE_REQUIRED#)</span></label>',
'</div>'))
,p_before_item=>'<div class="t-Form-fieldContainer t-Form-fieldContainer--floatingLabel is-required #ITEM_CSS_CLASSES#" id="#CURRENT_ITEM_CONTAINER_ID#">'
,p_after_item=>'</div>'
,p_item_pre_text=>'<span class="t-Form-itemText t-Form-itemText--pre">#CURRENT_ITEM_PRE_TEXT#</span>'
,p_item_post_text=>'<span class="t-Form-itemText t-Form-itemText--post">#CURRENT_ITEM_POST_TEXT#</span>'
,p_before_element=>'<div class="t-Form-inputContainer"><div class="t-Form-itemWrapper">#ITEM_PRE_TEXT#'
,p_after_element=>'#ITEM_POST_TEXT##HELP_TEMPLATE#</div>#INLINE_HELP_TEMPLATE##ERROR_TEMPLATE#</div>'
,p_help_link=>'<button class="t-Form-helpButton js-itemHelp" data-itemhelp="#CURRENT_ITEM_ID#" title="#CURRENT_ITEM_HELP_LABEL#" aria-label="#CURRENT_ITEM_HELP_LABEL#" tabindex="-1" type="button"><span class="a-Icon icon-help" aria-hidden="true"></span></button>'
,p_inline_help_text=>'<span class="t-Form-inlineHelp">#CURRENT_ITEM_INLINE_HELP_TEXT#</span>'
,p_error_template=>'<span class="t-Form-error">#ERROR_MESSAGE#</span>'
,p_theme_id=>42
,p_theme_class_id=>4
,p_reference_id=>1607675344320152883
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/breadcrumb/breadcrumb
begin
wwv_flow_api.create_menu_template(
 p_id=>wwv_flow_api.id(9822555663688101)
,p_name=>'Breadcrumb'
,p_internal_name=>'BREADCRUMB'
,p_before_first=>'<ul class="t-Breadcrumb #COMPONENT_CSS_CLASSES#">'
,p_current_page_option=>'<li class="t-Breadcrumb-item is-active"><h1 class="t-Breadcrumb-label">#NAME#</h1></li>'
,p_non_current_page_option=>'<li class="t-Breadcrumb-item"><a href="#LINK#" class="t-Breadcrumb-label">#NAME#</a></li>'
,p_after_last=>'</ul>'
,p_max_levels=>6
,p_start_with_node=>'PARENT_TO_LEAF'
,p_theme_id=>42
,p_theme_class_id=>1
,p_reference_id=>4070916542570059325
,p_translate_this_template=>'N'
);
end;
/
prompt --application/shared_components/user_interface/templates/popuplov
begin
wwv_flow_api.create_popup_lov_template(
 p_id=>wwv_flow_api.id(9822782620688125)
,p_page_name=>'winlov'
,p_page_title=>'Search Dialog'
,p_page_html_head=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<!DOCTYPE html>',
'<html lang="&BROWSER_LANGUAGE.">',
'<head>',
'<title>#TITLE#</title>',
'#APEX_CSS#',
'#THEME_CSS#',
'#THEME_STYLE_CSS#',
'#FAVICONS#',
'#APEX_JAVASCRIPT#',
'#THEME_JAVASCRIPT#',
'<meta name="viewport" content="width=device-width,initial-scale=1.0" />',
'</head>'))
,p_page_body_attr=>'onload="first_field()" class="t-Page t-Page--popupLOV"'
,p_before_field_text=>'<div class="t-PopupLOV-actions t-Form--large">'
,p_filter_width=>'20'
,p_filter_max_width=>'100'
,p_filter_text_attr=>'class="apex-item-text"'
,p_find_button_text=>'Search'
,p_find_button_attr=>'class="t-Button t-Button--hot t-Button--padLeft"'
,p_close_button_text=>'Close'
,p_close_button_attr=>'class="t-Button u-pullRight"'
,p_next_button_text=>'Next &gt;'
,p_next_button_attr=>'class="t-Button t-PopupLOV-button"'
,p_prev_button_text=>'&lt; Previous'
,p_prev_button_attr=>'class="t-Button t-PopupLOV-button"'
,p_after_field_text=>'</div>'
,p_scrollbars=>'1'
,p_resizable=>'1'
,p_width=>'380'
,p_result_row_x_of_y=>'<div class="t-PopupLOV-pagination">Row(s) #FIRST_ROW# - #LAST_ROW#</div>'
,p_result_rows_per_pg=>100
,p_before_result_set=>'<div class="t-PopupLOV-links">'
,p_theme_id=>42
,p_theme_class_id=>1
,p_reference_id=>2885398517835871876
,p_translate_this_template=>'N'
,p_after_result_set=>'</div>'
);
end;
/
prompt --application/shared_components/user_interface/templates/calendar/calendar
begin
wwv_flow_api.create_calendar_template(
 p_id=>wwv_flow_api.id(9822672172688110)
,p_cal_template_name=>'Calendar'
,p_internal_name=>'CALENDAR'
,p_day_of_week_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<th id="#DY#" scope="col" class="t-ClassicCalendar-dayColumn">',
'  <span class="visible-md visible-lg">#IDAY#</span>',
'  <span class="hidden-md hidden-lg">#IDY#</span>',
'</th>'))
,p_month_title_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-ClassicCalendar">',
'<h1 class="t-ClassicCalendar-title">#IMONTH# #YYYY#</h1>'))
,p_month_open_format=>'<table class="t-ClassicCalendar-calendar" cellpadding="0" cellspacing="0" border="0" aria-label="#IMONTH# #YYYY#">'
,p_month_close_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</table>',
'</div>',
''))
,p_day_title_format=>'<span class="t-ClassicCalendar-date">#DD#</span>'
,p_day_open_format=>'<td class="t-ClassicCalendar-day" headers="#DY#">#TITLE_FORMAT#<div class="t-ClassicCalendar-dayEvents">#DATA#</div>'
,p_day_close_format=>'</td>'
,p_today_open_format=>'<td class="t-ClassicCalendar-day is-today" headers="#DY#">#TITLE_FORMAT#<div class="t-ClassicCalendar-dayEvents">#DATA#</div>'
,p_weekend_title_format=>'<span class="t-ClassicCalendar-date">#DD#</span>'
,p_weekend_open_format=>'<td class="t-ClassicCalendar-day is-weekend" headers="#DY#">#TITLE_FORMAT#<div class="t-ClassicCalendar-dayEvents">#DATA#</div>'
,p_weekend_close_format=>'</td>'
,p_nonday_title_format=>'<span class="t-ClassicCalendar-date">#DD#</span>'
,p_nonday_open_format=>'<td class="t-ClassicCalendar-day is-inactive" headers="#DY#">'
,p_nonday_close_format=>'</td>'
,p_week_open_format=>'<tr>'
,p_week_close_format=>'</tr> '
,p_daily_title_format=>'<table cellspacing="0" cellpadding="0" border="0" summary="" class="t1DayCalendarHolder"> <tr> <td class="t1MonthTitle">#IMONTH# #DD#, #YYYY#</td> </tr> <tr> <td>'
,p_daily_open_format=>'<tr>'
,p_daily_close_format=>'</tr>'
,p_weekly_title_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-ClassicCalendar t-ClassicCalendar--weekly">',
'<h1 class="t-ClassicCalendar-title">#WTITLE#</h1>'))
,p_weekly_day_of_week_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<th scope="col" class="t-ClassicCalendar-dayColumn" id="#DY#">',
'  <span class="visible-md visible-lg">#DD# #IDAY#</span>',
'  <span class="hidden-md hidden-lg">#DD# #IDY#</span>',
'</th>'))
,p_weekly_month_open_format=>'<table border="0" cellpadding="0" cellspacing="0" aria-label="#CALENDAR_TITLE# #START_DL# - #END_DL#" class="t-ClassicCalendar-calendar">'
,p_weekly_month_close_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</table>',
'</div>'))
,p_weekly_day_open_format=>'<td class="t-ClassicCalendar-day" headers="#DY#"><div class="t-ClassicCalendar-dayEvents">'
,p_weekly_day_close_format=>'</div></td>'
,p_weekly_today_open_format=>'<td class="t-ClassicCalendar-day is-today" headers="#DY#"><div class="t-ClassicCalendar-dayEvents">'
,p_weekly_weekend_open_format=>'<td class="t-ClassicCalendar-day is-weekend" headers="#DY#"><div class="t-ClassicCalendar-dayEvents">'
,p_weekly_weekend_close_format=>'</div></td>'
,p_weekly_time_open_format=>'<th scope="row" class="t-ClassicCalendar-day t-ClassicCalendar-timeCol">'
,p_weekly_time_close_format=>'</th>'
,p_weekly_time_title_format=>'#TIME#'
,p_weekly_hour_open_format=>'<tr>'
,p_weekly_hour_close_format=>'</tr>'
,p_daily_day_of_week_format=>'<th scope="col" id="#DY#" class="t-ClassicCalendar-dayColumn">#IDAY#</th>'
,p_daily_month_title_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-ClassicCalendar t-ClassicCalendar--daily">',
'<h1 class="t-ClassicCalendar-title">#IMONTH# #DD#, #YYYY#</h1>'))
,p_daily_month_open_format=>'<table border="0" cellpadding="0" cellspacing="0" aria-label="#CALENDAR_TITLE# #START_DL#" class="t-ClassicCalendar-calendar">'
,p_daily_month_close_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</table>',
'</div>'))
,p_daily_day_open_format=>'<td class="t-ClassicCalendar-day" headers="#DY#"><div class="t-ClassicCalendar-dayEvents">'
,p_daily_day_close_format=>'</div></td>'
,p_daily_today_open_format=>'<td class="t-ClassicCalendar-day is-today" headers="#DY#"><div class="t-ClassicCalendar-dayEvents">'
,p_daily_time_open_format=>'<th scope="row" class="t-ClassicCalendar-day t-ClassicCalendar-timeCol" id="#TIME#">'
,p_daily_time_close_format=>'</th>'
,p_daily_time_title_format=>'#TIME#'
,p_daily_hour_open_format=>'<tr>'
,p_daily_hour_close_format=>'</tr>'
,p_cust_month_title_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-ClassicCalendar">',
'<h1 class="t-ClassicCalendar-title">#IMONTH# #YYYY#</h1>'))
,p_cust_day_of_week_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<th id="#DY#" scope="col" class="t-ClassicCalendar-dayColumn">',
'  <span class="visible-md visible-lg">#IDAY#</span>',
'  <span class="hidden-md hidden-lg">#IDY#</span>',
'</th>'))
,p_cust_month_open_format=>'<table class="t-ClassicCalendar-calendar" cellpadding="0" cellspacing="0" border="0" aria-label="#IMONTH# #YYYY#">'
,p_cust_month_close_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</table>',
'</div>'))
,p_cust_week_open_format=>'<tr>'
,p_cust_week_close_format=>'</tr> '
,p_cust_day_title_format=>'<span class="t-ClassicCalendar-date">#DD#</span>'
,p_cust_day_open_format=>'<td class="t-ClassicCalendar-day" headers="#DY#">'
,p_cust_day_close_format=>'</td>'
,p_cust_today_open_format=>'<td class="t-ClassicCalendar-day is-today" headers="#DY#">'
,p_cust_nonday_title_format=>'<span class="t-ClassicCalendar-date">#DD#</span>'
,p_cust_nonday_open_format=>'<td class="t-ClassicCalendar-day is-inactive" headers="#DY#">'
,p_cust_nonday_close_format=>'</td>'
,p_cust_weekend_title_format=>'<span class="t-ClassicCalendar-date">#DD#</span>'
,p_cust_weekend_open_format=>'<td class="t-ClassicCalendar-day is-weekend" headers="#DY#">'
,p_cust_weekend_close_format=>'</td>'
,p_cust_hour_open_format=>'<tr>'
,p_cust_hour_close_format=>'</tr>'
,p_cust_time_title_format=>'#TIME#'
,p_cust_time_open_format=>'<th scope="row" class="t-ClassicCalendar-day t-ClassicCalendar-timeCol">'
,p_cust_time_close_format=>'</th>'
,p_cust_wk_month_title_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-ClassicCalendar">',
'<h1 class="t-ClassicCalendar-title">#WTITLE#</h1>'))
,p_cust_wk_day_of_week_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<th scope="col" class="t-ClassicCalendar-dayColumn" id="#DY#">',
'  <span class="visible-md visible-lg">#DD# #IDAY#</span>',
'  <span class="hidden-md hidden-lg">#DD# #IDY#</span>',
'</th>'))
,p_cust_wk_month_open_format=>'<table border="0" cellpadding="0" cellspacing="0" summary="#CALENDAR_TITLE# #START_DL# - #END_DL#" class="t-ClassicCalendar-calendar">'
,p_cust_wk_month_close_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'</table>',
'</div>'))
,p_cust_wk_week_open_format=>'<tr>'
,p_cust_wk_week_close_format=>'</tr> '
,p_cust_wk_day_open_format=>'<td class="t-ClassicCalendar-day" headers="#DY#"><div class="t-ClassicCalendar-dayEvents">'
,p_cust_wk_day_close_format=>'</div></td>'
,p_cust_wk_today_open_format=>'<td class="t-ClassicCalendar-day is-today" headers="#DY#"><div class="t-ClassicCalendar-dayEvents">'
,p_cust_wk_weekend_open_format=>'<td class="t-ClassicCalendar-day" headers="#DY#">'
,p_cust_wk_weekend_close_format=>'</td>'
,p_agenda_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<div class="t-ClassicCalendar t-ClassicCalendar--list">',
'  <div class="t-ClassicCalendar-title">#IMONTH# #YYYY#</div>',
'  <ul class="t-ClassicCalendar-list">',
'    #DAYS#',
'  </ul>',
'</div>'))
,p_agenda_past_day_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'  <li class="t-ClassicCalendar-listTitle is-past">',
'    <span class="t-ClassicCalendar-listDayTitle">#IDAY#</span><span class="t-ClassicCalendar-listDayDate">#IMONTH# #DD#</span>',
'  </li>'))
,p_agenda_today_day_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'  <li class="t-ClassicCalendar-listTitle is-today">',
'    <span class="t-ClassicCalendar-listDayTitle">#IDAY#</span><span class="t-ClassicCalendar-listDayDate">#IMONTH# #DD#</span>',
'  </li>'))
,p_agenda_future_day_format=>wwv_flow_string.join(wwv_flow_t_varchar2(
'  <li class="t-ClassicCalendar-listTitle is-future">',
'    <span class="t-ClassicCalendar-listDayTitle">#IDAY#</span><span class="t-ClassicCalendar-listDayDate">#IMONTH# #DD#</span>',
'  </li>'))
,p_agenda_past_entry_format=>'  <li class="t-ClassicCalendar-listEvent is-past">#DATA#</li>'
,p_agenda_today_entry_format=>'  <li class="t-ClassicCalendar-listEvent is-today">#DATA#</li>'
,p_agenda_future_entry_format=>'  <li class="t-ClassicCalendar-listEvent is-future">#DATA#</li>'
,p_month_data_format=>'#DAYS#'
,p_month_data_entry_format=>'<span class="t-ClassicCalendar-event">#DATA#</span>'
,p_theme_id=>42
,p_theme_class_id=>1
,p_reference_id=>4070916747979059326
);
end;
/
prompt --application/shared_components/user_interface/themes
begin
wwv_flow_api.create_theme(
 p_id=>wwv_flow_api.id(9823968670688153)
,p_theme_id=>42
,p_theme_name=>'Universal Theme'
,p_theme_internal_name=>'UNIVERSAL_THEME'
,p_ui_type_name=>'DESKTOP'
,p_navigation_type=>'L'
,p_nav_bar_type=>'LIST'
,p_reference_id=>4070917134413059350
,p_is_locked=>false
,p_default_page_template=>wwv_flow_api.id(9732194808687963)
,p_default_dialog_template=>wwv_flow_api.id(9727847199687960)
,p_error_template=>wwv_flow_api.id(9721413857687955)
,p_printer_friendly_template=>wwv_flow_api.id(9732194808687963)
,p_breadcrumb_display_point=>'REGION_POSITION_01'
,p_sidebar_display_point=>'REGION_POSITION_02'
,p_login_template=>wwv_flow_api.id(9721413857687955)
,p_default_button_template=>wwv_flow_api.id(9821119233688096)
,p_default_region_template=>wwv_flow_api.id(9765042323688020)
,p_default_chart_template=>wwv_flow_api.id(9765042323688020)
,p_default_form_template=>wwv_flow_api.id(9765042323688020)
,p_default_reportr_template=>wwv_flow_api.id(9765042323688020)
,p_default_tabform_template=>wwv_flow_api.id(9765042323688020)
,p_default_wizard_template=>wwv_flow_api.id(9765042323688020)
,p_default_menur_template=>wwv_flow_api.id(9774426068688028)
,p_default_listr_template=>wwv_flow_api.id(9765042323688020)
,p_default_irr_template=>wwv_flow_api.id(9763915989688019)
,p_default_report_template=>wwv_flow_api.id(9790776953688052)
,p_default_label_template=>wwv_flow_api.id(9820028477688087)
,p_default_menu_template=>wwv_flow_api.id(9822555663688101)
,p_default_calendar_template=>wwv_flow_api.id(9822672172688110)
,p_default_list_template=>wwv_flow_api.id(9807187050688071)
,p_default_nav_list_template=>wwv_flow_api.id(9815734538688080)
,p_default_top_nav_list_temp=>wwv_flow_api.id(9815734538688080)
,p_default_side_nav_list_temp=>wwv_flow_api.id(9813182182688077)
,p_default_nav_list_position=>'SIDE'
,p_default_dialogbtnr_template=>wwv_flow_api.id(9740827754687991)
,p_default_dialogr_template=>wwv_flow_api.id(9739874064687990)
,p_default_option_label=>wwv_flow_api.id(9820028477688087)
,p_default_required_label=>wwv_flow_api.id(9820300113688088)
,p_default_page_transition=>'NONE'
,p_default_popup_transition=>'NONE'
,p_default_navbar_list_template=>wwv_flow_api.id(9812990164688077)
,p_file_prefix => nvl(wwv_flow_application_install.get_static_theme_file_prefix(42),'#IMAGE_PREFIX#themes/theme_42/1.3/')
,p_files_version=>62
,p_icon_library=>'FONTAPEX'
,p_javascript_file_urls=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#IMAGE_PREFIX#libraries/apex/#MIN_DIRECTORY#widget.stickyWidget#MIN#.js?v=#APEX_VERSION#',
'#THEME_IMAGES#js/theme42#MIN#.js?v=#APEX_VERSION#'))
,p_css_file_urls=>'#THEME_IMAGES#css/Core#MIN#.css?v=#APEX_VERSION#'
);
end;
/
prompt --application/shared_components/user_interface/theme_style
begin
wwv_flow_api.create_theme_style(
 p_id=>wwv_flow_api.id(9822916859688127)
,p_theme_id=>42
,p_name=>'Vista'
,p_css_file_urls=>'#THEME_IMAGES#css/Vista#MIN#.css?v=#APEX_VERSION#'
,p_is_current=>false
,p_is_public=>true
,p_is_accessible=>false
,p_theme_roller_read_only=>true
,p_reference_id=>4007676303523989775
);
wwv_flow_api.create_theme_style(
 p_id=>wwv_flow_api.id(9823137262688127)
,p_theme_id=>42
,p_name=>'Vita'
,p_is_current=>false
,p_is_public=>true
,p_is_accessible=>true
,p_theme_roller_input_file_urls=>'#THEME_IMAGES#less/theme/Vita.less'
,p_theme_roller_output_file_url=>'#THEME_IMAGES#css/Vita#MIN#.css?v=#APEX_VERSION#'
,p_theme_roller_read_only=>true
,p_reference_id=>2719875314571594493
);
wwv_flow_api.create_theme_style(
 p_id=>wwv_flow_api.id(9823304776688127)
,p_theme_id=>42
,p_name=>'Vita - Dark'
,p_is_current=>false
,p_is_public=>true
,p_is_accessible=>false
,p_theme_roller_input_file_urls=>'#THEME_IMAGES#less/theme/Vita-Dark.less'
,p_theme_roller_output_file_url=>'#THEME_IMAGES#css/Vita-Dark#MIN#.css?v=#APEX_VERSION#'
,p_theme_roller_read_only=>true
,p_reference_id=>3543348412015319650
);
wwv_flow_api.create_theme_style(
 p_id=>wwv_flow_api.id(9823525392688127)
,p_theme_id=>42
,p_name=>'Vita - Red'
,p_is_current=>false
,p_is_public=>true
,p_is_accessible=>false
,p_theme_roller_input_file_urls=>'#THEME_IMAGES#less/theme/Vita-Red.less'
,p_theme_roller_output_file_url=>'#THEME_IMAGES#css/Vita-Red#MIN#.css?v=#APEX_VERSION#'
,p_theme_roller_read_only=>true
,p_reference_id=>1938457712423918173
);
wwv_flow_api.create_theme_style(
 p_id=>wwv_flow_api.id(9823761877688127)
,p_theme_id=>42
,p_name=>'Vita - Slate'
,p_is_current=>true
,p_is_public=>true
,p_is_accessible=>false
,p_theme_roller_input_file_urls=>'#THEME_IMAGES#less/theme/Vita-Slate.less'
,p_theme_roller_output_file_url=>'#THEME_IMAGES#css/Vita-Slate#MIN#.css?v=#APEX_VERSION#'
,p_theme_roller_read_only=>true
,p_reference_id=>3291983347983194966
);
end;
/
prompt --application/shared_components/user_interface/theme_files
begin
null;
end;
/
prompt --application/shared_components/user_interface/theme_display_points
begin
null;
end;
/
prompt --application/shared_components/user_interface/template_opt_groups
begin
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9736714596687984)
,p_theme_id=>42
,p_name=>'ALERT_TYPE'
,p_display_name=>'Alert Type'
,p_display_sequence=>3
,p_template_types=>'REGION'
,p_help_text=>'Sets the type of alert which can be used to determine the icon, icon color, and the background color.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9737968223687989)
,p_theme_id=>42
,p_name=>'ALERT_ICONS'
,p_display_name=>'Alert Icons'
,p_display_sequence=>2
,p_template_types=>'REGION'
,p_help_text=>'Sets how icons are handled for the Alert Region.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9738325116687989)
,p_theme_id=>42
,p_name=>'ALERT_TITLE'
,p_display_name=>'Alert Title'
,p_display_sequence=>40
,p_template_types=>'REGION'
,p_help_text=>'Determines how the title of the alert is displayed.'
,p_null_text=>'Visible - Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9738958844687990)
,p_theme_id=>42
,p_name=>'ALERT_DISPLAY'
,p_display_name=>'Alert Display'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_help_text=>'Sets the layout of the Alert Region.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9741709467687992)
,p_theme_id=>42
,p_name=>'STYLE'
,p_display_name=>'Style'
,p_display_sequence=>40
,p_template_types=>'REGION'
,p_help_text=>'Determines how the region is styled. Use the "Remove Borders" template option to remove the region''s borders and shadows.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9742375281687992)
,p_theme_id=>42
,p_name=>'BODY_PADDING'
,p_display_name=>'Body Padding'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_help_text=>'Sets the Region Body padding for the region.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9744546560687994)
,p_theme_id=>42
,p_name=>'BODY_OVERFLOW'
,p_display_name=>'Body Overflow'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_help_text=>'Determines the scroll behavior when the region contents are larger than their container.'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9744957574687994)
,p_theme_id=>42
,p_name=>'ANIMATION'
,p_display_name=>'Animation'
,p_display_sequence=>10
,p_template_types=>'REGION'
,p_help_text=>'Sets the animation when navigating within the Carousel Region.'
,p_null_text=>'Fade'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9746151420687996)
,p_theme_id=>42
,p_name=>'TIMER'
,p_display_name=>'Timer'
,p_display_sequence=>2
,p_template_types=>'REGION'
,p_help_text=>'Sets the timer for when to automatically navigate to the next region within the Carousel Region.'
,p_null_text=>'No Timer'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9746992832687996)
,p_theme_id=>42
,p_name=>'BODY_HEIGHT'
,p_display_name=>'Body Height'
,p_display_sequence=>10
,p_template_types=>'REGION'
,p_help_text=>'Sets the Region Body height. You can also specify a custom height by modifying the Region''s CSS Classes and using the height helper classes "i-hXXX" where XXX is any increment of 10 from 100 to 800.'
,p_null_text=>'Auto - Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9748113149687997)
,p_theme_id=>42
,p_name=>'ACCENT'
,p_display_name=>'Accent'
,p_display_sequence=>30
,p_template_types=>'REGION'
,p_help_text=>'Set the Region''s accent. This accent corresponds to a Theme-Rollable color and sets the background of the Region''s Header.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9749398276687999)
,p_theme_id=>42
,p_name=>'HEADER'
,p_display_name=>'Header'
,p_display_sequence=>20
,p_template_types=>'REGION'
,p_help_text=>'Determines the display of the Region Header which also contains the Region Title.'
,p_null_text=>'Visible - Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9752345725688002)
,p_theme_id=>42
,p_name=>'COLLAPSIBLE_BUTTON_ICONS'
,p_display_name=>'Collapsible Button Icons'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_help_text=>'Determines which arrows to use to represent the icons for the collapse and expand button.'
,p_null_text=>'Arrows'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9752760481688003)
,p_theme_id=>42
,p_name=>'COLLAPSIBLE_ICON_POSITION'
,p_display_name=>'Collapsible Icon Position'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_help_text=>'Determines the position of the expand and collapse toggle for the region.'
,p_null_text=>'Start'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9754966226688011)
,p_theme_id=>42
,p_name=>'DEFAULT_STATE'
,p_display_name=>'Default State'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_help_text=>'Sets the default state of the region.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9755973583688012)
,p_theme_id=>42
,p_name=>'REGION_TITLE'
,p_display_name=>'Region Title'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_help_text=>'Sets the source of the Title Bar region''s title.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9757188941688012)
,p_theme_id=>42
,p_name=>'BODY_STYLE'
,p_display_name=>'Body Style'
,p_display_sequence=>20
,p_template_types=>'REGION'
,p_help_text=>'Controls the display of the region''s body container.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9758665881688015)
,p_theme_id=>42
,p_name=>'DISPLAY_ICON'
,p_display_name=>'Display Icon'
,p_display_sequence=>50
,p_template_types=>'REGION'
,p_help_text=>'Display the Hero Region icon.'
,p_null_text=>'Yes (Default)'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9759294418688016)
,p_theme_id=>42
,p_name=>'ICON_SHAPE'
,p_display_name=>'Icon Shape'
,p_display_sequence=>60
,p_template_types=>'REGION'
,p_help_text=>'Determines the shape of the icon.'
,p_null_text=>'Rounded Corners'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9761354322688017)
,p_theme_id=>42
,p_name=>'DIALOG_SIZE'
,p_display_name=>'Dialog Size'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9772915564688027)
,p_theme_id=>42
,p_name=>'LAYOUT'
,p_display_name=>'Layout'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9773387695688028)
,p_theme_id=>42
,p_name=>'TAB_STYLE'
,p_display_name=>'Tab Style'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9773926842688028)
,p_theme_id=>42
,p_name=>'TABS_SIZE'
,p_display_name=>'Tabs Size'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9776081830688030)
,p_theme_id=>42
,p_name=>'HIDE_STEPS_FOR'
,p_display_name=>'Hide Steps For'
,p_display_sequence=>1
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9777212990688037)
,p_theme_id=>42
,p_name=>'BADGE_SIZE'
,p_display_name=>'Badge Size'
,p_display_sequence=>10
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9778470443688038)
,p_theme_id=>42
,p_name=>'LAYOUT'
,p_display_name=>'Layout'
,p_display_sequence=>30
,p_template_types=>'REPORT'
,p_help_text=>'Determines the layout of Cards in the report.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9780462791688040)
,p_theme_id=>42
,p_name=>'STYLE'
,p_display_name=>'Style'
,p_display_sequence=>10
,p_template_types=>'REPORT'
,p_help_text=>'Determines the overall style for the component.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9781244843688042)
,p_theme_id=>42
,p_name=>'ANIMATION'
,p_display_name=>'Animation'
,p_display_sequence=>70
,p_template_types=>'REPORT'
,p_help_text=>'Sets the hover and focus animation.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9781895042688042)
,p_theme_id=>42
,p_name=>'ICON_SHAPE'
,p_display_name=>'Icon Shape'
,p_display_sequence=>60
,p_template_types=>'REPORT'
,p_help_text=>'Determines the shape of the icon.'
,p_null_text=>'Circle'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9784006583688045)
,p_theme_id=>42
,p_name=>'BODY_TEXT'
,p_display_name=>'Body Text'
,p_display_sequence=>40
,p_template_types=>'REPORT'
,p_help_text=>'Determines the height of the card body.'
,p_null_text=>'Auto'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9785095805688046)
,p_theme_id=>42
,p_name=>'ICONS'
,p_display_name=>'Icons'
,p_display_sequence=>20
,p_template_types=>'REPORT'
,p_help_text=>'Controls how to handle icons in the report.'
,p_null_text=>'No Icons'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9787068036688049)
,p_theme_id=>42
,p_name=>'COMMENTS_STYLE'
,p_display_name=>'Comments Style'
,p_display_sequence=>10
,p_template_types=>'REPORT'
,p_help_text=>'Determines the style in which comments are displayed.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9790269827688052)
,p_theme_id=>42
,p_name=>'SIZE'
,p_display_name=>'Size'
,p_display_sequence=>35
,p_template_types=>'REPORT'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9791070979688053)
,p_theme_id=>42
,p_name=>'REPORT_BORDER'
,p_display_name=>'Report Border'
,p_display_sequence=>30
,p_template_types=>'REPORT'
,p_help_text=>'Controls the display of the Report''s borders.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9791834752688053)
,p_theme_id=>42
,p_name=>'ALTERNATING_ROWS'
,p_display_name=>'Alternating Rows'
,p_display_sequence=>10
,p_template_types=>'REPORT'
,p_help_text=>'Shades alternate rows in the report with slightly different background colors.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9792831199688054)
,p_theme_id=>42
,p_name=>'ROW_HIGHLIGHTING'
,p_display_name=>'Row Highlighting'
,p_display_sequence=>20
,p_template_types=>'REPORT'
,p_help_text=>'Determines whether you want the row to be highlighted on hover.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9794418510688055)
,p_theme_id=>42
,p_name=>'LABEL_WIDTH'
,p_display_name=>'Label Width'
,p_display_sequence=>10
,p_template_types=>'REPORT'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9797800158688064)
,p_theme_id=>42
,p_name=>'LAYOUT'
,p_display_name=>'Layout'
,p_display_sequence=>30
,p_template_types=>'LIST'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9799694951688065)
,p_theme_id=>42
,p_name=>'BADGE_SIZE'
,p_display_name=>'Badge Size'
,p_display_sequence=>70
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9801042467688067)
,p_theme_id=>42
,p_name=>'STYLE'
,p_display_name=>'Style'
,p_display_sequence=>10
,p_template_types=>'LIST'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9802035137688068)
,p_theme_id=>42
,p_name=>'ANIMATION'
,p_display_name=>'Animation'
,p_display_sequence=>80
,p_template_types=>'LIST'
,p_help_text=>'Sets the hover and focus animation.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9802696520688068)
,p_theme_id=>42
,p_name=>'ICON_SHAPE'
,p_display_name=>'Icon Shape'
,p_display_sequence=>60
,p_template_types=>'LIST'
,p_help_text=>'Determines the shape of the icon.'
,p_null_text=>'Circle'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9805405815688070)
,p_theme_id=>42
,p_name=>'ICONS'
,p_display_name=>'Icons'
,p_display_sequence=>20
,p_template_types=>'LIST'
,p_null_text=>'No Icons'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9806089747688071)
,p_theme_id=>42
,p_name=>'BODY_TEXT'
,p_display_name=>'Body Text'
,p_display_sequence=>40
,p_template_types=>'LIST'
,p_help_text=>'Determines the height of the card body.'
,p_null_text=>'Auto'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9807457363688072)
,p_theme_id=>42
,p_name=>'DISPLAY_ICONS'
,p_display_name=>'Display Icons'
,p_display_sequence=>30
,p_template_types=>'LIST'
,p_null_text=>'No Icons'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9810649159688075)
,p_theme_id=>42
,p_name=>'SIZE'
,p_display_name=>'Size'
,p_display_sequence=>1
,p_template_types=>'LIST'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9817056740688081)
,p_theme_id=>42
,p_name=>'DESKTOP'
,p_display_name=>'Desktop'
,p_display_sequence=>90
,p_template_types=>'LIST'
,p_help_text=>'Determines the display for a desktop-sized screen'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9817843155688082)
,p_theme_id=>42
,p_name=>'MOBILE'
,p_display_name=>'Mobile'
,p_display_sequence=>100
,p_template_types=>'LIST'
,p_help_text=>'Determines the display for a mobile-sized screen'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9818601323688083)
,p_theme_id=>42
,p_name=>'LABEL_DISPLAY'
,p_display_name=>'Label Display'
,p_display_sequence=>50
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9820691839688095)
,p_theme_id=>42
,p_name=>'ICON_HOVER_ANIMATION'
,p_display_name=>'Icon Hover Animation'
,p_display_sequence=>55
,p_template_types=>'BUTTON'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9821466696688096)
,p_theme_id=>42
,p_name=>'ICON_POSITION'
,p_display_name=>'Icon Position'
,p_display_sequence=>50
,p_template_types=>'BUTTON'
,p_help_text=>'Sets the position of the icon relative to the label.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9824141954688169)
,p_theme_id=>42
,p_name=>'TYPE'
,p_display_name=>'Type'
,p_display_sequence=>20
,p_template_types=>'BUTTON'
,p_null_text=>'Normal'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9824530443688170)
,p_theme_id=>42
,p_name=>'WIDTH'
,p_display_name=>'Width'
,p_display_sequence=>60
,p_template_types=>'BUTTON'
,p_help_text=>'Sets the width of the button.'
,p_null_text=>'Auto - Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9825393341688171)
,p_theme_id=>42
,p_name=>'STYLE'
,p_display_name=>'Style'
,p_display_sequence=>30
,p_template_types=>'BUTTON'
,p_help_text=>'Sets the style of the button. Use the "Simple" option for secondary actions or sets of buttons. Use the "Remove UI Decoration" option to make the button appear as text.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9825760804688172)
,p_theme_id=>42
,p_name=>'SIZE'
,p_display_name=>'Size'
,p_display_sequence=>10
,p_template_types=>'BUTTON'
,p_help_text=>'Sets the size of the button.'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9826159905688172)
,p_theme_id=>42
,p_name=>'SPACING_LEFT'
,p_display_name=>'Spacing Left'
,p_display_sequence=>70
,p_template_types=>'BUTTON'
,p_help_text=>'Controls the spacing to the left of the button.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9827306136688173)
,p_theme_id=>42
,p_name=>'SPACING_RIGHT'
,p_display_name=>'Spacing Right'
,p_display_sequence=>80
,p_template_types=>'BUTTON'
,p_help_text=>'Controls the spacing to the right of the button.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9827970714688173)
,p_theme_id=>42
,p_name=>'BUTTON_SET'
,p_display_name=>'Button Set'
,p_display_sequence=>40
,p_template_types=>'BUTTON'
,p_help_text=>'Enables you to group many buttons together into a pill. You can use this option to specify where the button is within this set. Set the option to Default if this button is not part of a button set.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9828709506688174)
,p_theme_id=>42
,p_name=>'LABEL_ALIGNMENT'
,p_display_name=>'Label Alignment'
,p_display_sequence=>130
,p_template_types=>'REGION'
,p_help_text=>'Set the label text alignment for items within this region.'
,p_null_text=>'Right'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9829158305688174)
,p_theme_id=>42
,p_name=>'ITEM_SIZE'
,p_display_name=>'Item Size'
,p_display_sequence=>110
,p_template_types=>'REGION'
,p_help_text=>'Sets the size of the form items within this region.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9829723762688176)
,p_theme_id=>42
,p_name=>'ITEM_PADDING'
,p_display_name=>'Item Padding'
,p_display_sequence=>100
,p_template_types=>'REGION'
,p_help_text=>'Sets the padding around items within this region.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9830364893688176)
,p_theme_id=>42
,p_name=>'LABEL_POSITION'
,p_display_name=>'Label Position'
,p_display_sequence=>140
,p_template_types=>'REGION'
,p_help_text=>'Sets the position of the label relative to the form item.'
,p_null_text=>'Inline - Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9830779259688177)
,p_theme_id=>42
,p_name=>'ITEM_WIDTH'
,p_display_name=>'Item Width'
,p_display_sequence=>120
,p_template_types=>'REGION'
,p_help_text=>'Sets the width of the form items within this region.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9831175250688177)
,p_theme_id=>42
,p_name=>'ITEM_PRE_TEXT'
,p_display_name=>'Item Pre Text'
,p_display_sequence=>20
,p_template_types=>'FIELD'
,p_help_text=>'Adjust the display of the Item Pre Text'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9831512153688177)
,p_theme_id=>42
,p_name=>'ITEM_POST_TEXT'
,p_display_name=>'Item Post Text'
,p_display_sequence=>30
,p_template_types=>'FIELD'
,p_help_text=>'Adjust the display of the Item Post Text'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9831954394688177)
,p_theme_id=>42
,p_name=>'REGION_TOP_MARGIN'
,p_display_name=>'Top Margin'
,p_display_sequence=>200
,p_template_types=>'REGION'
,p_help_text=>'Set the top margin for this region.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9832946681688178)
,p_theme_id=>42
,p_name=>'REGION_BOTTOM_MARGIN'
,p_display_name=>'Bottom Margin'
,p_display_sequence=>210
,p_template_types=>'REGION'
,p_help_text=>'Set the bottom margin for this region.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9833957878688179)
,p_theme_id=>42
,p_name=>'REGION_RIGHT_MARGIN'
,p_display_name=>'Right Margin'
,p_display_sequence=>230
,p_template_types=>'REGION'
,p_help_text=>'Set the right margin for this region.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9834905706688180)
,p_theme_id=>42
,p_name=>'REGION_LEFT_MARGIN'
,p_display_name=>'Left Margin'
,p_display_sequence=>220
,p_template_types=>'REGION'
,p_help_text=>'Set the left margin for this region.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9835973671688181)
,p_theme_id=>42
,p_name=>'PAGINATION_DISPLAY'
,p_display_name=>'Pagination Display'
,p_display_sequence=>10
,p_template_types=>'REPORT'
,p_help_text=>'Controls the display of pagination for this region.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9836597146688181)
,p_theme_id=>42
,p_name=>'SPACING_TOP'
,p_display_name=>'Spacing Top'
,p_display_sequence=>90
,p_template_types=>'BUTTON'
,p_help_text=>'Controls the spacing to the top of the button.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9837176826688181)
,p_theme_id=>42
,p_name=>'SPACING_BOTTOM'
,p_display_name=>'Spacing Bottom'
,p_display_sequence=>100
,p_template_types=>'BUTTON'
,p_help_text=>'Controls the spacing to the bottom of the button.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9837978206688182)
,p_theme_id=>42
,p_name=>'RADIO_GROUP_DISPLAY'
,p_display_name=>'Item Group Display'
,p_display_sequence=>300
,p_template_types=>'FIELD'
,p_help_text=>'Determines the display style for radio and check box items.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9838309887688183)
,p_theme_id=>42
,p_name=>'SIZE'
,p_display_name=>'Size'
,p_display_sequence=>10
,p_template_types=>'FIELD'
,p_null_text=>'Default'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9839140797688183)
,p_theme_id=>42
,p_name=>'BOTTOM_MARGIN'
,p_display_name=>'Bottom Margin'
,p_display_sequence=>220
,p_template_types=>'FIELD'
,p_help_text=>'Set the bottom margin for this field.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9840104506688184)
,p_theme_id=>42
,p_name=>'LEFT_MARGIN'
,p_display_name=>'Left Margin'
,p_display_sequence=>220
,p_template_types=>'FIELD'
,p_help_text=>'Set the left margin for this field.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9841181981688185)
,p_theme_id=>42
,p_name=>'RIGHT_MARGIN'
,p_display_name=>'Right Margin'
,p_display_sequence=>230
,p_template_types=>'FIELD'
,p_help_text=>'Set the right margin for this field.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
wwv_flow_api.create_template_opt_group(
 p_id=>wwv_flow_api.id(9842104263688186)
,p_theme_id=>42
,p_name=>'TOP_MARGIN'
,p_display_name=>'Top Margin'
,p_display_sequence=>200
,p_template_types=>'FIELD'
,p_help_text=>'Set the top margin for this field.'
,p_null_text=>'Default'
,p_is_advanced=>'Y'
);
end;
/
prompt --application/shared_components/user_interface/template_options
begin
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9718256143687950)
,p_theme_id=>42
,p_name=>'STICKY_HEADER_ON_MOBILE'
,p_display_name=>'Sticky Header on Mobile'
,p_display_sequence=>100
,p_page_template_id=>wwv_flow_api.id(9715583223687903)
,p_css_classes=>'js-pageStickyMobileHeader'
,p_template_types=>'PAGE'
,p_help_text=>'This will position the contents of the Breadcrumb Bar region position so it sticks to the top of the screen for small screens.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9721307134687955)
,p_theme_id=>42
,p_name=>'STICKY_HEADER_ON_MOBILE'
,p_display_name=>'Sticky Header on Mobile'
,p_display_sequence=>100
,p_page_template_id=>wwv_flow_api.id(9718391330687953)
,p_css_classes=>'js-pageStickyMobileHeader'
,p_template_types=>'PAGE'
,p_help_text=>'This will position the contents of the Breadcrumb Bar region position so it sticks to the top of the screen for small screens.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9725235788687959)
,p_theme_id=>42
,p_name=>'STICKY_HEADER_ON_MOBILE'
,p_display_name=>'Sticky Header on Mobile'
,p_display_sequence=>100
,p_page_template_id=>wwv_flow_api.id(9722224555687956)
,p_css_classes=>'js-pageStickyMobileHeader'
,p_template_types=>'PAGE'
,p_help_text=>'This will position the contents of the Breadcrumb Bar region position so it sticks to the top of the screen for small screens.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9727726665687960)
,p_theme_id=>42
,p_name=>'STICKY_HEADER_ON_MOBILE'
,p_display_name=>'Sticky Header on Mobile'
,p_display_sequence=>100
,p_page_template_id=>wwv_flow_api.id(9725334349687959)
,p_css_classes=>'js-pageStickyMobileHeader'
,p_template_types=>'PAGE'
,p_help_text=>'This will position the contents of the Breadcrumb Bar region position so it sticks to the top of the screen for small screens.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9729025561687961)
,p_theme_id=>42
,p_name=>'REMOVE_BODY_PADDING'
,p_display_name=>'Remove Body Padding'
,p_display_sequence=>20
,p_page_template_id=>wwv_flow_api.id(9727847199687960)
,p_css_classes=>'t-Dialog--noPadding'
,p_template_types=>'PAGE'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9729245085687961)
,p_theme_id=>42
,p_name=>'STRETCH_TO_FIT_WINDOW'
,p_display_name=>'Stretch to Fit Window'
,p_display_sequence=>1
,p_page_template_id=>wwv_flow_api.id(9727847199687960)
,p_css_classes=>'ui-dialog--stretch'
,p_template_types=>'PAGE'
,p_help_text=>'Stretch the dialog to fit the browser window.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9732092542687963)
,p_theme_id=>42
,p_name=>'STICKY_HEADER_ON_MOBILE'
,p_display_name=>'Sticky Header on Mobile'
,p_display_sequence=>100
,p_page_template_id=>wwv_flow_api.id(9729332661687961)
,p_css_classes=>'js-pageStickyMobileHeader'
,p_template_types=>'PAGE'
,p_help_text=>'This will position the contents of the Breadcrumb Bar region position so it sticks to the top of the screen for small screens.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9734571584687964)
,p_theme_id=>42
,p_name=>'STICKY_HEADER_ON_MOBILE'
,p_display_name=>'Sticky Header on Mobile'
,p_display_sequence=>100
,p_page_template_id=>wwv_flow_api.id(9732194808687963)
,p_css_classes=>'js-pageStickyMobileHeader'
,p_template_types=>'PAGE'
,p_help_text=>'This will position the contents of the Breadcrumb Bar region position so it sticks to the top of the screen for small screens.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9735806663687971)
,p_theme_id=>42
,p_name=>'REMOVE_BODY_PADDING'
,p_display_name=>'Remove Body Padding'
,p_display_sequence=>20
,p_page_template_id=>wwv_flow_api.id(9734610063687964)
,p_css_classes=>'t-Dialog--noPadding'
,p_template_types=>'PAGE'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9736046590687971)
,p_theme_id=>42
,p_name=>'STRETCH_TO_FIT_WINDOW'
,p_display_name=>'Stretch to Fit Window'
,p_display_sequence=>10
,p_page_template_id=>wwv_flow_api.id(9734610063687964)
,p_css_classes=>'ui-dialog--stretch'
,p_template_types=>'PAGE'
,p_help_text=>'Stretch the dialog to fit the browser window.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9736974506687988)
,p_theme_id=>42
,p_name=>'WARNING'
,p_display_name=>'Warning'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--warning'
,p_group_id=>wwv_flow_api.id(9736714596687984)
,p_template_types=>'REGION'
,p_help_text=>'Show a warning alert.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9737162636687988)
,p_theme_id=>42
,p_name=>'SUCCESS'
,p_display_name=>'Success'
,p_display_sequence=>40
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--success'
,p_group_id=>wwv_flow_api.id(9736714596687984)
,p_template_types=>'REGION'
,p_help_text=>'Show success alert.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9737358444687988)
,p_theme_id=>42
,p_name=>'DANGER'
,p_display_name=>'Danger'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--danger'
,p_group_id=>wwv_flow_api.id(9736714596687984)
,p_template_types=>'REGION'
,p_help_text=>'Show an error or danger alert.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9737578488687989)
,p_theme_id=>42
,p_name=>'COLOREDBACKGROUND'
,p_display_name=>'Highlight Background'
,p_display_sequence=>1
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--colorBG'
,p_template_types=>'REGION'
,p_help_text=>'Set alert background color to that of the alert type (warning, success, etc.)'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9737766293687989)
,p_theme_id=>42
,p_name=>'INFORMATION'
,p_display_name=>'Information'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--info'
,p_group_id=>wwv_flow_api.id(9736714596687984)
,p_template_types=>'REGION'
,p_help_text=>'Show informational alert.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9738185608687989)
,p_theme_id=>42
,p_name=>'USEDEFAULTICONS'
,p_display_name=>'Show Default Icons'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--defaultIcons'
,p_group_id=>wwv_flow_api.id(9737968223687989)
,p_template_types=>'REGION'
,p_help_text=>'Uses default icons for alert types.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9738509354687989)
,p_theme_id=>42
,p_name=>'HIDDENHEADERNOAT'
,p_display_name=>'Hidden'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--removeHeading'
,p_group_id=>wwv_flow_api.id(9738325116687989)
,p_template_types=>'REGION'
,p_help_text=>'Hides the Alert Title from being displayed.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9738759976687990)
,p_theme_id=>42
,p_name=>'HIDDENHEADER'
,p_display_name=>'Hidden but Accessible'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--accessibleHeading'
,p_group_id=>wwv_flow_api.id(9738325116687989)
,p_template_types=>'REGION'
,p_help_text=>'Visually hides the alert title, but assistive technologies can still read it.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9739128235687990)
,p_theme_id=>42
,p_name=>'WIZARD'
,p_display_name=>'Wizard'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--wizard'
,p_group_id=>wwv_flow_api.id(9738958844687990)
,p_template_types=>'REGION'
,p_help_text=>'Show the alert in a wizard style region.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9739365286687990)
,p_theme_id=>42
,p_name=>'HORIZONTAL'
,p_display_name=>'Horizontal'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--horizontal'
,p_group_id=>wwv_flow_api.id(9738958844687990)
,p_template_types=>'REGION'
,p_help_text=>'Show horizontal alert with buttons to the right.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9739534442687990)
,p_theme_id=>42
,p_name=>'HIDE_ICONS'
,p_display_name=>'Hide Icons'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--noIcon'
,p_group_id=>wwv_flow_api.id(9737968223687989)
,p_template_types=>'REGION'
,p_help_text=>'Hides alert icons'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9739712659687990)
,p_theme_id=>42
,p_name=>'SHOW_CUSTOM_ICONS'
,p_display_name=>'Show Custom Icons'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9736107349687972)
,p_css_classes=>'t-Alert--customIcons'
,p_group_id=>wwv_flow_api.id(9737968223687989)
,p_template_types=>'REGION'
,p_help_text=>'Set custom icons by modifying the Alert Region''s Icon CSS Classes property.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9741986840687992)
,p_theme_id=>42
,p_name=>'REMOVEUIDECORATION'
,p_display_name=>'Remove UI Decoration'
,p_display_sequence=>4
,p_region_template_id=>wwv_flow_api.id(9740827754687991)
,p_css_classes=>'t-ButtonRegion--noUI'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9742110436687992)
,p_theme_id=>42
,p_name=>'BORDERLESS'
,p_display_name=>'Borderless'
,p_display_sequence=>1
,p_region_template_id=>wwv_flow_api.id(9740827754687991)
,p_css_classes=>'t-ButtonRegion--noBorder'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9742532821687992)
,p_theme_id=>42
,p_name=>'SLIMPADDING'
,p_display_name=>'Slim Padding'
,p_display_sequence=>5
,p_region_template_id=>wwv_flow_api.id(9740827754687991)
,p_css_classes=>'t-ButtonRegion--slimPadding'
,p_group_id=>wwv_flow_api.id(9742375281687992)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9742757922687993)
,p_theme_id=>42
,p_name=>'NOPADDING'
,p_display_name=>'No Padding'
,p_display_sequence=>3
,p_region_template_id=>wwv_flow_api.id(9740827754687991)
,p_css_classes=>'t-ButtonRegion--noPadding'
,p_group_id=>wwv_flow_api.id(9742375281687992)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9742933303687993)
,p_theme_id=>42
,p_name=>'STICK_TO_BOTTOM'
,p_display_name=>'Stick to Bottom for Mobile'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9740827754687991)
,p_css_classes=>'t-ButtonRegion--stickToBottom'
,p_template_types=>'REGION'
,p_help_text=>'This will position the button container region to the bottom of the screen for small screens.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9743902081687994)
,p_theme_id=>42
,p_name=>'SHOW_REGION_ICON'
,p_display_name=>'Show Region Icon'
,p_display_sequence=>50
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--showIcon'
,p_template_types=>'REGION'
,p_help_text=>'Displays the region icon in the region header beside the region title'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9744182345687994)
,p_theme_id=>42
,p_name=>'NOBORDER'
,p_display_name=>'Remove Borders'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--noBorder'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
,p_help_text=>'Removes borders from the region.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9744331579687994)
,p_theme_id=>42
,p_name=>'REMEMBER_CAROUSEL_SLIDE'
,p_display_name=>'Remember Carousel Slide'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'js-useLocalStorage'
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9744787223687994)
,p_theme_id=>42
,p_name=>'SCROLLBODY'
,p_display_name=>'Scroll'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--scrollBody'
,p_group_id=>wwv_flow_api.id(9744546560687994)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9745186038687995)
,p_theme_id=>42
,p_name=>'SLIDE'
,p_display_name=>'Slide'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--carouselSlide'
,p_group_id=>wwv_flow_api.id(9744957574687994)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9745317316687995)
,p_theme_id=>42
,p_name=>'SPIN'
,p_display_name=>'Spin'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--carouselSpin'
,p_group_id=>wwv_flow_api.id(9744957574687994)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9745513769687995)
,p_theme_id=>42
,p_name=>'STACKED'
,p_display_name=>'Stack Region'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--stacked'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
,p_help_text=>'Removes side borders and shadows, and can be useful for accordions and regions that need to be grouped together vertically.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9745772206687995)
,p_theme_id=>42
,p_name=>'SHOW_NEXT_AND_PREVIOUS_BUTTONS'
,p_display_name=>'Show Next and Previous Buttons'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--showCarouselControls'
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9745972419687995)
,p_theme_id=>42
,p_name=>'SHOW_MAXIMIZE_BUTTON'
,p_display_name=>'Show Maximize Button'
,p_display_sequence=>40
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'js-showMaximizeButton'
,p_template_types=>'REGION'
,p_help_text=>'Displays a button in the Region Header to maximize the region. Clicking this button will toggle the maximize state and stretch the region to fill the screen.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9746302837687996)
,p_theme_id=>42
,p_name=>'10_SECONDS'
,p_display_name=>'10 Seconds'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'js-cycle10s'
,p_group_id=>wwv_flow_api.id(9746151420687996)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9746599900687996)
,p_theme_id=>42
,p_name=>'15_SECONDS'
,p_display_name=>'15 Seconds'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'js-cycle15s'
,p_group_id=>wwv_flow_api.id(9746151420687996)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9746728962687996)
,p_theme_id=>42
,p_name=>'20_SECONDS'
,p_display_name=>'20 Seconds'
,p_display_sequence=>40
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'js-cycle20s'
,p_group_id=>wwv_flow_api.id(9746151420687996)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9747179753687996)
,p_theme_id=>42
,p_name=>'240PX'
,p_display_name=>'240px'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'i-h240'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
,p_help_text=>'Sets region body height to 240px.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9747385169687997)
,p_theme_id=>42
,p_name=>'320PX'
,p_display_name=>'320px'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'i-h320'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
,p_help_text=>'Sets region body height to 320px.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9747542228687997)
,p_theme_id=>42
,p_name=>'480PX'
,p_display_name=>'480px'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'i-h480'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9747758213687997)
,p_theme_id=>42
,p_name=>'5_SECONDS'
,p_display_name=>'5 Seconds'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'js-cycle5s'
,p_group_id=>wwv_flow_api.id(9746151420687996)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9747975315687997)
,p_theme_id=>42
,p_name=>'640PX'
,p_display_name=>'640px'
,p_display_sequence=>40
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'i-h640'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9748318023687997)
,p_theme_id=>42
,p_name=>'ACCENT_1'
,p_display_name=>'Accent 1'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--accent1'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9748515833687998)
,p_theme_id=>42
,p_name=>'ACCENT_2'
,p_display_name=>'Accent 2'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--accent2'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9748709705687999)
,p_theme_id=>42
,p_name=>'ACCENT_3'
,p_display_name=>'Accent 3'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--accent3'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9748938535687999)
,p_theme_id=>42
,p_name=>'ACCENT_4'
,p_display_name=>'Accent 4'
,p_display_sequence=>40
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--accent4'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9749148512687999)
,p_theme_id=>42
,p_name=>'ACCENT_5'
,p_display_name=>'Accent 5'
,p_display_sequence=>50
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--accent5'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9749516338687999)
,p_theme_id=>42
,p_name=>'HIDDENHEADERNOAT'
,p_display_name=>'Hidden'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--removeHeader'
,p_group_id=>wwv_flow_api.id(9749398276687999)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9749720297687999)
,p_theme_id=>42
,p_name=>'HIDEOVERFLOW'
,p_display_name=>'Hide'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--hiddenOverflow'
,p_group_id=>wwv_flow_api.id(9744546560687994)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9749908774688000)
,p_theme_id=>42
,p_name=>'HIDEREGIONHEADER'
,p_display_name=>'Hidden but accessible'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--hideHeader'
,p_group_id=>wwv_flow_api.id(9749398276687999)
,p_template_types=>'REGION'
,p_help_text=>'This option will hide the region header.  Note that the region title will still be audible for Screen Readers. Buttons placed in the region header will be hidden and inaccessible.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9750120181688000)
,p_theme_id=>42
,p_name=>'NOBODYPADDING'
,p_display_name=>'Remove Body Padding'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9743063117687993)
,p_css_classes=>'t-Region--noPadding'
,p_template_types=>'REGION'
,p_help_text=>'Removes padding from region body.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9751140577688001)
,p_theme_id=>42
,p_name=>'240PX'
,p_display_name=>'240px'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'i-h240'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
,p_help_text=>'Sets region body height to 240px.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9751355868688001)
,p_theme_id=>42
,p_name=>'320PX'
,p_display_name=>'320px'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'i-h320'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
,p_help_text=>'Sets region body height to 320px.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9751508909688001)
,p_theme_id=>42
,p_name=>'ACCENT_1'
,p_display_name=>'Accent 1'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--accent1'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9751701259688001)
,p_theme_id=>42
,p_name=>'ACCENT_2'
,p_display_name=>'Accent 2'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--accent2'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9751951119688002)
,p_theme_id=>42
,p_name=>'ACCENT_3'
,p_display_name=>'Accent 3'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--accent3'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9752184715688002)
,p_theme_id=>42
,p_name=>'ACCENT_4'
,p_display_name=>'Accent 4'
,p_display_sequence=>40
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--accent4'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9752540094688003)
,p_theme_id=>42
,p_name=>'ICONS_PLUS_OR_MINUS'
,p_display_name=>'Plus or Minus'
,p_display_sequence=>1
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--hideShowIconsMath'
,p_group_id=>wwv_flow_api.id(9752345725688002)
,p_template_types=>'REGION'
,p_help_text=>'Use the plus and minus icons for the expand and collapse button.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9752964636688003)
,p_theme_id=>42
,p_name=>'CONRTOLS_POSITION_END'
,p_display_name=>'End'
,p_display_sequence=>1
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--controlsPosEnd'
,p_group_id=>wwv_flow_api.id(9752760481688003)
,p_template_types=>'REGION'
,p_help_text=>'Position the expand / collapse button to the end of the region header.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9753142308688007)
,p_theme_id=>42
,p_name=>'480PX'
,p_display_name=>'480px'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'i-h480'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
,p_help_text=>'Sets body height to 480px.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9753309685688007)
,p_theme_id=>42
,p_name=>'640PX'
,p_display_name=>'640px'
,p_display_sequence=>40
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'i-h640'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
,p_help_text=>'Sets body height to 640px.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9753587152688007)
,p_theme_id=>42
,p_name=>'REMOVE_UI_DECORATION'
,p_display_name=>'Remove UI Decoration'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--noUI'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
,p_help_text=>'Removes UI decoration (borders, backgrounds, shadows, etc) from the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9753789076688007)
,p_theme_id=>42
,p_name=>'ACCENT_5'
,p_display_name=>'Accent 5'
,p_display_sequence=>50
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--accent5'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9753917867688007)
,p_theme_id=>42
,p_name=>'HIDEOVERFLOW'
,p_display_name=>'Hide'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--hiddenOverflow'
,p_group_id=>wwv_flow_api.id(9744546560687994)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9754123437688008)
,p_theme_id=>42
,p_name=>'NOBODYPADDING'
,p_display_name=>'Remove Body Padding'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--noPadding'
,p_template_types=>'REGION'
,p_help_text=>'Removes padding from region body.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9754356525688008)
,p_theme_id=>42
,p_name=>'NOBORDER'
,p_display_name=>'Remove Borders'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--noBorder'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
,p_help_text=>'Removes borders from the region.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9754503809688008)
,p_theme_id=>42
,p_name=>'SCROLLBODY'
,p_display_name=>'Scroll - Default'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--scrollBody'
,p_group_id=>wwv_flow_api.id(9744546560687994)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9754758969688008)
,p_theme_id=>42
,p_name=>'STACKED'
,p_display_name=>'Stack Region'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'t-Region--stacked'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
,p_help_text=>'Removes side borders and shadows, and can be useful for accordions and regions that need to be grouped together vertically.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9755127729688011)
,p_theme_id=>42
,p_name=>'EXPANDED'
,p_display_name=>'Expanded'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'is-expanded'
,p_group_id=>wwv_flow_api.id(9754966226688011)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9755317233688011)
,p_theme_id=>42
,p_name=>'COLLAPSED'
,p_display_name=>'Collapsed'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'is-collapsed'
,p_group_id=>wwv_flow_api.id(9754966226688011)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9755548970688011)
,p_theme_id=>42
,p_name=>'REMEMBER_COLLAPSIBLE_STATE'
,p_display_name=>'Remember Collapsible State'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9750220677688000)
,p_css_classes=>'js-useLocalStorage'
,p_template_types=>'REGION'
,p_help_text=>'This option saves the current state of the collapsible region for the duration of the session.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9756171079688012)
,p_theme_id=>42
,p_name=>'CONTENT_TITLE_H1'
,p_display_name=>'Heading Level 1'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9755638233688011)
,p_css_classes=>'t-ContentBlock--h1'
,p_group_id=>wwv_flow_api.id(9755973583688012)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9756370489688012)
,p_theme_id=>42
,p_name=>'CONTENT_TITLE_H2'
,p_display_name=>'Heading Level 2'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9755638233688011)
,p_css_classes=>'t-ContentBlock--h2'
,p_group_id=>wwv_flow_api.id(9755973583688012)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9756581451688012)
,p_theme_id=>42
,p_name=>'CONTENT_TITLE_H3'
,p_display_name=>'Heading Level 3'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9755638233688011)
,p_css_classes=>'t-ContentBlock--h3'
,p_group_id=>wwv_flow_api.id(9755973583688012)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9756707002688012)
,p_theme_id=>42
,p_name=>'SHOW_REGION_ICON'
,p_display_name=>'Show Region Icon'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9755638233688011)
,p_css_classes=>'t-ContentBlock--showIcon'
,p_template_types=>'REGION'
,p_help_text=>'Displays the region icon in the region header beside the region title'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9756992639688012)
,p_theme_id=>42
,p_name=>'ADD_BODY_PADDING'
,p_display_name=>'Add Body Padding'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9755638233688011)
,p_css_classes=>'t-ContentBlock--padded'
,p_template_types=>'REGION'
,p_help_text=>'Adds padding to the region''s body container.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9757345046688013)
,p_theme_id=>42
,p_name=>'SHADOW_BACKGROUND'
,p_display_name=>'Shadow Background'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9755638233688011)
,p_css_classes=>'t-ContentBlock--shadowBG'
,p_group_id=>wwv_flow_api.id(9757188941688012)
,p_template_types=>'REGION'
,p_help_text=>'Gives the region body a slightly darker background.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9757597754688013)
,p_theme_id=>42
,p_name=>'LIGHT_BACKGROUND'
,p_display_name=>'Light Background'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9755638233688011)
,p_css_classes=>'t-ContentBlock--lightBG'
,p_group_id=>wwv_flow_api.id(9757188941688012)
,p_template_types=>'REGION'
,p_help_text=>'Gives the region body a slightly lighter background.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9758264100688013)
,p_theme_id=>42
,p_name=>'FEATURED'
,p_display_name=>'Featured'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9757663101688013)
,p_css_classes=>'t-HeroRegion--featured'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9758418627688013)
,p_theme_id=>42
,p_name=>'STACKED_FEATURED'
,p_display_name=>'Stacked Featured'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9757663101688013)
,p_css_classes=>'t-HeroRegion--featured t-HeroRegion--centered'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9758875182688015)
,p_theme_id=>42
,p_name=>'DISPLAY_ICON_NO'
,p_display_name=>'No'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9757663101688013)
,p_css_classes=>'t-HeroRegion--hideIcon'
,p_group_id=>wwv_flow_api.id(9758665881688015)
,p_template_types=>'REGION'
,p_help_text=>'Hide the Hero Region icon.'
);
end;
/
begin
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9759083782688015)
,p_theme_id=>42
,p_name=>'REMOVE_BODY_PADDING'
,p_display_name=>'Remove Body Padding'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9757663101688013)
,p_css_classes=>'t-HeroRegion--noPadding'
,p_template_types=>'REGION'
,p_help_text=>'Removes the padding around the hero region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9759445339688016)
,p_theme_id=>42
,p_name=>'ICONS_CIRCULAR'
,p_display_name=>'Circle'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9757663101688013)
,p_css_classes=>'t-HeroRegion--iconsCircle'
,p_group_id=>wwv_flow_api.id(9759294418688016)
,p_template_types=>'REGION'
,p_help_text=>'The icons are displayed within a circle.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9759631406688016)
,p_theme_id=>42
,p_name=>'ICONS_SQUARE'
,p_display_name=>'Square'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9757663101688013)
,p_css_classes=>'t-HeroRegion--iconsSquare'
,p_group_id=>wwv_flow_api.id(9759294418688016)
,p_template_types=>'REGION'
,p_help_text=>'The icons are displayed within a square.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9760300023688016)
,p_theme_id=>42
,p_name=>'REMOVE_BODY_PADDING'
,p_display_name=>'Remove Body Padding'
,p_display_sequence=>5
,p_region_template_id=>wwv_flow_api.id(9759783899688016)
,p_css_classes=>'t-DialogRegion--noPadding'
,p_template_types=>'REGION'
,p_help_text=>'Removes the padding around the region body.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9760550560688017)
,p_theme_id=>42
,p_name=>'AUTO_HEIGHT_INLINE_DIALOG'
,p_display_name=>'Auto Height'
,p_display_sequence=>1
,p_region_template_id=>wwv_flow_api.id(9759783899688016)
,p_css_classes=>'js-dialog-autoheight'
,p_template_types=>'REGION'
,p_help_text=>'This option will set the height of the dialog to fit its contents.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9760789463688017)
,p_theme_id=>42
,p_name=>'DRAGGABLE'
,p_display_name=>'Draggable'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9759783899688016)
,p_css_classes=>'js-draggable'
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9760916696688017)
,p_theme_id=>42
,p_name=>'MODAL'
,p_display_name=>'Modal'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9759783899688016)
,p_css_classes=>'js-modal'
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9761123158688017)
,p_theme_id=>42
,p_name=>'RESIZABLE'
,p_display_name=>'Resizable'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9759783899688016)
,p_css_classes=>'js-resizable'
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9761582056688017)
,p_theme_id=>42
,p_name=>'SMALL_480X320'
,p_display_name=>'Small (480x320)'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9759783899688016)
,p_css_classes=>'js-dialog-size480x320'
,p_group_id=>wwv_flow_api.id(9761354322688017)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9761740541688017)
,p_theme_id=>42
,p_name=>'LARGE_720X480'
,p_display_name=>'Large (720x480)'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9759783899688016)
,p_css_classes=>'js-dialog-size720x480'
,p_group_id=>wwv_flow_api.id(9761354322688017)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9761971610688018)
,p_theme_id=>42
,p_name=>'MEDIUM_600X400'
,p_display_name=>'Medium (600x400)'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9759783899688016)
,p_css_classes=>'js-dialog-size600x400'
,p_group_id=>wwv_flow_api.id(9761354322688017)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9762693819688018)
,p_theme_id=>42
,p_name=>'AUTO_HEIGHT_INLINE_DIALOG'
,p_display_name=>'Auto Height'
,p_display_sequence=>1
,p_region_template_id=>wwv_flow_api.id(9762017927688018)
,p_css_classes=>'js-dialog-autoheight'
,p_template_types=>'REGION'
,p_help_text=>'This option will set the height of the dialog to fit its contents.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9762895588688018)
,p_theme_id=>42
,p_name=>'LARGE_720X480'
,p_display_name=>'Large (720x480)'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9762017927688018)
,p_css_classes=>'js-dialog-size720x480'
,p_group_id=>wwv_flow_api.id(9761354322688017)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9763067759688018)
,p_theme_id=>42
,p_name=>'MEDIUM_600X400'
,p_display_name=>'Medium (600x400)'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9762017927688018)
,p_css_classes=>'js-dialog-size600x400'
,p_group_id=>wwv_flow_api.id(9761354322688017)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9763205332688019)
,p_theme_id=>42
,p_name=>'SMALL_480X320'
,p_display_name=>'Small (480x320)'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9762017927688018)
,p_css_classes=>'js-dialog-size480x320'
,p_group_id=>wwv_flow_api.id(9761354322688017)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9763471173688019)
,p_theme_id=>42
,p_name=>'NONE'
,p_display_name=>'None'
,p_display_sequence=>1
,p_region_template_id=>wwv_flow_api.id(9762017927688018)
,p_css_classes=>'js-dialog-nosize'
,p_group_id=>wwv_flow_api.id(9761354322688017)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9763669490688019)
,p_theme_id=>42
,p_name=>'REMOVE_BODY_PADDING'
,p_display_name=>'Remove Body Padding'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9762017927688018)
,p_css_classes=>'t-DialogRegion--noPadding'
,p_template_types=>'REGION'
,p_help_text=>'Removes the padding around the region body.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9763889288688019)
,p_theme_id=>42
,p_name=>'REMOVE_PAGE_OVERLAY'
,p_display_name=>'Remove Page Overlay'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9762017927688018)
,p_css_classes=>'js-popup-noOverlay'
,p_template_types=>'REGION'
,p_help_text=>'This option will display the inline dialog without an overlay on the background.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9764259025688019)
,p_theme_id=>42
,p_name=>'REMOVEBORDERS'
,p_display_name=>'Remove Borders'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9763915989688019)
,p_css_classes=>'t-IRR-region--noBorders'
,p_template_types=>'REGION'
,p_help_text=>'Removes borders around the Interactive Report'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9764412556688020)
,p_theme_id=>42
,p_name=>'SHOW_MAXIMIZE_BUTTON'
,p_display_name=>'Show Maximize Button'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9763915989688019)
,p_css_classes=>'js-showMaximizeButton'
,p_template_types=>'REGION'
,p_help_text=>'Displays a button in the Interactive Reports toolbar to maximize the report. Clicking this button will toggle the maximize state and stretch the report to fill the screen.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9765987899688021)
,p_theme_id=>42
,p_name=>'SCROLLBODY'
,p_display_name=>'Scroll - Default'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--scrollBody'
,p_group_id=>wwv_flow_api.id(9744546560687994)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9766129708688021)
,p_theme_id=>42
,p_name=>'HIDEREGIONHEADER'
,p_display_name=>'Hidden but accessible'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--hideHeader'
,p_group_id=>wwv_flow_api.id(9749398276687999)
,p_template_types=>'REGION'
,p_help_text=>'This option will hide the region header.  Note that the region title will still be audible for Screen Readers. Buttons placed in the region header will be hidden and inaccessible.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9766335694688021)
,p_theme_id=>42
,p_name=>'HIDEOVERFLOW'
,p_display_name=>'Hide'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--hiddenOverflow'
,p_group_id=>wwv_flow_api.id(9744546560687994)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9766556184688021)
,p_theme_id=>42
,p_name=>'HIDDENHEADERNOAT'
,p_display_name=>'Hidden'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--removeHeader'
,p_group_id=>wwv_flow_api.id(9749398276687999)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9766782834688021)
,p_theme_id=>42
,p_name=>'ACCENT_1'
,p_display_name=>'Accent 1'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent1'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9766984668688021)
,p_theme_id=>42
,p_name=>'ACCENT_2'
,p_display_name=>'Accent 2'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent2'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9767159733688022)
,p_theme_id=>42
,p_name=>'ACCENT_3'
,p_display_name=>'Accent 3'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent3'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9767392254688022)
,p_theme_id=>42
,p_name=>'ACCENT_4'
,p_display_name=>'Accent 4'
,p_display_sequence=>40
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent4'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9767531079688022)
,p_theme_id=>42
,p_name=>'ACCENT_5'
,p_display_name=>'Accent 5'
,p_display_sequence=>50
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent5'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9767780260688022)
,p_theme_id=>42
,p_name=>'SHOW_REGION_ICON'
,p_display_name=>'Show Region Icon'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--showIcon'
,p_template_types=>'REGION'
,p_help_text=>'Displays the region icon in the region header beside the region title'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9767921822688022)
,p_theme_id=>42
,p_name=>'TEXT_CONTENT'
,p_display_name=>'Text Content'
,p_display_sequence=>40
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--textContent'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
,p_help_text=>'Useful for displaying primarily text-based content, such as FAQs and more.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9768145989688022)
,p_theme_id=>42
,p_name=>'NOBORDER'
,p_display_name=>'Remove Borders'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--noBorder'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
,p_help_text=>'Removes borders from the region.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9768351111688023)
,p_theme_id=>42
,p_name=>'NOBODYPADDING'
,p_display_name=>'Remove Body Padding'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--noPadding'
,p_template_types=>'REGION'
,p_help_text=>'Removes padding from region body.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9768584156688023)
,p_theme_id=>42
,p_name=>'STACKED'
,p_display_name=>'Stack Region'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--stacked'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
,p_help_text=>'Removes side borders and shadows, and can be useful for accordions and regions that need to be grouped together vertically.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9768717982688023)
,p_theme_id=>42
,p_name=>'240PX'
,p_display_name=>'240px'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'i-h240'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
,p_help_text=>'Sets region body height to 240px.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9768973144688023)
,p_theme_id=>42
,p_name=>'320PX'
,p_display_name=>'320px'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'i-h320'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
,p_help_text=>'Sets region body height to 320px.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9769187020688023)
,p_theme_id=>42
,p_name=>'ACCENT_6'
,p_display_name=>'Accent 6'
,p_display_sequence=>60
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent6'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9769307772688023)
,p_theme_id=>42
,p_name=>'ACCENT_7'
,p_display_name=>'Accent 7'
,p_display_sequence=>70
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent7'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9769592326688024)
,p_theme_id=>42
,p_name=>'ACCENT_8'
,p_display_name=>'Accent 8'
,p_display_sequence=>80
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent8'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9769736420688024)
,p_theme_id=>42
,p_name=>'ACCENT_9'
,p_display_name=>'Accent 9'
,p_display_sequence=>90
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent9'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9769924600688024)
,p_theme_id=>42
,p_name=>'ACCENT_10'
,p_display_name=>'Accent 10'
,p_display_sequence=>100
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent10'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9770106198688024)
,p_theme_id=>42
,p_name=>'ACCENT_11'
,p_display_name=>'Accent 11'
,p_display_sequence=>110
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent11'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9770317538688024)
,p_theme_id=>42
,p_name=>'ACCENT_12'
,p_display_name=>'Accent 12'
,p_display_sequence=>120
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent12'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9770590908688025)
,p_theme_id=>42
,p_name=>'ACCENT_13'
,p_display_name=>'Accent 13'
,p_display_sequence=>130
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent13'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9770738418688025)
,p_theme_id=>42
,p_name=>'ACCENT_14'
,p_display_name=>'Accent 14'
,p_display_sequence=>140
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent14'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9770973617688025)
,p_theme_id=>42
,p_name=>'ACCENT_15'
,p_display_name=>'Accent 15'
,p_display_sequence=>150
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--accent15'
,p_group_id=>wwv_flow_api.id(9748113149687997)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9771157138688025)
,p_theme_id=>42
,p_name=>'SHOW_MAXIMIZE_BUTTON'
,p_display_name=>'Show Maximize Button'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'js-showMaximizeButton'
,p_template_types=>'REGION'
,p_help_text=>'Displays a button in the Region Header to maximize the region. Clicking this button will toggle the maximize state and stretch the region to fill the screen.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9771342692688025)
,p_theme_id=>42
,p_name=>'REMOVE_UI_DECORATION'
,p_display_name=>'Remove UI Decoration'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'t-Region--noUI'
,p_group_id=>wwv_flow_api.id(9741709467687992)
,p_template_types=>'REGION'
,p_help_text=>'Removes UI decoration (borders, backgrounds, shadows, etc) from the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9771500303688025)
,p_theme_id=>42
,p_name=>'480PX'
,p_display_name=>'480px'
,p_display_sequence=>30
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'i-h480'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9771700188688025)
,p_theme_id=>42
,p_name=>'640PX'
,p_display_name=>'640px'
,p_display_sequence=>40
,p_region_template_id=>wwv_flow_api.id(9765042323688020)
,p_css_classes=>'i-h640'
,p_group_id=>wwv_flow_api.id(9746992832687996)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9772784233688027)
,p_theme_id=>42
,p_name=>'REMEMBER_ACTIVE_TAB'
,p_display_name=>'Remember Active Tab'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9771800871688026)
,p_css_classes=>'js-useLocalStorage'
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9773157338688027)
,p_theme_id=>42
,p_name=>'FILL_TAB_LABELS'
,p_display_name=>'Fill Tab Labels'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9771800871688026)
,p_css_classes=>'t-TabsRegion-mod--fillLabels'
,p_group_id=>wwv_flow_api.id(9772915564688027)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9773577320688028)
,p_theme_id=>42
,p_name=>'SIMPLE'
,p_display_name=>'Simple'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9771800871688026)
,p_css_classes=>'t-TabsRegion-mod--simple'
,p_group_id=>wwv_flow_api.id(9773387695688028)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9773704864688028)
,p_theme_id=>42
,p_name=>'PILL'
,p_display_name=>'Pill'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9771800871688026)
,p_css_classes=>'t-TabsRegion-mod--pill'
,p_group_id=>wwv_flow_api.id(9773387695688028)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9774105044688028)
,p_theme_id=>42
,p_name=>'TABS_SMALL'
,p_display_name=>'Small'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9771800871688026)
,p_css_classes=>'t-TabsRegion-mod--small'
,p_group_id=>wwv_flow_api.id(9773926842688028)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9774324369688028)
,p_theme_id=>42
,p_name=>'TABSLARGE'
,p_display_name=>'Large'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9771800871688026)
,p_css_classes=>'t-TabsRegion-mod--large'
,p_group_id=>wwv_flow_api.id(9773926842688028)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9774794774688029)
,p_theme_id=>42
,p_name=>'HIDE_BREADCRUMB'
,p_display_name=>'Show Breadcrumbs'
,p_display_sequence=>1
,p_region_template_id=>wwv_flow_api.id(9774426068688028)
,p_css_classes=>'t-BreadcrumbRegion--showBreadcrumb'
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9774912186688029)
,p_theme_id=>42
,p_name=>'GET_TITLE_FROM_BREADCRUMB'
,p_display_name=>'Use Current Breadcrumb Entry'
,p_display_sequence=>1
,p_region_template_id=>wwv_flow_api.id(9774426068688028)
,p_css_classes=>'t-BreadcrumbRegion--useBreadcrumbTitle'
,p_group_id=>wwv_flow_api.id(9755973583688012)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9775107240688029)
,p_theme_id=>42
,p_name=>'USE_COMPACT_STYLE'
,p_display_name=>'Use Compact Style'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9774426068688028)
,p_css_classes=>'t-BreadcrumbRegion--compactTitle'
,p_template_types=>'REGION'
,p_help_text=>'Uses a compact style for the breadcrumbs.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9775379250688029)
,p_theme_id=>42
,p_name=>'REGION_HEADER_VISIBLE'
,p_display_name=>'Use Region Title'
,p_display_sequence=>1
,p_region_template_id=>wwv_flow_api.id(9774426068688028)
,p_css_classes=>'t-BreadcrumbRegion--useRegionTitle'
,p_group_id=>wwv_flow_api.id(9755973583688012)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9776239761688030)
,p_theme_id=>42
,p_name=>'HIDESMALLSCREENS'
,p_display_name=>'Small Screens (Tablet)'
,p_display_sequence=>20
,p_region_template_id=>wwv_flow_api.id(9775498010688029)
,p_css_classes=>'t-Wizard--hideStepsSmall'
,p_group_id=>wwv_flow_api.id(9776081830688030)
,p_template_types=>'REGION'
,p_help_text=>'Hides the wizard progress steps for screens that are smaller than 768px wide.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9776448183688031)
,p_theme_id=>42
,p_name=>'HIDEXSMALLSCREENS'
,p_display_name=>'X Small Screens (Mobile)'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9775498010688029)
,p_css_classes=>'t-Wizard--hideStepsXSmall'
,p_group_id=>wwv_flow_api.id(9776081830688030)
,p_template_types=>'REGION'
,p_help_text=>'Hides the wizard progress steps for screens that are smaller than 768px wide.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9776633662688031)
,p_theme_id=>42
,p_name=>'SHOW_TITLE'
,p_display_name=>'Show Title'
,p_display_sequence=>10
,p_region_template_id=>wwv_flow_api.id(9775498010688029)
,p_css_classes=>'t-Wizard--showTitle'
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9777432974688037)
,p_theme_id=>42
,p_name=>'128PX'
,p_display_name=>'128px'
,p_display_sequence=>50
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--xxlarge'
,p_group_id=>wwv_flow_api.id(9777212990688037)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9777640632688037)
,p_theme_id=>42
,p_name=>'32PX'
,p_display_name=>'32px'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--small'
,p_group_id=>wwv_flow_api.id(9777212990688037)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9777854239688038)
,p_theme_id=>42
,p_name=>'48PX'
,p_display_name=>'48px'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--medium'
,p_group_id=>wwv_flow_api.id(9777212990688037)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9778046176688038)
,p_theme_id=>42
,p_name=>'64PX'
,p_display_name=>'64px'
,p_display_sequence=>30
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--large'
,p_group_id=>wwv_flow_api.id(9777212990688037)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9778280735688038)
,p_theme_id=>42
,p_name=>'96PX'
,p_display_name=>'96px'
,p_display_sequence=>40
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--xlarge'
,p_group_id=>wwv_flow_api.id(9777212990688037)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9778683022688039)
,p_theme_id=>42
,p_name=>'2COLUMNGRID'
,p_display_name=>'2 Column Grid'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
,p_help_text=>'Arrange badges in a two column grid'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9778822850688039)
,p_theme_id=>42
,p_name=>'3COLUMNGRID'
,p_display_name=>'3 Column Grid'
,p_display_sequence=>30
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--cols t-BadgeList--3cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
,p_help_text=>'Arrange badges in a 3 column grid'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9779040186688039)
,p_theme_id=>42
,p_name=>'4COLUMNGRID'
,p_display_name=>'4 Column Grid'
,p_display_sequence=>40
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--cols t-BadgeList--4cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9779267517688039)
,p_theme_id=>42
,p_name=>'5COLUMNGRID'
,p_display_name=>'5 Column Grid'
,p_display_sequence=>50
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--cols t-BadgeList--5cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9779486683688039)
,p_theme_id=>42
,p_name=>'FLEXIBLEBOX'
,p_display_name=>'Flexible Box'
,p_display_sequence=>80
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--flex'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9779692663688040)
,p_theme_id=>42
,p_name=>'FLOATITEMS'
,p_display_name=>'Float Items'
,p_display_sequence=>70
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--float'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9779888377688040)
,p_theme_id=>42
,p_name=>'FIXED'
,p_display_name=>'Span Horizontally'
,p_display_sequence=>60
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--fixed'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9780008118688040)
,p_theme_id=>42
,p_name=>'STACKED'
,p_display_name=>'Stacked'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--stacked'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9780207150688040)
,p_theme_id=>42
,p_name=>'APPLY_THEME_COLORS'
,p_display_name=>'Apply Theme Colors'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'u-colors'
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9780621505688040)
,p_theme_id=>42
,p_name=>'CIRCULAR'
,p_display_name=>'Circular'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--circular'
,p_group_id=>wwv_flow_api.id(9780462791688040)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9780874638688041)
,p_theme_id=>42
,p_name=>'GRID'
,p_display_name=>'Grid'
,p_display_sequence=>30
,p_report_template_id=>wwv_flow_api.id(9776923303688037)
,p_css_classes=>'t-BadgeList--dash'
,p_group_id=>wwv_flow_api.id(9780462791688040)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9781465106688042)
,p_theme_id=>42
,p_name=>'CARDS_COLOR_FILL'
,p_display_name=>'Color Fill'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--animColorFill'
,p_group_id=>wwv_flow_api.id(9781244843688042)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9781665086688042)
,p_theme_id=>42
,p_name=>'CARD_RAISE_CARD'
,p_display_name=>'Raise Card'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--animRaiseCard'
,p_group_id=>wwv_flow_api.id(9781244843688042)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9782058980688043)
,p_theme_id=>42
,p_name=>'ICONS_SQUARE'
,p_display_name=>'Square'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--iconsSquare'
,p_group_id=>wwv_flow_api.id(9781895042688042)
,p_template_types=>'REPORT'
,p_help_text=>'The icons are displayed within a square shape.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9782239485688043)
,p_theme_id=>42
,p_name=>'ICONS_ROUNDED'
,p_display_name=>'Rounded Corners'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--iconsRounded'
,p_group_id=>wwv_flow_api.id(9781895042688042)
,p_template_types=>'REPORT'
,p_help_text=>'The icons are displayed within a square with rounded corners.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9782466283688044)
,p_theme_id=>42
,p_name=>'BLOCK'
,p_display_name=>'Block'
,p_display_sequence=>40
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--featured t-Cards--block force-fa-lg'
,p_group_id=>wwv_flow_api.id(9780462791688040)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9782605675688044)
,p_theme_id=>42
,p_name=>'DISPLAY_SUBTITLE'
,p_display_name=>'Display Subtitle'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--displaySubtitle'
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9782815150688044)
,p_theme_id=>42
,p_name=>'2_COLUMNS'
,p_display_name=>'2 Columns'
,p_display_sequence=>15
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9783029467688044)
,p_theme_id=>42
,p_name=>'3_COLUMNS'
,p_display_name=>'3 Columns'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--3cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
end;
/
begin
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9783274333688044)
,p_theme_id=>42
,p_name=>'4_COLUMNS'
,p_display_name=>'4 Columns'
,p_display_sequence=>30
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--4cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9783490189688045)
,p_theme_id=>42
,p_name=>'5_COLUMNS'
,p_display_name=>'5 Columns'
,p_display_sequence=>50
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--5cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9783631980688045)
,p_theme_id=>42
,p_name=>'FLOAT'
,p_display_name=>'Float'
,p_display_sequence=>60
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--float'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9783820992688045)
,p_theme_id=>42
,p_name=>'SPAN_HORIZONTALLY'
,p_display_name=>'Span Horizontally'
,p_display_sequence=>70
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--spanHorizontally'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9784257337688045)
,p_theme_id=>42
,p_name=>'2_LINES'
,p_display_name=>'2 Lines'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--desc-2ln'
,p_group_id=>wwv_flow_api.id(9784006583688045)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9784416941688046)
,p_theme_id=>42
,p_name=>'3_LINES'
,p_display_name=>'3 Lines'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--desc-3ln'
,p_group_id=>wwv_flow_api.id(9784006583688045)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9784658460688046)
,p_theme_id=>42
,p_name=>'4_LINES'
,p_display_name=>'4 Lines'
,p_display_sequence=>30
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--desc-4ln'
,p_group_id=>wwv_flow_api.id(9784006583688045)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9784873971688046)
,p_theme_id=>42
,p_name=>'USE_THEME_COLORS'
,p_display_name=>'Apply Theme Colors'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'u-colors'
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9785267303688046)
,p_theme_id=>42
,p_name=>'DISPLAY_ICONS'
,p_display_name=>'Display Icons'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--displayIcons'
,p_group_id=>wwv_flow_api.id(9785095805688046)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9785415975688046)
,p_theme_id=>42
,p_name=>'DISPLAY_INITIALS'
,p_display_name=>'Display Initials'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--displayInitials'
,p_group_id=>wwv_flow_api.id(9785095805688046)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9785643813688047)
,p_theme_id=>42
,p_name=>'FEATURED'
,p_display_name=>'Featured'
,p_display_sequence=>30
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--featured force-fa-lg'
,p_group_id=>wwv_flow_api.id(9780462791688040)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9785897996688047)
,p_theme_id=>42
,p_name=>'BASIC'
,p_display_name=>'Basic'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--basic'
,p_group_id=>wwv_flow_api.id(9780462791688040)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9786064799688048)
,p_theme_id=>42
,p_name=>'COMPACT'
,p_display_name=>'Compact'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--compact'
,p_group_id=>wwv_flow_api.id(9780462791688040)
,p_template_types=>'REPORT'
,p_help_text=>'Use this option when you want to show smaller cards.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9786238220688048)
,p_theme_id=>42
,p_name=>'HIDDEN_BODY_TEXT'
,p_display_name=>'Hidden'
,p_display_sequence=>50
,p_report_template_id=>wwv_flow_api.id(9780977451688041)
,p_css_classes=>'t-Cards--hideBody'
,p_group_id=>wwv_flow_api.id(9784006583688045)
,p_template_types=>'REPORT'
,p_help_text=>'This option hides the card body which contains description and subtext.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9786679197688048)
,p_theme_id=>42
,p_name=>'ICONS_SQUARE'
,p_display_name=>'Square'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9786327444688048)
,p_css_classes=>'t-Comments--iconsSquare'
,p_group_id=>wwv_flow_api.id(9781895042688042)
,p_template_types=>'REPORT'
,p_help_text=>'The icons are displayed within a square shape.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9786838702688048)
,p_theme_id=>42
,p_name=>'ICONS_ROUNDED'
,p_display_name=>'Rounded Corners'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9786327444688048)
,p_css_classes=>'t-Comments--iconsRounded'
,p_group_id=>wwv_flow_api.id(9781895042688042)
,p_template_types=>'REPORT'
,p_help_text=>'The icons are displayed within a square with rounded corners.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9787290765688049)
,p_theme_id=>42
,p_name=>'BASIC'
,p_display_name=>'Basic'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9786327444688048)
,p_css_classes=>'t-Comments--basic'
,p_group_id=>wwv_flow_api.id(9787068036688049)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9787464324688049)
,p_theme_id=>42
,p_name=>'SPEECH_BUBBLES'
,p_display_name=>'Speech Bubbles'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9786327444688048)
,p_css_classes=>'t-Comments--chat'
,p_group_id=>wwv_flow_api.id(9787068036688049)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9787841400688050)
,p_theme_id=>42
,p_name=>'2_COLUMN_GRID'
,p_display_name=>'2 Column Grid'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--cols t-MediaList--2cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9788039141688050)
,p_theme_id=>42
,p_name=>'3_COLUMN_GRID'
,p_display_name=>'3 Column Grid'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--cols t-MediaList--3cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9788225822688050)
,p_theme_id=>42
,p_name=>'4_COLUMN_GRID'
,p_display_name=>'4 Column Grid'
,p_display_sequence=>30
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--cols t-MediaList--4cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9788436586688050)
,p_theme_id=>42
,p_name=>'5_COLUMN_GRID'
,p_display_name=>'5 Column Grid'
,p_display_sequence=>40
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--cols t-MediaList--5cols'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9788661713688050)
,p_theme_id=>42
,p_name=>'STACK'
,p_display_name=>'Stack'
,p_display_sequence=>5
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--stack'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9788871859688051)
,p_theme_id=>42
,p_name=>'SPAN_HORIZONTAL'
,p_display_name=>'Span Horizontal'
,p_display_sequence=>50
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--horizontal'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9789017495688051)
,p_theme_id=>42
,p_name=>'SHOW_ICONS'
,p_display_name=>'Show Icons'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--showIcons'
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9789204635688051)
,p_theme_id=>42
,p_name=>'SHOW_DESCRIPTION'
,p_display_name=>'Show Description'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--showDesc'
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9789448207688051)
,p_theme_id=>42
,p_name=>'SHOW_BADGES'
,p_display_name=>'Show Badges'
,p_display_sequence=>30
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--showBadges'
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9789625810688051)
,p_theme_id=>42
,p_name=>'APPLY_THEME_COLORS'
,p_display_name=>'Apply Theme Colors'
,p_display_sequence=>40
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'u-colors'
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9789871387688051)
,p_theme_id=>42
,p_name=>'ICONS_SQUARE'
,p_display_name=>'Square'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--iconsSquare'
,p_group_id=>wwv_flow_api.id(9781895042688042)
,p_template_types=>'REPORT'
,p_help_text=>'The icons are displayed within a square shape.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9790040523688051)
,p_theme_id=>42
,p_name=>'ICONS_ROUNDED'
,p_display_name=>'Rounded Corners'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--iconsRounded'
,p_group_id=>wwv_flow_api.id(9781895042688042)
,p_template_types=>'REPORT'
,p_help_text=>'The icons are displayed within a square with rounded corners.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9790422475688052)
,p_theme_id=>42
,p_name=>'LARGE'
,p_display_name=>'Large'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9787594913688049)
,p_css_classes=>'t-MediaList--large force-fa-lg'
,p_group_id=>wwv_flow_api.id(9790269827688052)
,p_template_types=>'REPORT'
,p_help_text=>'Increases the size of the text and icons in the list.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9791221893688053)
,p_theme_id=>42
,p_name=>'REMOVEALLBORDERS'
,p_display_name=>'No Borders'
,p_display_sequence=>30
,p_report_template_id=>wwv_flow_api.id(9790776953688052)
,p_css_classes=>'t-Report--noBorders'
,p_group_id=>wwv_flow_api.id(9791070979688053)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9791411864688053)
,p_theme_id=>42
,p_name=>'STRETCHREPORT'
,p_display_name=>'Stretch Report'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9790776953688052)
,p_css_classes=>'t-Report--stretch'
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9791696789688053)
,p_theme_id=>42
,p_name=>'REMOVEOUTERBORDERS'
,p_display_name=>'No Outer Borders'
,p_display_sequence=>40
,p_report_template_id=>wwv_flow_api.id(9790776953688052)
,p_css_classes=>'t-Report--inline'
,p_group_id=>wwv_flow_api.id(9791070979688053)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9792019131688053)
,p_theme_id=>42
,p_name=>'ALTROWCOLORSDISABLE'
,p_display_name=>'Disable'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9790776953688052)
,p_css_classes=>'t-Report--staticRowColors'
,p_group_id=>wwv_flow_api.id(9791834752688053)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9792258448688053)
,p_theme_id=>42
,p_name=>'ALTROWCOLORSENABLE'
,p_display_name=>'Enable'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9790776953688052)
,p_css_classes=>'t-Report--altRowsDefault'
,p_group_id=>wwv_flow_api.id(9791834752688053)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9792426691688054)
,p_theme_id=>42
,p_name=>'HORIZONTALBORDERS'
,p_display_name=>'Horizontal Only'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9790776953688052)
,p_css_classes=>'t-Report--horizontalBorders'
,p_group_id=>wwv_flow_api.id(9791070979688053)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9792672707688054)
,p_theme_id=>42
,p_name=>'VERTICALBORDERS'
,p_display_name=>'Vertical Only'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9790776953688052)
,p_css_classes=>'t-Report--verticalBorders'
,p_group_id=>wwv_flow_api.id(9791070979688053)
,p_template_types=>'REPORT'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9793097809688054)
,p_theme_id=>42
,p_name=>'ENABLE'
,p_display_name=>'Enable'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9790776953688052)
,p_css_classes=>'t-Report--rowHighlight'
,p_group_id=>wwv_flow_api.id(9792831199688054)
,p_template_types=>'REPORT'
,p_help_text=>'Enable row highlighting on mouse over'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9793269539688054)
,p_theme_id=>42
,p_name=>'ROWHIGHLIGHTDISABLE'
,p_display_name=>'Disable'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9790776953688052)
,p_css_classes=>'t-Report--rowHighlightOff'
,p_group_id=>wwv_flow_api.id(9792831199688054)
,p_template_types=>'REPORT'
,p_help_text=>'Disable row highlighting on mouse over'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9793644685688055)
,p_theme_id=>42
,p_name=>'COMPACT'
,p_display_name=>'Compact'
,p_display_sequence=>1
,p_report_template_id=>wwv_flow_api.id(9793319708688054)
,p_css_classes=>'t-Timeline--compact'
,p_group_id=>wwv_flow_api.id(9780462791688040)
,p_template_types=>'REPORT'
,p_help_text=>'Displays a compact version of timeline with smaller text and fewer columns.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9794054787688055)
,p_theme_id=>42
,p_name=>'LEFT_ALIGNED_DETAILS'
,p_display_name=>'Left Aligned Details'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9793749257688055)
,p_css_classes=>'t-AVPList--leftAligned'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9794255787688055)
,p_theme_id=>42
,p_name=>'RIGHT_ALIGNED_DETAILS'
,p_display_name=>'Right Aligned Details'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9793749257688055)
,p_css_classes=>'t-AVPList--rightAligned'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9794688008688056)
,p_theme_id=>42
,p_name=>'FIXED_SMALL'
,p_display_name=>'Fixed - Small'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9793749257688055)
,p_css_classes=>'t-AVPList--fixedLabelSmall'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9794805493688056)
,p_theme_id=>42
,p_name=>'FIXED_MEDIUM'
,p_display_name=>'Fixed - Medium'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9793749257688055)
,p_css_classes=>'t-AVPList--fixedLabelMedium'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9795013132688056)
,p_theme_id=>42
,p_name=>'FIXED_LARGE'
,p_display_name=>'Fixed - Large'
,p_display_sequence=>30
,p_report_template_id=>wwv_flow_api.id(9793749257688055)
,p_css_classes=>'t-AVPList--fixedLabelLarge'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9795243555688056)
,p_theme_id=>42
,p_name=>'VARIABLE_SMALL'
,p_display_name=>'Variable - Small'
,p_display_sequence=>40
,p_report_template_id=>wwv_flow_api.id(9793749257688055)
,p_css_classes=>'t-AVPList--variableLabelSmall'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9795456523688056)
,p_theme_id=>42
,p_name=>'VARIABLE_MEDIUM'
,p_display_name=>'Variable - Medium'
,p_display_sequence=>50
,p_report_template_id=>wwv_flow_api.id(9793749257688055)
,p_css_classes=>'t-AVPList--variableLabelMedium'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9795688311688056)
,p_theme_id=>42
,p_name=>'VARIABLE_LARGE'
,p_display_name=>'Variable - Large'
,p_display_sequence=>60
,p_report_template_id=>wwv_flow_api.id(9793749257688055)
,p_css_classes=>'t-AVPList--variableLabelLarge'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9796015402688057)
,p_theme_id=>42
,p_name=>'FIXED_SMALL'
,p_display_name=>'Fixed - Small'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9795721115688056)
,p_css_classes=>'t-AVPList--fixedLabelSmall'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9796230348688057)
,p_theme_id=>42
,p_name=>'FIXED_MEDIUM'
,p_display_name=>'Fixed - Medium'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9795721115688056)
,p_css_classes=>'t-AVPList--fixedLabelMedium'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9796433151688057)
,p_theme_id=>42
,p_name=>'FIXED_LARGE'
,p_display_name=>'Fixed - Large'
,p_display_sequence=>30
,p_report_template_id=>wwv_flow_api.id(9795721115688056)
,p_css_classes=>'t-AVPList--fixedLabelLarge'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9796602957688057)
,p_theme_id=>42
,p_name=>'VARIABLE_LARGE'
,p_display_name=>'Variable - Large'
,p_display_sequence=>60
,p_report_template_id=>wwv_flow_api.id(9795721115688056)
,p_css_classes=>'t-AVPList--variableLabelLarge'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9796856579688057)
,p_theme_id=>42
,p_name=>'VARIABLE_MEDIUM'
,p_display_name=>'Variable - Medium'
,p_display_sequence=>50
,p_report_template_id=>wwv_flow_api.id(9795721115688056)
,p_css_classes=>'t-AVPList--variableLabelMedium'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9797036912688058)
,p_theme_id=>42
,p_name=>'VARIABLE_SMALL'
,p_display_name=>'Variable - Small'
,p_display_sequence=>40
,p_report_template_id=>wwv_flow_api.id(9795721115688056)
,p_css_classes=>'t-AVPList--variableLabelSmall'
,p_group_id=>wwv_flow_api.id(9794418510688055)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9797265864688058)
,p_theme_id=>42
,p_name=>'LEFT_ALIGNED_DETAILS'
,p_display_name=>'Left Aligned Details'
,p_display_sequence=>10
,p_report_template_id=>wwv_flow_api.id(9795721115688056)
,p_css_classes=>'t-AVPList--leftAligned'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9797437214688058)
,p_theme_id=>42
,p_name=>'RIGHT_ALIGNED_DETAILS'
,p_display_name=>'Right Aligned Details'
,p_display_sequence=>20
,p_report_template_id=>wwv_flow_api.id(9795721115688056)
,p_css_classes=>'t-AVPList--rightAligned'
,p_group_id=>wwv_flow_api.id(9778470443688038)
,p_template_types=>'REPORT'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9798090313688064)
,p_theme_id=>42
,p_name=>'FLOATITEMS'
,p_display_name=>'Float Items'
,p_display_sequence=>70
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--float'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_help_text=>'Float badges to left'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9798295253688064)
,p_theme_id=>42
,p_name=>'FLEXIBLEBOX'
,p_display_name=>'Flexible Box'
,p_display_sequence=>80
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--flex'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_help_text=>'Use flexbox to arrange items'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9798405364688064)
,p_theme_id=>42
,p_name=>'FIXED'
,p_display_name=>'Span Horizontally'
,p_display_sequence=>60
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--fixed'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_help_text=>'Span badges horizontally'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9798648014688064)
,p_theme_id=>42
,p_name=>'STACKED'
,p_display_name=>'Stacked'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--stacked'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_help_text=>'Stack badges on top of each other'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9798821051688065)
,p_theme_id=>42
,p_name=>'2COLUMNGRID'
,p_display_name=>'2 Column Grid'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_help_text=>'Arrange badges in a two column grid'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9799091561688065)
,p_theme_id=>42
,p_name=>'3COLUMNGRID'
,p_display_name=>'3 Column Grid'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--cols t-BadgeList--3cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_help_text=>'Arrange badges in a 3 column grid'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9799268132688065)
,p_theme_id=>42
,p_name=>'4COLUMNGRID'
,p_display_name=>'4 Column Grid'
,p_display_sequence=>40
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--cols t-BadgeList--4cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_help_text=>'Arrange badges in 4 column grid'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9799489130688065)
,p_theme_id=>42
,p_name=>'5COLUMNGRID'
,p_display_name=>'5 Column Grid'
,p_display_sequence=>50
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--cols t-BadgeList--5cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_help_text=>'Arrange badges in a 5 column grid'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9799818600688065)
,p_theme_id=>42
,p_name=>'SMALL'
,p_display_name=>'32px'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--small'
,p_group_id=>wwv_flow_api.id(9799694951688065)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9800090821688066)
,p_theme_id=>42
,p_name=>'MEDIUM'
,p_display_name=>'48px'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--medium'
,p_group_id=>wwv_flow_api.id(9799694951688065)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9800206279688066)
,p_theme_id=>42
,p_name=>'LARGE'
,p_display_name=>'64px'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--large'
,p_group_id=>wwv_flow_api.id(9799694951688065)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9800456445688066)
,p_theme_id=>42
,p_name=>'XXLARGE'
,p_display_name=>'128px'
,p_display_sequence=>50
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--xxlarge'
,p_group_id=>wwv_flow_api.id(9799694951688065)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9800679818688066)
,p_theme_id=>42
,p_name=>'XLARGE'
,p_display_name=>'96px'
,p_display_sequence=>40
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--xlarge'
,p_group_id=>wwv_flow_api.id(9799694951688065)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9800855209688066)
,p_theme_id=>42
,p_name=>'APPLY_THEME_COLORS'
,p_display_name=>'Apply Theme Colors'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'u-colors'
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9801200369688067)
,p_theme_id=>42
,p_name=>'CIRCULAR'
,p_display_name=>'Circular'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--circular'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9801434109688067)
,p_theme_id=>42
,p_name=>'GRID'
,p_display_name=>'Grid'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9797511594688059)
,p_css_classes=>'t-BadgeList--dash'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9801895770688067)
,p_theme_id=>42
,p_name=>'CARDS_STACKED'
,p_display_name=>'Stacked'
,p_display_sequence=>5
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--stacked'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_help_text=>'Stacks the cards on top of each other.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9802291760688068)
,p_theme_id=>42
,p_name=>'COLOR_FILL'
,p_display_name=>'Color Fill'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--animColorFill'
,p_group_id=>wwv_flow_api.id(9802035137688068)
,p_template_types=>'LIST'
,p_help_text=>'Fills the card background with the color of the icon or default link style.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9802459350688068)
,p_theme_id=>42
,p_name=>'RAISE_CARD'
,p_display_name=>'Raise Card'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--animRaiseCard'
,p_group_id=>wwv_flow_api.id(9802035137688068)
,p_template_types=>'LIST'
,p_help_text=>'Raises the card so it pops up.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9802897405688068)
,p_theme_id=>42
,p_name=>'ICONS_SQUARE'
,p_display_name=>'Square'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--iconsSquare'
,p_group_id=>wwv_flow_api.id(9802696520688068)
,p_template_types=>'LIST'
,p_help_text=>'The icons are displayed within a square shape.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9803019139688068)
,p_theme_id=>42
,p_name=>'ICONS_ROUNDED'
,p_display_name=>'Rounded Corners'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--iconsRounded'
,p_group_id=>wwv_flow_api.id(9802696520688068)
,p_template_types=>'LIST'
,p_help_text=>'The icons are displayed within a square with rounded corners.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9803263241688068)
,p_theme_id=>42
,p_name=>'DISPLAY_SUBTITLE'
,p_display_name=>'Display Subtitle'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--displaySubtitle'
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9803481667688068)
,p_theme_id=>42
,p_name=>'BLOCK'
,p_display_name=>'Block'
,p_display_sequence=>40
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--featured t-Cards--block force-fa-lg'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9803617339688069)
,p_theme_id=>42
,p_name=>'SPAN_HORIZONTALLY'
,p_display_name=>'Span Horizontally'
,p_display_sequence=>70
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--spanHorizontally'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9803891510688069)
,p_theme_id=>42
,p_name=>'FLOAT'
,p_display_name=>'Float'
,p_display_sequence=>60
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--float'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9804041375688069)
,p_theme_id=>42
,p_name=>'2_COLUMNS'
,p_display_name=>'2 Columns'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9804253065688069)
,p_theme_id=>42
,p_name=>'3_COLUMNS'
,p_display_name=>'3 Columns'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--3cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9804422132688069)
,p_theme_id=>42
,p_name=>'4_COLUMNS'
,p_display_name=>'4 Columns'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--4cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9804676181688070)
,p_theme_id=>42
,p_name=>'5_COLUMNS'
,p_display_name=>'5 Columns'
,p_display_sequence=>50
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--5cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9804859994688070)
,p_theme_id=>42
,p_name=>'FEATURED'
,p_display_name=>'Featured'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--featured force-fa-lg'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9805021342688070)
,p_theme_id=>42
,p_name=>'BASIC'
,p_display_name=>'Basic'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--basic'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
);
end;
/
begin
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9805292802688070)
,p_theme_id=>42
,p_name=>'USE_THEME_COLORS'
,p_display_name=>'Apply Theme Colors'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'u-colors'
,p_template_types=>'LIST'
,p_help_text=>'Applies the colors from the theme''s color palette to the icons or initials within cards.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9805601302688070)
,p_theme_id=>42
,p_name=>'DISPLAY_ICONS'
,p_display_name=>'Display Icons'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--displayIcons'
,p_group_id=>wwv_flow_api.id(9805405815688070)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9805851161688071)
,p_theme_id=>42
,p_name=>'DISPLAY_INITIALS'
,p_display_name=>'Display Initials'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--displayInitials'
,p_group_id=>wwv_flow_api.id(9805405815688070)
,p_template_types=>'LIST'
,p_help_text=>'Initials come from List Attribute 3'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9806238285688071)
,p_theme_id=>42
,p_name=>'2_LINES'
,p_display_name=>'2 Lines'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--desc-2ln'
,p_group_id=>wwv_flow_api.id(9806089747688071)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9806411071688071)
,p_theme_id=>42
,p_name=>'3_LINES'
,p_display_name=>'3 Lines'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--desc-3ln'
,p_group_id=>wwv_flow_api.id(9806089747688071)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9806697015688071)
,p_theme_id=>42
,p_name=>'4_LINES'
,p_display_name=>'4 Lines'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--desc-4ln'
,p_group_id=>wwv_flow_api.id(9806089747688071)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9806882666688071)
,p_theme_id=>42
,p_name=>'COMPACT'
,p_display_name=>'Compact'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--compact'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
,p_help_text=>'Use this option when you want to show smaller cards.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9807058855688071)
,p_theme_id=>42
,p_name=>'HIDDEN_BODY_TEXT'
,p_display_name=>'Hidden'
,p_display_sequence=>50
,p_list_template_id=>wwv_flow_api.id(9801570396688067)
,p_css_classes=>'t-Cards--hideBody'
,p_group_id=>wwv_flow_api.id(9806089747688071)
,p_template_types=>'LIST'
,p_help_text=>'This option hides the card body which contains description and subtext.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9807608472688072)
,p_theme_id=>42
,p_name=>'SHOWICONS'
,p_display_name=>'For All Items'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9807187050688071)
,p_css_classes=>'t-LinksList--showIcons'
,p_group_id=>wwv_flow_api.id(9807457363688072)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9807881833688072)
,p_theme_id=>42
,p_name=>'SHOWGOTOARROW'
,p_display_name=>'Show Right Arrow'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9807187050688071)
,p_css_classes=>'t-LinksList--showArrow'
,p_template_types=>'LIST'
,p_help_text=>'Show arrow to the right of link'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9808025137688072)
,p_theme_id=>42
,p_name=>'DISABLETEXTWRAPPING'
,p_display_name=>'Disable Text Wrapping'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9807187050688071)
,p_css_classes=>'t-LinksList--nowrap'
,p_template_types=>'LIST'
,p_help_text=>'Do not allow link text to wrap to new lines. Truncate with ellipsis.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9808200995688072)
,p_theme_id=>42
,p_name=>'SHOWBADGES'
,p_display_name=>'Show Badges'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9807187050688071)
,p_css_classes=>'t-LinksList--showBadge'
,p_template_types=>'LIST'
,p_help_text=>'Show badge to right of link (requires Attribute 1 to be populated)'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9808460697688073)
,p_theme_id=>42
,p_name=>'SHOWTOPICONS'
,p_display_name=>'For Top Level Items Only'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9807187050688071)
,p_css_classes=>'t-LinksList--showTopIcons'
,p_group_id=>wwv_flow_api.id(9807457363688072)
,p_template_types=>'LIST'
,p_help_text=>'This will show icons for top level items of the list only. It will not show icons for sub lists.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9808616972688073)
,p_theme_id=>42
,p_name=>'ACTIONS'
,p_display_name=>'Actions'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9807187050688071)
,p_css_classes=>'t-LinksList--actions'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
,p_help_text=>'Render as actions to be placed on the right side column.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9809016498688073)
,p_theme_id=>42
,p_name=>'SPANHORIZONTAL'
,p_display_name=>'Span Horizontal'
,p_display_sequence=>50
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'t-MediaList--horizontal'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_help_text=>'Show all list items in one horizontal row.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9809294843688073)
,p_theme_id=>42
,p_name=>'2COLUMNGRID'
,p_display_name=>'2 Column Grid'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'t-MediaList--cols t-MediaList--2cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9809404359688074)
,p_theme_id=>42
,p_name=>'3COLUMNGRID'
,p_display_name=>'3 Column Grid'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'t-MediaList--cols t-MediaList--3cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9809680521688074)
,p_theme_id=>42
,p_name=>'4COLUMNGRID'
,p_display_name=>'4 Column Grid'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'t-MediaList--cols t-MediaList--4cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9809887046688074)
,p_theme_id=>42
,p_name=>'5COLUMNGRID'
,p_display_name=>'5 Column Grid'
,p_display_sequence=>40
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'t-MediaList--cols t-MediaList--5cols'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9810007517688074)
,p_theme_id=>42
,p_name=>'ICONS_SQUARE'
,p_display_name=>'Square'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'t-MediaList--iconsSquare'
,p_group_id=>wwv_flow_api.id(9802696520688068)
,p_template_types=>'LIST'
,p_help_text=>'The icons are displayed within a square shape.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9810265284688074)
,p_theme_id=>42
,p_name=>'ICONS_ROUNDED'
,p_display_name=>'Rounded Corners'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'t-MediaList--iconsRounded'
,p_group_id=>wwv_flow_api.id(9802696520688068)
,p_template_types=>'LIST'
,p_help_text=>'The icons are displayed within a square with rounded corners.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9810402263688074)
,p_theme_id=>42
,p_name=>'APPLY_THEME_COLORS'
,p_display_name=>'Apply Theme Colors'
,p_display_sequence=>40
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'u-colors'
,p_template_types=>'LIST'
,p_help_text=>'Applies colors from the Theme''s color palette to icons in the list.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9810808142688075)
,p_theme_id=>42
,p_name=>'LIST_SIZE_LARGE'
,p_display_name=>'Large'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'t-MediaList--large force-fa-lg'
,p_group_id=>wwv_flow_api.id(9810649159688075)
,p_template_types=>'LIST'
,p_help_text=>'Increases the size of the text and icons in the list.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9811031147688075)
,p_theme_id=>42
,p_name=>'SHOW_ICONS'
,p_display_name=>'Show Icons'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'t-MediaList--showIcons'
,p_template_types=>'LIST'
,p_help_text=>'Display an icon next to the list item.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9811285349688075)
,p_theme_id=>42
,p_name=>'SHOW_DESCRIPTION'
,p_display_name=>'Show Description'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'t-MediaList--showDesc'
,p_template_types=>'LIST'
,p_help_text=>'Shows the description (Attribute 1) for each list item.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9811447334688075)
,p_theme_id=>42
,p_name=>'SHOW_BADGES'
,p_display_name=>'Show Badges'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9808756458688073)
,p_css_classes=>'t-MediaList--showBadges'
,p_template_types=>'LIST'
,p_help_text=>'Show a badge (Attribute 2) to the right of the list item.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9811860641688076)
,p_theme_id=>42
,p_name=>'ADD_ACTIONS'
,p_display_name=>'Add Actions'
,p_display_sequence=>40
,p_list_template_id=>wwv_flow_api.id(9811531114688075)
,p_css_classes=>'js-addActions'
,p_template_types=>'LIST'
,p_help_text=>'Use this option to add shortcuts for menu items. Note that actions.js must be included on your page to support this functionality.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9812089364688076)
,p_theme_id=>42
,p_name=>'BEHAVE_LIKE_TABS'
,p_display_name=>'Behave Like Tabs'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9811531114688075)
,p_css_classes=>'js-tabLike'
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9812226664688076)
,p_theme_id=>42
,p_name=>'ENABLE_SLIDE_ANIMATION'
,p_display_name=>'Enable Slide Animation'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9811531114688075)
,p_css_classes=>'js-slide'
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9812435288688076)
,p_theme_id=>42
,p_name=>'SHOW_SUB_MENU_ICONS'
,p_display_name=>'Show Sub Menu Icons'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9811531114688075)
,p_css_classes=>'js-showSubMenuIcons'
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9812822197688077)
,p_theme_id=>42
,p_name=>'ADD_ACTIONS'
,p_display_name=>'Add Actions'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9812503983688076)
,p_css_classes=>'js-addActions'
,p_template_types=>'LIST'
,p_help_text=>'Enables you to define a keyboard shortcut to activate the menu item.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9813454860688078)
,p_theme_id=>42
,p_name=>'STYLE_A'
,p_display_name=>'Style A'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9813182182688077)
,p_css_classes=>'t-TreeNav--styleA'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
,p_help_text=>'Style Variation A'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9813692256688078)
,p_theme_id=>42
,p_name=>'STYLE_B'
,p_display_name=>'Style B'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9813182182688077)
,p_css_classes=>'t-TreeNav--styleB'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
,p_help_text=>'Style Variation B'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9813840946688078)
,p_theme_id=>42
,p_name=>'STYLE_C'
,p_display_name=>'Classic'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9813182182688077)
,p_css_classes=>'t-TreeNav--classic'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
,p_help_text=>'Classic Style'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9814000820688078)
,p_theme_id=>42
,p_name=>'COLLAPSED_DEFAULT'
,p_display_name=>'Collapsed by Default'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9813182182688077)
,p_css_classes=>'js-defaultCollapsed'
,p_template_types=>'LIST'
,p_help_text=>'This option will load the side navigation menu in a collapsed state by default.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9814432349688079)
,p_theme_id=>42
,p_name=>'LARGE'
,p_display_name=>'Large'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9814107555688078)
,p_css_classes=>'t-Tabs--large'
,p_group_id=>wwv_flow_api.id(9810649159688075)
,p_template_types=>'LIST'
,p_help_text=>'Increases font size and white space around tab items.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9814662327688079)
,p_theme_id=>42
,p_name=>'SIMPLE'
,p_display_name=>'Simple'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9814107555688078)
,p_css_classes=>'t-Tabs--simple'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
,p_help_text=>'A very simplistic tab UI.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9814879225688079)
,p_theme_id=>42
,p_name=>'PILL'
,p_display_name=>'Pill'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9814107555688078)
,p_css_classes=>'t-Tabs--pill'
,p_group_id=>wwv_flow_api.id(9801042467688067)
,p_template_types=>'LIST'
,p_help_text=>'Displays tabs in a pill container.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9815088323688079)
,p_theme_id=>42
,p_name=>'INLINE_WITH_LABEL'
,p_display_name=>'Inline with Label'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9814107555688078)
,p_css_classes=>'t-Tabs--inlineIcons'
,p_group_id=>wwv_flow_api.id(9805405815688070)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9815272431688080)
,p_theme_id=>42
,p_name=>'ABOVE_LABEL'
,p_display_name=>'Above Label'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9814107555688078)
,p_css_classes=>'t-Tabs--iconsAbove'
,p_group_id=>wwv_flow_api.id(9805405815688070)
,p_template_types=>'LIST'
,p_help_text=>'Places icons above tab label.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9815480784688080)
,p_theme_id=>42
,p_name=>'FILL_LABELS'
,p_display_name=>'Fill Labels'
,p_display_sequence=>1
,p_list_template_id=>wwv_flow_api.id(9814107555688078)
,p_css_classes=>'t-Tabs--fillLabels'
,p_group_id=>wwv_flow_api.id(9797800158688064)
,p_template_types=>'LIST'
,p_help_text=>'Stretch tabs to fill to the width of the tabs container.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9815692799688080)
,p_theme_id=>42
,p_name=>'SMALL'
,p_display_name=>'Small'
,p_display_sequence=>5
,p_list_template_id=>wwv_flow_api.id(9814107555688078)
,p_css_classes=>'t-Tabs--small'
,p_group_id=>wwv_flow_api.id(9810649159688075)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9816056301688080)
,p_theme_id=>42
,p_name=>'ADD_ACTIONS'
,p_display_name=>'Add Actions'
,p_display_sequence=>1
,p_list_template_id=>wwv_flow_api.id(9815734538688080)
,p_css_classes=>'js-addActions'
,p_template_types=>'LIST'
,p_help_text=>'Use this option to add shortcuts for menu items. Note that actions.js must be included on your page to support this functionality.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9816208157688080)
,p_theme_id=>42
,p_name=>'BEHAVE_LIKE_TABS'
,p_display_name=>'Behave Like Tabs'
,p_display_sequence=>1
,p_list_template_id=>wwv_flow_api.id(9815734538688080)
,p_css_classes=>'js-tabLike'
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9816448379688081)
,p_theme_id=>42
,p_name=>'ENABLE_SLIDE_ANIMATION'
,p_display_name=>'Enable Slide Animation'
,p_display_sequence=>1
,p_list_template_id=>wwv_flow_api.id(9815734538688080)
,p_css_classes=>'js-slide'
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9816629052688081)
,p_theme_id=>42
,p_name=>'SHOW_SUB_MENU_ICONS'
,p_display_name=>'Show Sub Menu Icons'
,p_display_sequence=>1
,p_list_template_id=>wwv_flow_api.id(9815734538688080)
,p_css_classes=>'js-showSubMenuIcons'
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9817296613688081)
,p_theme_id=>42
,p_name=>'LABEL_INLINE_LG'
,p_display_name=>'Display labels inline'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9816752314688081)
,p_css_classes=>'t-NavTabs--inlineLabels-lg'
,p_group_id=>wwv_flow_api.id(9817056740688081)
,p_template_types=>'LIST'
,p_help_text=>'Display the label inline with the icon and badge'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9817437067688082)
,p_theme_id=>42
,p_name=>'LABEL_ABOVE_LG'
,p_display_name=>'Display labels above'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9816752314688081)
,p_css_classes=>'t-NavTabs--stacked'
,p_group_id=>wwv_flow_api.id(9817056740688081)
,p_template_types=>'LIST'
,p_help_text=>'Display the label stacked above the icon and badge'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9817690905688082)
,p_theme_id=>42
,p_name=>'NO_LABEL_LG'
,p_display_name=>'Do not display labels'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9816752314688081)
,p_css_classes=>'t-NavTabs--hiddenLabels-lg'
,p_group_id=>wwv_flow_api.id(9817056740688081)
,p_template_types=>'LIST'
,p_help_text=>'Hides the label for the list item'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9818046536688082)
,p_theme_id=>42
,p_name=>'DISPLAY_LABELS_SM'
,p_display_name=>'Display labels'
,p_display_sequence=>40
,p_list_template_id=>wwv_flow_api.id(9816752314688081)
,p_css_classes=>'t-NavTabs--displayLabels-sm'
,p_group_id=>wwv_flow_api.id(9817843155688082)
,p_template_types=>'LIST'
,p_help_text=>'Displays the label for the list items below the icon'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9818291089688082)
,p_theme_id=>42
,p_name=>'HIDE_LABELS_SM'
,p_display_name=>'Do not display labels'
,p_display_sequence=>50
,p_list_template_id=>wwv_flow_api.id(9816752314688081)
,p_css_classes=>'t-NavTabs--hiddenLabels-sm'
,p_group_id=>wwv_flow_api.id(9817843155688082)
,p_template_types=>'LIST'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9818842819688083)
,p_theme_id=>42
,p_name=>'ALLSTEPS'
,p_display_name=>'All Steps'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9818313839688082)
,p_css_classes=>'t-WizardSteps--displayLabels'
,p_group_id=>wwv_flow_api.id(9818601323688083)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9819040272688083)
,p_theme_id=>42
,p_name=>'CURRENTSTEPONLY'
,p_display_name=>'Current Step Only'
,p_display_sequence=>20
,p_list_template_id=>wwv_flow_api.id(9818313839688082)
,p_css_classes=>'t-WizardSteps--displayCurrentLabelOnly'
,p_group_id=>wwv_flow_api.id(9818601323688083)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9819262329688083)
,p_theme_id=>42
,p_name=>'HIDELABELS'
,p_display_name=>'Hide Labels'
,p_display_sequence=>30
,p_list_template_id=>wwv_flow_api.id(9818313839688082)
,p_css_classes=>'t-WizardSteps--hideLabels'
,p_group_id=>wwv_flow_api.id(9818601323688083)
,p_template_types=>'LIST'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9819482369688083)
,p_theme_id=>42
,p_name=>'WIZARD_PROGRESS_LINKS'
,p_display_name=>'Make Wizard Steps Clickable'
,p_display_sequence=>40
,p_list_template_id=>wwv_flow_api.id(9818313839688082)
,p_css_classes=>'js-wizardProgressLinks'
,p_template_types=>'LIST'
,p_help_text=>'This option will make the wizard steps clickable links.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9819694631688083)
,p_theme_id=>42
,p_name=>'VERTICAL_LIST'
,p_display_name=>'Vertical Orientation'
,p_display_sequence=>10
,p_list_template_id=>wwv_flow_api.id(9818313839688082)
,p_css_classes=>'t-WizardSteps--vertical'
,p_template_types=>'LIST'
,p_help_text=>'Displays the wizard progress list in a vertical orientation and is suitable for displaying within a side column of a page.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9820862888688095)
,p_theme_id=>42
,p_name=>'SPIN'
,p_display_name=>'Spin'
,p_display_sequence=>10
,p_button_template_id=>wwv_flow_api.id(9820400204688092)
,p_css_classes=>'t-Button--hoverIconSpin'
,p_group_id=>wwv_flow_api.id(9820691839688095)
,p_template_types=>'BUTTON'
,p_help_text=>'The icon will spin on button hover or focus.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9821095010688096)
,p_theme_id=>42
,p_name=>'PUSH'
,p_display_name=>'Push'
,p_display_sequence=>20
,p_button_template_id=>wwv_flow_api.id(9820400204688092)
,p_css_classes=>'t-Button--hoverIconPush'
,p_group_id=>wwv_flow_api.id(9820691839688095)
,p_template_types=>'BUTTON'
,p_help_text=>'The icon will animate to the right or left on button hover or focus.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9821654312688096)
,p_theme_id=>42
,p_name=>'LEFTICON'
,p_display_name=>'Left'
,p_display_sequence=>10
,p_button_template_id=>wwv_flow_api.id(9821219757688096)
,p_css_classes=>'t-Button--iconLeft'
,p_group_id=>wwv_flow_api.id(9821466696688096)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9821886506688096)
,p_theme_id=>42
,p_name=>'RIGHTICON'
,p_display_name=>'Right'
,p_display_sequence=>20
,p_button_template_id=>wwv_flow_api.id(9821219757688096)
,p_css_classes=>'t-Button--iconRight'
,p_group_id=>wwv_flow_api.id(9821466696688096)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9822027776688097)
,p_theme_id=>42
,p_name=>'HIDE_LABEL_ON_MOBILE'
,p_display_name=>'Hide Label on Mobile'
,p_display_sequence=>10
,p_button_template_id=>wwv_flow_api.id(9821219757688096)
,p_css_classes=>'t-Button--mobileHideLabel'
,p_template_types=>'BUTTON'
,p_help_text=>'This template options hides the button label on small screens.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9822242723688097)
,p_theme_id=>42
,p_name=>'SPIN'
,p_display_name=>'Spin'
,p_display_sequence=>10
,p_button_template_id=>wwv_flow_api.id(9821219757688096)
,p_css_classes=>'t-Button--hoverIconSpin'
,p_group_id=>wwv_flow_api.id(9820691839688095)
,p_template_types=>'BUTTON'
,p_help_text=>'The icon will spin on button hover or focus.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9822400869688097)
,p_theme_id=>42
,p_name=>'PUSH'
,p_display_name=>'Push'
,p_display_sequence=>20
,p_button_template_id=>wwv_flow_api.id(9821219757688096)
,p_css_classes=>'t-Button--hoverIconPush'
,p_group_id=>wwv_flow_api.id(9820691839688095)
,p_template_types=>'BUTTON'
,p_help_text=>'The icon will animate to the right or left on button hover or focus.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9824314968688170)
,p_theme_id=>42
,p_name=>'PRIMARY'
,p_display_name=>'Primary'
,p_display_sequence=>10
,p_css_classes=>'t-Button--primary'
,p_group_id=>wwv_flow_api.id(9824141954688169)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9824760081688171)
,p_theme_id=>42
,p_name=>'STRETCH'
,p_display_name=>'Stretch'
,p_display_sequence=>10
,p_css_classes=>'t-Button--stretch'
,p_group_id=>wwv_flow_api.id(9824530443688170)
,p_template_types=>'BUTTON'
,p_help_text=>'Stretches button to fill container'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9824945550688171)
,p_theme_id=>42
,p_name=>'DANGER'
,p_display_name=>'Danger'
,p_display_sequence=>30
,p_css_classes=>'t-Button--danger'
,p_group_id=>wwv_flow_api.id(9824141954688169)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9825125838688171)
,p_theme_id=>42
,p_name=>'SUCCESS'
,p_display_name=>'Success'
,p_display_sequence=>40
,p_css_classes=>'t-Button--success'
,p_group_id=>wwv_flow_api.id(9824141954688169)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9825513088688172)
,p_theme_id=>42
,p_name=>'NOUI'
,p_display_name=>'Remove UI Decoration'
,p_display_sequence=>20
,p_css_classes=>'t-Button--noUI'
,p_group_id=>wwv_flow_api.id(9825393341688171)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9825997146688172)
,p_theme_id=>42
,p_name=>'LARGE'
,p_display_name=>'Large'
,p_display_sequence=>30
,p_css_classes=>'t-Button--large'
,p_group_id=>wwv_flow_api.id(9825760804688172)
,p_template_types=>'BUTTON'
,p_help_text=>'A large button.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9826336899688172)
,p_theme_id=>42
,p_name=>'SMALLLEFTMARGIN'
,p_display_name=>'Small'
,p_display_sequence=>10
,p_css_classes=>'t-Button--padLeft'
,p_group_id=>wwv_flow_api.id(9826159905688172)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9826516359688172)
,p_theme_id=>42
,p_name=>'SMALL'
,p_display_name=>'Small'
,p_display_sequence=>20
,p_css_classes=>'t-Button--small'
,p_group_id=>wwv_flow_api.id(9825760804688172)
,p_template_types=>'BUTTON'
,p_help_text=>'A small button.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9826786233688172)
,p_theme_id=>42
,p_name=>'WARNING'
,p_display_name=>'Warning'
,p_display_sequence=>20
,p_css_classes=>'t-Button--warning'
,p_group_id=>wwv_flow_api.id(9824141954688169)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9826982252688173)
,p_theme_id=>42
,p_name=>'SIMPLE'
,p_display_name=>'Simple'
,p_display_sequence=>10
,p_css_classes=>'t-Button--simple'
,p_group_id=>wwv_flow_api.id(9825393341688171)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9827199921688173)
,p_theme_id=>42
,p_name=>'LARGELEFTMARGIN'
,p_display_name=>'Large'
,p_display_sequence=>20
,p_css_classes=>'t-Button--gapLeft'
,p_group_id=>wwv_flow_api.id(9826159905688172)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9827549971688173)
,p_theme_id=>42
,p_name=>'SMALLRIGHTMARGIN'
,p_display_name=>'Small'
,p_display_sequence=>10
,p_css_classes=>'t-Button--padRight'
,p_group_id=>wwv_flow_api.id(9827306136688173)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9827761706688173)
,p_theme_id=>42
,p_name=>'LARGERIGHTMARGIN'
,p_display_name=>'Large'
,p_display_sequence=>20
,p_css_classes=>'t-Button--gapRight'
,p_group_id=>wwv_flow_api.id(9827306136688173)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9828114114688173)
,p_theme_id=>42
,p_name=>'PILLSTART'
,p_display_name=>'First Button'
,p_display_sequence=>10
,p_css_classes=>'t-Button--pillStart'
,p_group_id=>wwv_flow_api.id(9827970714688173)
,p_template_types=>'BUTTON'
,p_help_text=>'Use this for the start of a pill button.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9828339712688174)
,p_theme_id=>42
,p_name=>'PILL'
,p_display_name=>'Inner Button'
,p_display_sequence=>20
,p_css_classes=>'t-Button--pill'
,p_group_id=>wwv_flow_api.id(9827970714688173)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9828510686688174)
,p_theme_id=>42
,p_name=>'PILLEND'
,p_display_name=>'Last Button'
,p_display_sequence=>30
,p_css_classes=>'t-Button--pillEnd'
,p_group_id=>wwv_flow_api.id(9827970714688173)
,p_template_types=>'BUTTON'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9828937398688174)
,p_theme_id=>42
,p_name=>'FORMLEFTLABELS'
,p_display_name=>'Left'
,p_display_sequence=>20
,p_css_classes=>'t-Form--leftLabels'
,p_group_id=>wwv_flow_api.id(9828709506688174)
,p_template_types=>'REGION'
,p_help_text=>'Align form labels to left.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9829370631688174)
,p_theme_id=>42
,p_name=>'FORMSIZELARGE'
,p_display_name=>'Large'
,p_display_sequence=>10
,p_css_classes=>'t-Form--large'
,p_group_id=>wwv_flow_api.id(9829158305688174)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9829521046688176)
,p_theme_id=>42
,p_name=>'FORMSIZEXLARGE'
,p_display_name=>'X Large'
,p_display_sequence=>20
,p_css_classes=>'t-Form--xlarge'
,p_group_id=>wwv_flow_api.id(9829158305688174)
,p_template_types=>'REGION'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9829947668688176)
,p_theme_id=>42
,p_name=>'FORMSLIMPADDING'
,p_display_name=>'Slim Padding'
,p_display_sequence=>10
,p_css_classes=>'t-Form--slimPadding'
,p_group_id=>wwv_flow_api.id(9829723762688176)
,p_template_types=>'REGION'
,p_help_text=>'Reduces form item padding to 4px.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9830189735688176)
,p_theme_id=>42
,p_name=>'FORMREMOVEPADDING'
,p_display_name=>'Remove Padding'
,p_display_sequence=>20
,p_css_classes=>'t-Form--noPadding'
,p_group_id=>wwv_flow_api.id(9829723762688176)
,p_template_types=>'REGION'
,p_help_text=>'Removes padding between items.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9830594362688177)
,p_theme_id=>42
,p_name=>'SHOWFORMLABELSABOVE'
,p_display_name=>'Show Form Labels Above'
,p_display_sequence=>10
,p_css_classes=>'t-Form--labelsAbove'
,p_group_id=>wwv_flow_api.id(9830364893688176)
,p_template_types=>'REGION'
,p_help_text=>'Show form labels above input fields.'
,p_is_advanced=>'N'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9830931929688177)
,p_theme_id=>42
,p_name=>'STRETCH_FORM_FIELDS'
,p_display_name=>'Stretch Form Fields'
,p_display_sequence=>10
,p_css_classes=>'t-Form--stretchInputs'
,p_group_id=>wwv_flow_api.id(9830779259688177)
,p_template_types=>'REGION'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9831308641688177)
,p_theme_id=>42
,p_name=>'PRE_TEXT_BLOCK'
,p_display_name=>'Display as Block'
,p_display_sequence=>10
,p_css_classes=>'t-Form-fieldContainer--preTextBlock'
,p_group_id=>wwv_flow_api.id(9831175250688177)
,p_template_types=>'FIELD'
,p_help_text=>'Displays the Item Pre Text in a block style immediately before the item.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9831731310688177)
,p_theme_id=>42
,p_name=>'POST_TEXT_BLOCK'
,p_display_name=>'Display as Block'
,p_display_sequence=>10
,p_css_classes=>'t-Form-fieldContainer--postTextBlock'
,p_group_id=>wwv_flow_api.id(9831512153688177)
,p_template_types=>'FIELD'
,p_help_text=>'Displays the Item Post Text in a block style immediately after the item.'
);
end;
/
begin
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9832156427688178)
,p_theme_id=>42
,p_name=>'RTM_NONE'
,p_display_name=>'None'
,p_display_sequence=>10
,p_css_classes=>'margin-top-none'
,p_group_id=>wwv_flow_api.id(9831954394688177)
,p_template_types=>'REGION'
,p_help_text=>'Removes the top margin for this region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9832309656688178)
,p_theme_id=>42
,p_name=>'RTM_SMALL'
,p_display_name=>'Small'
,p_display_sequence=>20
,p_css_classes=>'margin-top-sm'
,p_group_id=>wwv_flow_api.id(9831954394688177)
,p_template_types=>'REGION'
,p_help_text=>'Adds a small top margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9832595939688178)
,p_theme_id=>42
,p_name=>'RTM_MEDIUM'
,p_display_name=>'Medium'
,p_display_sequence=>30
,p_css_classes=>'margin-top-md'
,p_group_id=>wwv_flow_api.id(9831954394688177)
,p_template_types=>'REGION'
,p_help_text=>'Adds a medium top margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9832732359688178)
,p_theme_id=>42
,p_name=>'RTM_LARGE'
,p_display_name=>'Large'
,p_display_sequence=>40
,p_css_classes=>'margin-top-lg'
,p_group_id=>wwv_flow_api.id(9831954394688177)
,p_template_types=>'REGION'
,p_help_text=>'Adds a large top margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9833199897688178)
,p_theme_id=>42
,p_name=>'RBM_NONE'
,p_display_name=>'None'
,p_display_sequence=>10
,p_css_classes=>'margin-bottom-none'
,p_group_id=>wwv_flow_api.id(9832946681688178)
,p_template_types=>'REGION'
,p_help_text=>'Removes the bottom margin for this region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9833304672688178)
,p_theme_id=>42
,p_name=>'RBM_SMALL'
,p_display_name=>'Small'
,p_display_sequence=>20
,p_css_classes=>'margin-bottom-sm'
,p_group_id=>wwv_flow_api.id(9832946681688178)
,p_template_types=>'REGION'
,p_help_text=>'Adds a small bottom margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9833597141688179)
,p_theme_id=>42
,p_name=>'RBM_MEDIUM'
,p_display_name=>'Medium'
,p_display_sequence=>30
,p_css_classes=>'margin-bottom-md'
,p_group_id=>wwv_flow_api.id(9832946681688178)
,p_template_types=>'REGION'
,p_help_text=>'Adds a medium bottom margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9833753775688179)
,p_theme_id=>42
,p_name=>'RBM_LARGE'
,p_display_name=>'Large'
,p_display_sequence=>40
,p_css_classes=>'margin-bottom-lg'
,p_group_id=>wwv_flow_api.id(9832946681688178)
,p_template_types=>'REGION'
,p_help_text=>'Adds a large bottom margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9834185110688179)
,p_theme_id=>42
,p_name=>'RRM_NONE'
,p_display_name=>'None'
,p_display_sequence=>10
,p_css_classes=>'margin-right-none'
,p_group_id=>wwv_flow_api.id(9833957878688179)
,p_template_types=>'REGION'
,p_help_text=>'Removes the right margin from the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9834328256688179)
,p_theme_id=>42
,p_name=>'RRM_SMALL'
,p_display_name=>'Small'
,p_display_sequence=>20
,p_css_classes=>'margin-right-sm'
,p_group_id=>wwv_flow_api.id(9833957878688179)
,p_template_types=>'REGION'
,p_help_text=>'Adds a small right margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9834560617688180)
,p_theme_id=>42
,p_name=>'RRM_MEDIUM'
,p_display_name=>'Medium'
,p_display_sequence=>30
,p_css_classes=>'margin-right-md'
,p_group_id=>wwv_flow_api.id(9833957878688179)
,p_template_types=>'REGION'
,p_help_text=>'Adds a medium right margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9834761578688180)
,p_theme_id=>42
,p_name=>'RRM_LARGE'
,p_display_name=>'Large'
,p_display_sequence=>40
,p_css_classes=>'margin-right-lg'
,p_group_id=>wwv_flow_api.id(9833957878688179)
,p_template_types=>'REGION'
,p_help_text=>'Adds a large right margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9835165791688180)
,p_theme_id=>42
,p_name=>'RLM_NONE'
,p_display_name=>'None'
,p_display_sequence=>10
,p_css_classes=>'margin-left-none'
,p_group_id=>wwv_flow_api.id(9834905706688180)
,p_template_types=>'REGION'
,p_help_text=>'Removes the left margin from the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9835335069688180)
,p_theme_id=>42
,p_name=>'RLM_SMALL'
,p_display_name=>'Small'
,p_display_sequence=>20
,p_css_classes=>'margin-left-sm'
,p_group_id=>wwv_flow_api.id(9834905706688180)
,p_template_types=>'REGION'
,p_help_text=>'Adds a small left margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9835591418688180)
,p_theme_id=>42
,p_name=>'RLM_MEDIUM'
,p_display_name=>'Medium'
,p_display_sequence=>30
,p_css_classes=>'margin-left-md'
,p_group_id=>wwv_flow_api.id(9834905706688180)
,p_template_types=>'REGION'
,p_help_text=>'Adds a medium right margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9835770091688180)
,p_theme_id=>42
,p_name=>'RLM_LARGE'
,p_display_name=>'Large'
,p_display_sequence=>40
,p_css_classes=>'margin-left-lg'
,p_group_id=>wwv_flow_api.id(9834905706688180)
,p_template_types=>'REGION'
,p_help_text=>'Adds a large right margin to the region.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9836148568688181)
,p_theme_id=>42
,p_name=>'HIDE_WHEN_ALL_ROWS_DISPLAYED'
,p_display_name=>'Hide when all rows displayed'
,p_display_sequence=>10
,p_css_classes=>'t-Report--hideNoPagination'
,p_group_id=>wwv_flow_api.id(9835973671688181)
,p_template_types=>'REPORT'
,p_help_text=>'This option will hide the pagination when all rows are displayed.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9836327675688181)
,p_theme_id=>42
,p_name=>'DISPLAY_AS_LINK'
,p_display_name=>'Display as Link'
,p_display_sequence=>30
,p_css_classes=>'t-Button--link'
,p_group_id=>wwv_flow_api.id(9825393341688171)
,p_template_types=>'BUTTON'
,p_help_text=>'This option makes the button appear as a text link.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9836721150688181)
,p_theme_id=>42
,p_name=>'SMALLTOPMARGIN'
,p_display_name=>'Small'
,p_display_sequence=>10
,p_css_classes=>'t-Button--padTop'
,p_group_id=>wwv_flow_api.id(9836597146688181)
,p_template_types=>'BUTTON'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9836965032688181)
,p_theme_id=>42
,p_name=>'LARGETOPMARGIN'
,p_display_name=>'Large'
,p_display_sequence=>20
,p_css_classes=>'t-Button--gapTop'
,p_group_id=>wwv_flow_api.id(9836597146688181)
,p_template_types=>'BUTTON'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9837315408688182)
,p_theme_id=>42
,p_name=>'SMALLBOTTOMMARGIN'
,p_display_name=>'Small'
,p_display_sequence=>10
,p_css_classes=>'t-Button--padBottom'
,p_group_id=>wwv_flow_api.id(9837176826688181)
,p_template_types=>'BUTTON'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9837573033688182)
,p_theme_id=>42
,p_name=>'LARGEBOTTOMMARGIN'
,p_display_name=>'Large'
,p_display_sequence=>20
,p_css_classes=>'t-Button--gapBottom'
,p_group_id=>wwv_flow_api.id(9837176826688181)
,p_template_types=>'BUTTON'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9837769223688182)
,p_theme_id=>42
,p_name=>'TINY'
,p_display_name=>'Tiny'
,p_display_sequence=>10
,p_css_classes=>'t-Button--tiny'
,p_group_id=>wwv_flow_api.id(9825760804688172)
,p_template_types=>'BUTTON'
,p_help_text=>'A very small button.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9838191592688182)
,p_theme_id=>42
,p_name=>'DISPLAY_AS_PILL_BUTTON'
,p_display_name=>'Display as Pill Button'
,p_display_sequence=>10
,p_css_classes=>'t-Form-fieldContainer--radioButtonGroup'
,p_group_id=>wwv_flow_api.id(9837978206688182)
,p_template_types=>'FIELD'
,p_help_text=>'Displays the radio buttons to look like a button set / pill button.  Note that the the radio buttons must all be in the same row for this option to work.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9838574049688183)
,p_theme_id=>42
,p_name=>'LARGE_FIELD'
,p_display_name=>'Large'
,p_display_sequence=>10
,p_css_classes=>'t-Form-fieldContainer--large'
,p_group_id=>wwv_flow_api.id(9838309887688183)
,p_template_types=>'FIELD'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9838748934688183)
,p_theme_id=>42
,p_name=>'X_LARGE_SIZE'
,p_display_name=>'X Large'
,p_display_sequence=>20
,p_css_classes=>'t-Form-fieldContainer--xlarge'
,p_group_id=>wwv_flow_api.id(9838309887688183)
,p_template_types=>'FIELD'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9838997814688183)
,p_theme_id=>42
,p_name=>'STRETCH_FORM_ITEM'
,p_display_name=>'Stretch Form Item'
,p_display_sequence=>10
,p_css_classes=>'t-Form-fieldContainer--stretchInputs'
,p_template_types=>'FIELD'
,p_help_text=>'Stretches the form item to fill its container.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9839384706688183)
,p_theme_id=>42
,p_name=>'FBM_NONE'
,p_display_name=>'None'
,p_display_sequence=>10
,p_css_classes=>'margin-bottom-none'
,p_group_id=>wwv_flow_api.id(9839140797688183)
,p_template_types=>'FIELD'
,p_help_text=>'Removes the bottom margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9839514260688184)
,p_theme_id=>42
,p_name=>'FBM_SMALL'
,p_display_name=>'Small'
,p_display_sequence=>20
,p_css_classes=>'margin-bottom-sm'
,p_group_id=>wwv_flow_api.id(9839140797688183)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a small bottom margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9839745562688184)
,p_theme_id=>42
,p_name=>'FBM_MEDIUM'
,p_display_name=>'Medium'
,p_display_sequence=>30
,p_css_classes=>'margin-bottom-md'
,p_group_id=>wwv_flow_api.id(9839140797688183)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a medium bottom margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9839919901688184)
,p_theme_id=>42
,p_name=>'FBM_LARGE'
,p_display_name=>'Large'
,p_display_sequence=>40
,p_css_classes=>'margin-bottom-lg'
,p_group_id=>wwv_flow_api.id(9839140797688183)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a large bottom margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9840375160688184)
,p_theme_id=>42
,p_name=>'FLM_NONE'
,p_display_name=>'None'
,p_display_sequence=>10
,p_css_classes=>'margin-left-none'
,p_group_id=>wwv_flow_api.id(9840104506688184)
,p_template_types=>'FIELD'
,p_help_text=>'Removes the left margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9840536727688184)
,p_theme_id=>42
,p_name=>'FLM_SMALL'
,p_display_name=>'Small'
,p_display_sequence=>20
,p_css_classes=>'margin-left-sm'
,p_group_id=>wwv_flow_api.id(9840104506688184)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a small left margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9840784754688185)
,p_theme_id=>42
,p_name=>'FLM_MEDIUM'
,p_display_name=>'Medium'
,p_display_sequence=>30
,p_css_classes=>'margin-left-md'
,p_group_id=>wwv_flow_api.id(9840104506688184)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a medium left margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9840918559688185)
,p_theme_id=>42
,p_name=>'FLM_LARGE'
,p_display_name=>'Large'
,p_display_sequence=>40
,p_css_classes=>'margin-left-lg'
,p_group_id=>wwv_flow_api.id(9840104506688184)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a large left margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9841365983688185)
,p_theme_id=>42
,p_name=>'FRM_NONE'
,p_display_name=>'None'
,p_display_sequence=>10
,p_css_classes=>'margin-right-none'
,p_group_id=>wwv_flow_api.id(9841181981688185)
,p_template_types=>'FIELD'
,p_help_text=>'Removes the right margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9841552050688185)
,p_theme_id=>42
,p_name=>'FRM_SMALL'
,p_display_name=>'Small'
,p_display_sequence=>20
,p_css_classes=>'margin-right-sm'
,p_group_id=>wwv_flow_api.id(9841181981688185)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a small right margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9841748106688185)
,p_theme_id=>42
,p_name=>'FRM_MEDIUM'
,p_display_name=>'Medium'
,p_display_sequence=>30
,p_css_classes=>'margin-right-md'
,p_group_id=>wwv_flow_api.id(9841181981688185)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a medium right margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9841963405688186)
,p_theme_id=>42
,p_name=>'FRM_LARGE'
,p_display_name=>'Large'
,p_display_sequence=>40
,p_css_classes=>'margin-right-lg'
,p_group_id=>wwv_flow_api.id(9841181981688185)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a large right margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9842389157688186)
,p_theme_id=>42
,p_name=>'FTM_NONE'
,p_display_name=>'None'
,p_display_sequence=>10
,p_css_classes=>'margin-top-none'
,p_group_id=>wwv_flow_api.id(9842104263688186)
,p_template_types=>'FIELD'
,p_help_text=>'Removes the top margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9842532256688186)
,p_theme_id=>42
,p_name=>'FTM_SMALL'
,p_display_name=>'Small'
,p_display_sequence=>20
,p_css_classes=>'margin-top-sm'
,p_group_id=>wwv_flow_api.id(9842104263688186)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a small top margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9842739472688186)
,p_theme_id=>42
,p_name=>'FTM_MEDIUM'
,p_display_name=>'Medium'
,p_display_sequence=>30
,p_css_classes=>'margin-top-md'
,p_group_id=>wwv_flow_api.id(9842104263688186)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a medium top margin for this field.'
);
wwv_flow_api.create_template_option(
 p_id=>wwv_flow_api.id(9842909415688186)
,p_theme_id=>42
,p_name=>'FTM_LARGE'
,p_display_name=>'Large'
,p_display_sequence=>40
,p_css_classes=>'margin-top-lg'
,p_group_id=>wwv_flow_api.id(9842104263688186)
,p_template_types=>'FIELD'
,p_help_text=>'Adds a large top margin for this field.'
);
end;
/
prompt --application/shared_components/globalization/language
begin
null;
end;
/
prompt --application/shared_components/globalization/translations
begin
null;
end;
/
prompt --application/shared_components/logic/build_options
begin
wwv_flow_api.create_build_option(
 p_id=>wwv_flow_api.id(9845173009688250)
,p_build_option_name=>'Feature: Access Control'
,p_build_option_status=>'INCLUDE'
,p_feature_identifier=>'APPLICATION_ACCESS_CONTROL'
,p_build_option_comment=>'Incorporate role based user authentication within your application and manage username mappings to application roles.'
);
end;
/
prompt --application/shared_components/globalization/messages
begin
null;
end;
/
prompt --application/shared_components/globalization/dyntranslations
begin
null;
end;
/
prompt --application/shared_components/user_interface/shortcuts/delete_confirm_msg
begin
wwv_flow_api.create_shortcut(
 p_id=>wwv_flow_api.id(9847872266688259)
,p_shortcut_name=>'DELETE_CONFIRM_MSG'
,p_shortcut_type=>'TEXT_ESCAPE_JS'
,p_shortcut=>'Would you like to perform this delete action?'
);
end;
/
prompt --application/shared_components/security/authentications/application_express_authentication
begin
wwv_flow_api.create_authentication(
 p_id=>wwv_flow_api.id(9714428553687881)
,p_name=>'Application Express Authentication'
,p_scheme_type=>'NATIVE_APEX_ACCOUNTS'
,p_invalid_session_type=>'LOGIN'
,p_use_secure_cookie_yn=>'N'
,p_ras_mode=>0
);
end;
/
prompt --application/user_interfaces
begin
wwv_flow_api.create_user_interface(
 p_id=>wwv_flow_api.id(9843694399688199)
,p_ui_type_name=>'DESKTOP'
,p_display_name=>'Desktop'
,p_display_seq=>10
,p_use_auto_detect=>false
,p_is_default=>true
,p_theme_id=>42
,p_home_url=>'f?p=&APP_ID.:1:&SESSION.'
,p_login_url=>'f?p=&APP_ID.:LOGIN_DESKTOP:&SESSION.'
,p_theme_style_by_user_pref=>false
,p_global_page_id=>0
,p_navigation_list_id=>wwv_flow_api.id(9715221966687890)
,p_navigation_list_position=>'TOP'
,p_navigation_list_template_id=>wwv_flow_api.id(9815734538688080)
,p_nav_list_template_options=>'#DEFAULT#:js-tabLike'
,p_css_file_urls=>'#APP_IMAGES#app-icon.css?version=#APP_VERSION#'
,p_nav_bar_type=>'LIST'
,p_nav_bar_list_id=>wwv_flow_api.id(9843375564688197)
,p_nav_bar_list_template_id=>wwv_flow_api.id(9812990164688077)
,p_nav_bar_template_options=>'#DEFAULT#'
);
end;
/
prompt --application/user_interfaces/combined_files
begin
null;
end;
/
prompt --application/pages/page_00000
begin
wwv_flow_api.create_page(
 p_id=>0
,p_user_interface_id=>wwv_flow_api.id(9843694399688199)
,p_name=>'Global Page - Desktop'
,p_autocomplete_on_off=>'OFF'
,p_protection_level=>'D'
,p_last_updated_by=>'ADIZOHAR'
,p_last_upd_yyyymmddhh24miss=>'20200506182841'
);
end;
/
prompt --application/pages/page_00001
begin
wwv_flow_api.create_page(
 p_id=>1
,p_user_interface_id=>wwv_flow_api.id(9843694399688199)
,p_name=>'Home'
,p_alias=>'HOME'
,p_step_title=>'OCI Usage and Cost Report'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_last_updated_by=>'ADIZOHAR'
,p_last_upd_yyyymmddhh24miss=>'20210329021046'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9856082202688393)
,p_plug_name=>'OCI Usage and Cost Report'
,p_icon_css_classes=>'app-icon'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>wwv_flow_api.id(9757663101688013)
,p_plug_display_sequence=>10
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
,p_attribute_03=>'Y'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(11933109282191624)
,p_plug_name=>'P1_WELCOME'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11933213511191625)
,p_name=>'P1_WELCOME'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(11933109282191624)
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'PLSQL'
,p_attribute_03=>wwv_flow_string.join(wwv_flow_t_varchar2(
'BEGIN',
'',
'     htp.p(''<H4>Welcome <FONT COLOR="RED">''||:USER||''</FONT> ...<br><br>''||',
'     ''Usage and Cost Reports to Autonomous database''||',
'     ''<br><br>Created by <b>Adi Zohar</b>, Feb 2020-Apr 2021<br><br>''||',
'     ''Application github link = <a target=_new href="https://github.com/oracle/oci-python-sdk/tree/master/examples/usage_reports_to_adw">usage_reports_to_adw</a><br><br>''||',
'     ''Please check as well <a target=_new href="https://github.com/oracle/oci-python-sdk/tree/master/examples/showoci">showoci</a> application<br><br>''||',
unistr('     ''<H6><b>DISCLAIMER \2013 This is not an official Oracle application<b></H6>'''),
'     );',
'',
'END;'))
);
end;
/
prompt --application/pages/page_00002
begin
wwv_flow_api.create_page(
 p_id=>2
,p_user_interface_id=>wwv_flow_api.id(9843694399688199)
,p_name=>'Current State'
,p_step_title=>'Current State'
,p_warn_on_unsaved_changes=>'N'
,p_autocomplete_on_off=>'OFF'
,p_inline_css=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#report .t-fht-thead{',
'  overflow: auto !important;',
'}',
''))
,p_page_template_options=>'#DEFAULT#'
,p_last_updated_by=>'ADIZOHAR'
,p_last_upd_yyyymmddhh24miss=>'20210329143409'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9905068422740501)
,p_plug_name=>'Filter'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9907719837740528)
,p_plug_name=>'ShowGraphs'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'ITEM_IS_NOT_ZERO'
,p_plug_display_when_condition=>'P2_ROWS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9905297750740503)
,p_plug_name=>'Report'
,p_region_name=>'report'
,p_parent_plug_id=>wwv_flow_api.id(9907719837740528)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>130
,p_plug_display_point=>'BODY'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    tenant_id,',
'    prd_compartment_path, ',
'    prd_compartment_name, ',
'    prd_region, ',
'    prd_service, ',
'    prd_resource,',
'    USAGE_INTERVAL_START,',
'    USAGE_INTERVAL_END,',
'    sum(',
'		case when USG_CONSUMED_UNITS like ''%MS%'' ',
'        then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000',
'		else USG_BILLED_QUANTITY',
'		end ',
'	) as USG_BILLED_QUANTITY,',
'    case when USG_CONSUMED_UNITS like ''%MS%'' ',
'		then replace(replace(USG_CONSUMED_UNITS,''MS'',''''),''_'','''')',
'		else USG_CONSUMED_UNITS',
'	end as USG_CONSUMED_UNITS, ',
'    USG_CONSUMED_MEASURE,',
'    TAG_SPECIAL,',
'    TAGS_DATA',
'from oci_usage',
'where ',
'    tenant_name=:P2_TENANT_NAME and',
'    (:P2_COMPARTMENT_NAME is null or prd_compartment_name = :P2_COMPARTMENT_NAME) and',
'    (:P2_PRODUCT_SERVICE is null or prd_service = :P2_PRODUCT_SERVICE) and',
'    (:P2_PRODUCT_REGION is null or prd_region = :P2_PRODUCT_REGION) and',
'    (:P2_COMPARTMENT_TOP is null or prd_compartment_path like :P2_COMPARTMENT_TOP ||''%'') and',
'    (:P2_PRODUCT_RESOURCE is null or prd_resource = :P2_PRODUCT_RESOURCE) and',
'    (:P2_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'    (:P2_TENANT_ID is null or tenant_id = :P2_TENANT_ID) and',
'    (:P2_TAG_SPECIAL is null or tag_special = :P2_TAG_SPECIAL) and',
'    (:P2_TAG_KEY is null or tags_data like ''%#'' || :P2_TAG_KEY || ''=%'') and',
'    (:P2_TAG_DATA is null or tags_data like ''%#'' || nvl(:P2_TAG_KEY,''%'') || ''='' || :P2_TAG_DATA || ''#%'') and',
'    USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'') and',
'    USG_BILLED_QUANTITY>0',
'group by ',
'	tenant_id,',
'    prd_compartment_path, ',
'	prd_compartment_name, ',
'	prd_region, ',
'	prd_service, ',
'	prd_resource, ',
'	USG_CONSUMED_UNITS, ',
'	USG_CONSUMED_MEASURE,',
'    USAGE_INTERVAL_START,',
'    USAGE_INTERVAL_END,',
'    TAGS_DATA,',
'    TAG_SPECIAL',
'order by 1,2,3,4',
'',
'',
'',
''))
,p_plug_source_type=>'NATIVE_IR'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet(
 p_id=>wwv_flow_api.id(9905307857740504)
,p_max_row_count=>'1000000'
,p_allow_save_rpt_public=>'Y'
,p_show_nulls_as=>'-'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_show_display_row_count=>'Y'
,p_report_list_mode=>'TABS'
,p_show_detail_link=>'N'
,p_show_rows_per_page=>'N'
,p_show_notify=>'Y'
,p_download_formats=>'CSV:HTML:EMAIL:XLSX:PDF:RTF'
,p_owner=>'USAGE'
,p_internal_uid=>9905307857740504
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(9905496466740505)
,p_db_column_name=>'PRD_COMPARTMENT_PATH'
,p_display_order=>10
,p_column_identifier=>'A'
,p_column_label=>'Prd Compartment Path'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRD_COMPARTMENT_PATH#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(9905524047740506)
,p_db_column_name=>'PRD_COMPARTMENT_NAME'
,p_display_order=>20
,p_column_identifier=>'B'
,p_column_label=>'Prd Compartment Name'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRD_COMPARTMENT_NAME#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(9905699183740507)
,p_db_column_name=>'PRD_REGION'
,p_display_order=>30
,p_column_identifier=>'C'
,p_column_label=>'Prd Region'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRD_REGION#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(9905777360740508)
,p_db_column_name=>'PRD_SERVICE'
,p_display_order=>40
,p_column_identifier=>'D'
,p_column_label=>'Prd Service'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRD_SERVICE#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(9905898081740509)
,p_db_column_name=>'PRD_RESOURCE'
,p_display_order=>50
,p_column_identifier=>'E'
,p_column_label=>'Prd Resource'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRD_RESOURCE#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(9905978395740510)
,p_db_column_name=>'USG_BILLED_QUANTITY'
,p_display_order=>60
,p_column_identifier=>'F'
,p_column_label=>'Usg Billed Quantity'
,p_column_html_expression=>'<span style="white-space:nowrap;">#USG_BILLED_QUANTITY#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(9906057561740511)
,p_db_column_name=>'USG_CONSUMED_UNITS'
,p_display_order=>70
,p_column_identifier=>'G'
,p_column_label=>'Usg Consumed Units'
,p_column_html_expression=>'<span style="white-space:nowrap;">#USG_CONSUMED_UNITS#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(9906191666740512)
,p_db_column_name=>'USG_CONSUMED_MEASURE'
,p_display_order=>80
,p_column_identifier=>'H'
,p_column_label=>'Usg Consumed Measure'
,p_column_html_expression=>'<span style="white-space:nowrap;">#USG_CONSUMED_MEASURE#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(9924908761716121)
,p_db_column_name=>'USAGE_INTERVAL_START'
,p_display_order=>90
,p_column_identifier=>'I'
,p_column_label=>'Usage Interval Start'
,p_column_html_expression=>'<span style="white-space:nowrap;">#USAGE_INTERVAL_START#</span>'
,p_column_type=>'DATE'
,p_column_alignment=>'CENTER'
,p_format_mask=>'DD-MON-YYYY HH24:MI'
,p_tz_dependent=>'N'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(9925093992716122)
,p_db_column_name=>'USAGE_INTERVAL_END'
,p_display_order=>100
,p_column_identifier=>'J'
,p_column_label=>'Usage Interval End'
,p_column_html_expression=>'<span style="white-space:nowrap;">#USAGE_INTERVAL_END#</span>'
,p_column_type=>'DATE'
,p_column_alignment=>'CENTER'
,p_format_mask=>'DD-MON-YYYY HH24:MI'
,p_tz_dependent=>'N'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(10814538653165717)
,p_db_column_name=>'TAGS_DATA'
,p_display_order=>120
,p_column_identifier=>'L'
,p_column_label=>'Tags Data (Separated by #)'
,p_column_html_expression=>'<span style="white-space:nowrap;">#TAGS_DATA#</span>'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12305713938574229)
,p_db_column_name=>'TENANT_ID'
,p_display_order=>130
,p_column_identifier=>'M'
,p_column_label=>'Tenant Id'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11789105721177224)
,p_db_column_name=>'TAG_SPECIAL'
,p_display_order=>140
,p_column_identifier=>'N'
,p_column_label=>'Tag Special'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_rpt(
 p_id=>wwv_flow_api.id(9917472939935282)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'99175'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'TENANT_ID:PRD_COMPARTMENT_PATH:PRD_COMPARTMENT_NAME:PRD_REGION:PRD_SERVICE:PRD_RESOURCE:USG_BILLED_QUANTITY:USG_CONSUMED_UNITS:USG_CONSUMED_MEASURE:USAGE_INTERVAL_START:USAGE_INTERVAL_END:TAG_SPECIAL:TAGS_DATA:'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9906337017740514)
,p_plug_name=>'OCPUs Chart per Compartment'
,p_parent_plug_id=>wwv_flow_api.id(9907719837740528)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>70
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(9906423826740515)
,p_region_id=>wwv_flow_api.id(9906337017740514)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'horizontal'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_sorting=>'value-desc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
,p_overview_rendered=>'off'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(9906502232740516)
,p_chart_id=>wwv_flow_api.id(9906423826740515)
,p_seq=>10
,p_name=>'OCPUs per Service'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    prd_compartment_name,',
'    prd_service, ',
'    sum(',
'		case when USG_CONSUMED_UNITS like ''%MS%'' ',
'        then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000',
'		else USG_BILLED_QUANTITY',
'		end ',
'	) as USG_BILLED_QUANTITY',
'from oci_usage',
'where ',
'    tenant_name=:P2_TENANT_NAME and',
'    (:P2_COMPARTMENT_NAME is null or prd_compartment_name = :P2_COMPARTMENT_NAME) and',
'    (:P2_PRODUCT_SERVICE is null or prd_service = :P2_PRODUCT_SERVICE) and',
'    (:P2_PRODUCT_REGION is null or prd_region = :P2_PRODUCT_REGION) and',
'    (:P2_COMPARTMENT_TOP is null or prd_compartment_path like :P2_COMPARTMENT_TOP ||''%'') and',
'    USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'') and',
'    (:P2_PRODUCT_RESOURCE is null or prd_resource = :P2_PRODUCT_RESOURCE) and',
'    (:P2_TENANT_ID is null or tenant_id = :P2_TENANT_ID) and',
'    (:P2_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'    (:P2_TAG_KEY is null or tags_data like ''%#'' || :P2_TAG_KEY || ''=%'') and',
'    (:P2_TAG_DATA is null or tags_data like ''%#'' || nvl(:P2_TAG_KEY,''%'') || ''='' || :P2_TAG_DATA || ''#%'') and',
'    (:P2_TAG_SPECIAL is null or tag_special = :P2_TAG_SPECIAL) and',
'    USG_BILLED_QUANTITY>0 and',
'    USG_CONSUMED_MEASURE=''OCPUS''',
'group by ',
'	prd_compartment_name, prd_service',
'order by 3 desc',
'',
'',
'',
''))
,p_series_name_column_name=>'PRD_SERVICE'
,p_items_value_column_name=>'USG_BILLED_QUANTITY'
,p_group_short_desc_column_name=>'USG_BILLED_QUANTITY'
,p_items_label_column_name=>'PRD_COMPARTMENT_NAME'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'insideBarEdge'
,p_items_label_font_style=>'normal'
,p_items_label_font_size=>'8'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9906780581740518)
,p_chart_id=>wwv_flow_api.id(9906423826740515)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9906673387740517)
,p_chart_id=>wwv_flow_api.id(9906423826740515)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9906821641740519)
,p_plug_name=>'Storage Chart per Compartment in TB'
,p_parent_plug_id=>wwv_flow_api.id(9907719837740528)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>90
,p_plug_new_grid_row=>false
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(9906988781740520)
,p_region_id=>wwv_flow_api.id(9906821641740519)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'horizontal'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_sorting=>'value-desc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
,p_overview_rendered=>'off'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(9907045247740521)
,p_chart_id=>wwv_flow_api.id(9906988781740520)
,p_seq=>10
,p_name=>'Storage per Service in TB'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    prd_compartment_name,',
'    prd_service,',
'    round(sum(',
'        case ',
'            when USG_CONSUMED_UNITS = ''KB'' then USG_BILLED_QUANTITY/1000/1000/1000',
'            when USG_CONSUMED_UNITS = ''MB'' then USG_BILLED_QUANTITY/1000/1000',
'            when USG_CONSUMED_UNITS = ''GB'' then USG_BILLED_QUANTITY/1000',
'            when USG_CONSUMED_UNITS = ''TB'' then USG_BILLED_QUANTITY',
'        end',
'    ),2) as USG_BILLED_QUANTITY',
'from ',
'(',
'    select ',
'        prd_compartment_name,',
'        prd_service, ',
'        sum(',
'            case when USG_CONSUMED_UNITS like ''%MS%'' ',
'            then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000',
'            else USG_BILLED_QUANTITY',
'            end ',
'        ) as USG_BILLED_QUANTITY,',
'        case when USG_CONSUMED_UNITS like ''%MS%'' ',
'            then replace(replace(USG_CONSUMED_UNITS,''MS'',''''),''_'','''')',
'            else USG_CONSUMED_UNITS',
'        end as USG_CONSUMED_UNITS',
'    from oci_usage',
'    where ',
'        tenant_name=:P2_TENANT_NAME and',
'        (:P2_COMPARTMENT_NAME is null or prd_compartment_name = :P2_COMPARTMENT_NAME) and',
'        (:P2_PRODUCT_SERVICE is null or prd_service = :P2_PRODUCT_SERVICE) and',
'        (:P2_PRODUCT_REGION is null or prd_region = :P2_PRODUCT_REGION) and',
'        (:P2_COMPARTMENT_TOP is null or prd_compartment_path like :P2_COMPARTMENT_TOP ||''%'') and',
'        (:P2_PRODUCT_RESOURCE is null or prd_resource = :P2_PRODUCT_RESOURCE) and',
'        (:P2_TENANT_ID is null or tenant_id = :P2_TENANT_ID) and',
'        (:P2_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'        (:P2_TAG_KEY is null or tags_data like ''%#'' || :P2_TAG_KEY || ''=%'') and',
'        (:P2_TAG_DATA is null or tags_data like ''%#'' || nvl(:P2_TAG_KEY,''%'') || ''='' || :P2_TAG_DATA || ''#%'') and',
'        (:P2_TAG_SPECIAL is null or tag_special = :P2_TAG_SPECIAL) and',
'        USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'') and',
'        USG_BILLED_QUANTITY>0 and',
'        USG_CONSUMED_MEASURE=''STORAGE_SIZE''',
'    group by ',
'        prd_compartment_name,',
'        prd_service,',
'        USG_CONSUMED_UNITS',
')',
'group by prd_compartment_name, prd_service order by 3 desc',
'',
'',
''))
,p_series_name_column_name=>'PRD_SERVICE'
,p_items_value_column_name=>'USG_BILLED_QUANTITY'
,p_group_short_desc_column_name=>'USG_BILLED_QUANTITY'
,p_items_label_column_name=>'PRD_COMPARTMENT_NAME'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'insideBarEdge'
,p_items_label_font_family=>'Arial'
,p_items_label_font_style=>'normal'
,p_items_label_font_size=>'8'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9907262849740523)
,p_chart_id=>wwv_flow_api.id(9906988781740520)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9907197005740522)
,p_chart_id=>wwv_flow_api.id(9906988781740520)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9909405153740545)
,p_plug_name=>'OCPUs Resource Chart'
,p_parent_plug_id=>wwv_flow_api.id(9907719837740528)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>50
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(9909551743740546)
,p_region_id=>wwv_flow_api.id(9909405153740545)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'off'
,p_stack_label=>'off'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
,p_overview_rendered=>'off'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(9909674684740547)
,p_chart_id=>wwv_flow_api.id(9909551743740546)
,p_seq=>10
,p_name=>'OCPUs per Resource'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    prd_resource, ',
'    sum(',
'		case when USG_CONSUMED_UNITS like ''%MS%'' ',
'        then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000',
'		else USG_BILLED_QUANTITY',
'		end ',
'	) as USG_BILLED_QUANTITY',
'from oci_usage',
'where ',
'    tenant_name=:P2_TENANT_NAME and',
'    (:P2_COMPARTMENT_NAME is null or prd_compartment_name = :P2_COMPARTMENT_NAME) and',
'    (:P2_COMPARTMENT_TOP is null or prd_compartment_path like :P2_COMPARTMENT_TOP ||''%'') and',
'    (:P2_PRODUCT_SERVICE is null or prd_service = :P2_PRODUCT_SERVICE) and',
'    (:P2_PRODUCT_REGION is null or prd_region = :P2_PRODUCT_REGION) and',
'    (:P2_PRODUCT_RESOURCE is null or prd_resource = :P2_PRODUCT_RESOURCE) and',
'    (:P2_TENANT_ID is null or tenant_id = :P2_TENANT_ID) and',
'    (:P2_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'    (:P2_TAG_KEY is null or tags_data like ''%#'' || :P2_TAG_KEY || ''=%'') and',
'    (:P2_TAG_DATA is null or tags_data like ''%#'' || nvl(:P2_TAG_KEY,''%'') || ''='' || :P2_TAG_DATA || ''#%'') and',
'    (:P2_TAG_SPECIAL is null or tag_special = :P2_TAG_SPECIAL) and',
'    USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'') and',
'    USG_BILLED_QUANTITY>0 and',
'    USG_CONSUMED_MEASURE=''OCPUS''',
'group by ',
'	prd_resource',
'order by 2 desc',
'',
'',
'',
''))
,p_items_value_column_name=>'USG_BILLED_QUANTITY'
,p_group_short_desc_column_name=>'USG_BILLED_QUANTITY'
,p_items_label_column_name=>'PRD_RESOURCE'
,p_color=>'#4CD964'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'auto'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9909811381740549)
,p_chart_id=>wwv_flow_api.id(9909551743740546)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9909783516740548)
,p_chart_id=>wwv_flow_api.id(9909551743740546)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9923029639716102)
,p_plug_name=>'OCPUs Product Chart'
,p_parent_plug_id=>wwv_flow_api.id(9907719837740528)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>10
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(9923190243716103)
,p_region_id=>wwv_flow_api.id(9923029639716102)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'off'
,p_connect_nulls=>'Y'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(9923297286716104)
,p_chart_id=>wwv_flow_api.id(9923190243716103)
,p_seq=>10
,p_name=>'OCPUs per Service'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    prd_service, ',
'    sum(',
'		case when USG_CONSUMED_UNITS like ''%MS%'' ',
'        then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000',
'		else USG_BILLED_QUANTITY',
'		end ',
'	) as USG_BILLED_QUANTITY',
'from oci_usage',
'where ',
'    tenant_name=:P2_TENANT_NAME and',
'    (:P2_COMPARTMENT_NAME is null or prd_compartment_name = :P2_COMPARTMENT_NAME) and',
'    (:P2_COMPARTMENT_TOP is null or prd_compartment_path like :P2_COMPARTMENT_TOP ||''%'') and',
'    (:P2_PRODUCT_SERVICE is null or prd_service = :P2_PRODUCT_SERVICE) and',
'    (:P2_PRODUCT_REGION is null or prd_region = :P2_PRODUCT_REGION) and',
'    (:P2_TENANT_ID is null or tenant_id = :P2_TENANT_ID) and',
'    (:P2_PRODUCT_RESOURCE is null or prd_resource = :P2_PRODUCT_RESOURCE) and',
'    (:P2_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'    (:P2_TAG_KEY is null or tags_data like ''%#'' || :P2_TAG_KEY || ''=%'') and',
'    (:P2_TAG_DATA is null or tags_data like ''%#'' || nvl(:P2_TAG_KEY,''%'') || ''='' || :P2_TAG_DATA || ''#%'') and',
'    (:P2_TAG_SPECIAL is null or tag_special = :P2_TAG_SPECIAL) and',
'    USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'') and',
'    USG_BILLED_QUANTITY>0 and',
'    USG_CONSUMED_MEASURE=''OCPUS''',
'group by ',
'	prd_service',
'order by 2 desc',
'',
'',
'',
''))
,p_items_value_column_name=>'USG_BILLED_QUANTITY'
,p_group_short_desc_column_name=>'USG_BILLED_QUANTITY'
,p_items_label_column_name=>'PRD_SERVICE'
,p_color=>'#4CD964'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'auto'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9923304855716105)
,p_chart_id=>wwv_flow_api.id(9923190243716103)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9923476916716106)
,p_chart_id=>wwv_flow_api.id(9923190243716103)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9923541167716107)
,p_plug_name=>'Storage Chart in TB'
,p_parent_plug_id=>wwv_flow_api.id(9907719837740528)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>30
,p_plug_new_grid_row=>false
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(9923640328716108)
,p_region_id=>wwv_flow_api.id(9923541167716107)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'off'
,p_connect_nulls=>'Y'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(9923743722716109)
,p_chart_id=>wwv_flow_api.id(9923640328716108)
,p_seq=>10
,p_name=>'Storage per Service in TB'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    prd_service,',
'    round(sum(',
'        case ',
'            when USG_CONSUMED_UNITS = ''KB'' then USG_BILLED_QUANTITY/1000/1000/1000',
'            when USG_CONSUMED_UNITS = ''MB'' then USG_BILLED_QUANTITY/1000/1000',
'            when USG_CONSUMED_UNITS = ''GB'' then USG_BILLED_QUANTITY/1000',
'            when USG_CONSUMED_UNITS = ''TB'' then USG_BILLED_QUANTITY',
'        end',
'    ),2) as USG_BILLED_QUANTITY',
'from ',
'(',
'    select ',
'        prd_service, ',
'        sum(',
'            case when USG_CONSUMED_UNITS like ''%MS%'' ',
'            then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000',
'            else USG_BILLED_QUANTITY',
'            end ',
'        ) as USG_BILLED_QUANTITY,',
'        case when USG_CONSUMED_UNITS like ''%MS%'' ',
'            then replace(replace(USG_CONSUMED_UNITS,''MS'',''''),''_'','''')',
'            else USG_CONSUMED_UNITS',
'        end as USG_CONSUMED_UNITS',
'    from oci_usage',
'    where ',
'        tenant_name=:P2_TENANT_NAME and',
'        (:P2_COMPARTMENT_NAME is null or prd_compartment_name = :P2_COMPARTMENT_NAME) and',
'        (:P2_PRODUCT_SERVICE is null or prd_service = :P2_PRODUCT_SERVICE) and',
'        (:P2_PRODUCT_REGION is null or prd_region = :P2_PRODUCT_REGION) and',
'        (:P2_COMPARTMENT_TOP is null or prd_compartment_path like :P2_COMPARTMENT_TOP ||''%'') and',
'        (:P2_PRODUCT_RESOURCE is null or prd_resource = :P2_PRODUCT_RESOURCE) and',
'        (:P2_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'        (:P2_TENANT_ID is null or tenant_id = :P2_TENANT_ID) and',
'        (:P2_TAG_KEY is null or tags_data like ''%#'' || :P2_TAG_KEY || ''=%'') and',
'        (:P2_TAG_DATA is null or tags_data like ''%#'' || nvl(:P2_TAG_KEY,''%'') || ''='' || :P2_TAG_DATA || ''#%'') and',
'        (:P2_TAG_SPECIAL is null or tag_special = :P2_TAG_SPECIAL) and',
'        USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'') and',
'        USG_BILLED_QUANTITY>0 and',
'        USG_CONSUMED_MEASURE=''STORAGE_SIZE''',
'    group by ',
'        prd_service,',
'        USG_CONSUMED_UNITS',
')',
'group by prd_service order by 2 desc',
'',
'',
''))
,p_items_value_column_name=>'USG_BILLED_QUANTITY'
,p_group_short_desc_column_name=>'USG_BILLED_QUANTITY'
,p_items_label_column_name=>'PRD_SERVICE'
,p_color=>'#34AADC'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'auto'
);
end;
/
begin
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9923915405716111)
,p_chart_id=>wwv_flow_api.id(9923640328716108)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9923836203716110)
,p_chart_id=>wwv_flow_api.id(9923640328716108)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(10813323429165705)
,p_plug_name=>'Storage Resource in TB'
,p_parent_plug_id=>wwv_flow_api.id(9907719837740528)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>60
,p_plug_new_grid_row=>false
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(10813427444165706)
,p_region_id=>wwv_flow_api.id(10813323429165705)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'off'
,p_stack_label=>'off'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
,p_overview_rendered=>'off'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(10813589982165707)
,p_chart_id=>wwv_flow_api.id(10813427444165706)
,p_seq=>10
,p_name=>'Storage per Resource  in TB'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    prd_resource,',
'    round(sum(',
'        case ',
'            when USG_CONSUMED_UNITS = ''KB'' then USG_BILLED_QUANTITY/1000/1000/1000',
'            when USG_CONSUMED_UNITS = ''MB'' then USG_BILLED_QUANTITY/1000/1000',
'            when USG_CONSUMED_UNITS = ''GB'' then USG_BILLED_QUANTITY/1000',
'            when USG_CONSUMED_UNITS = ''TB'' then USG_BILLED_QUANTITY',
'        end',
'    ),2) as USG_BILLED_QUANTITY',
'from ',
'(',
'    select ',
'        prd_resource, ',
'        sum(',
'            case when USG_CONSUMED_UNITS like ''%MS%'' ',
'            then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000',
'            else USG_BILLED_QUANTITY',
'            end ',
'        ) as USG_BILLED_QUANTITY,',
'        case when USG_CONSUMED_UNITS like ''%MS%'' ',
'            then replace(replace(USG_CONSUMED_UNITS,''MS'',''''),''_'','''')',
'            else USG_CONSUMED_UNITS',
'        end as USG_CONSUMED_UNITS',
'    from oci_usage',
'    where ',
'        tenant_name=:P2_TENANT_NAME and',
'        (:P2_COMPARTMENT_NAME is null or prd_compartment_name = :P2_COMPARTMENT_NAME) and',
'        (:P2_PRODUCT_SERVICE is null or prd_service = :P2_PRODUCT_SERVICE) and',
'        (:P2_PRODUCT_REGION is null or prd_region = :P2_PRODUCT_REGION) and',
'        (:P2_COMPARTMENT_TOP is null or prd_compartment_path like :P2_COMPARTMENT_TOP ||''%'') and',
'        (:P2_PRODUCT_RESOURCE is null or prd_resource = :P2_PRODUCT_RESOURCE) and',
'        (:P2_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'        (:P2_TENANT_ID is null or tenant_id = :P2_TENANT_ID) and',
'        (:P2_TAG_KEY is null or tags_data like ''%#'' || :P2_TAG_KEY || ''=%'') and',
'        (:P2_TAG_DATA is null or tags_data like ''%#'' || nvl(:P2_TAG_KEY,''%'') || ''='' || :P2_TAG_DATA || ''#%'') and',
'        (:P2_TAG_SPECIAL is null or tag_special = :P2_TAG_SPECIAL) and',
'        USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'') and',
'        USG_BILLED_QUANTITY>0 and',
'        USG_CONSUMED_MEASURE=''STORAGE_SIZE''',
'    group by ',
'        prd_resource,',
'        USG_CONSUMED_UNITS',
')',
'group by prd_resource order by 2 desc',
'',
'',
''))
,p_items_value_column_name=>'USG_BILLED_QUANTITY'
,p_group_short_desc_column_name=>'USG_BILLED_QUANTITY'
,p_items_label_column_name=>'PRD_RESOURCE'
,p_color=>'#34AADC'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'auto'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(10813796398165709)
,p_chart_id=>wwv_flow_api.id(10813427444165706)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(10813694012165708)
,p_chart_id=>wwv_flow_api.id(10813427444165706)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(11789267282177225)
,p_plug_name=>'OCPUs Chart per Tag Special Data'
,p_parent_plug_id=>wwv_flow_api.id(9907719837740528)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>110
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(11789334170177226)
,p_region_id=>wwv_flow_api.id(11789267282177225)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'horizontal'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_sorting=>'value-desc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(11789415051177227)
,p_chart_id=>wwv_flow_api.id(11789334170177226)
,p_seq=>10
,p_name=>'OCPUs per Service'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    tag_special,',
'    prd_service, ',
'    sum(',
'		case when USG_CONSUMED_UNITS like ''%MS%'' ',
'        then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000',
'		else USG_BILLED_QUANTITY',
'		end ',
'	) as USG_BILLED_QUANTITY',
'from oci_usage',
'where ',
'    tenant_name=:P2_TENANT_NAME and',
'    (:P2_COMPARTMENT_NAME is null or prd_compartment_name = :P2_COMPARTMENT_NAME) and',
'    (:P2_PRODUCT_SERVICE is null or prd_service = :P2_PRODUCT_SERVICE) and',
'    (:P2_PRODUCT_REGION is null or prd_region = :P2_PRODUCT_REGION) and',
'    (:P2_COMPARTMENT_TOP is null or prd_compartment_path like :P2_COMPARTMENT_TOP ||''%'') and',
'    USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'') and',
'    (:P2_PRODUCT_RESOURCE is null or prd_resource = :P2_PRODUCT_RESOURCE) and',
'    (:P2_TENANT_ID is null or tenant_id = :P2_TENANT_ID) and',
'    (:P2_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'    (:P2_TAG_KEY is null or tags_data like ''%#'' || :P2_TAG_KEY || ''=%'') and',
'    (:P2_TAG_DATA is null or tags_data like ''%#'' || nvl(:P2_TAG_KEY,''%'') || ''='' || :P2_TAG_DATA || ''#%'') and',
'    (:P2_TAG_SPECIAL is null or tag_special = :P2_TAG_SPECIAL) and',
'    USG_BILLED_QUANTITY>0 and',
'    USG_CONSUMED_MEASURE=''OCPUS'' and',
'    tag_special is not null',
'group by ',
'	tag_special, prd_service',
'order by 3 desc',
'',
'',
'',
''))
,p_series_name_column_name=>'PRD_SERVICE'
,p_items_value_column_name=>'USG_BILLED_QUANTITY'
,p_group_short_desc_column_name=>'USG_BILLED_QUANTITY'
,p_items_label_column_name=>'TAG_SPECIAL'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'insideBarEdge'
,p_items_label_font_style=>'normal'
,p_items_label_font_size=>'8'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(11789569471177228)
,p_chart_id=>wwv_flow_api.id(11789334170177226)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(11789694843177229)
,p_chart_id=>wwv_flow_api.id(11789334170177226)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(11789788701177230)
,p_plug_name=>'Storage Chart per Tag Special Data TB'
,p_parent_plug_id=>wwv_flow_api.id(9907719837740528)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>120
,p_plug_new_grid_row=>false
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(11789895535177231)
,p_region_id=>wwv_flow_api.id(11789788701177230)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'horizontal'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_sorting=>'value-desc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(11789946205177232)
,p_chart_id=>wwv_flow_api.id(11789895535177231)
,p_seq=>10
,p_name=>'Storage per Service in TB'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    tag_special,',
'    prd_service,',
'    round(sum(',
'        case ',
'            when USG_CONSUMED_UNITS = ''KB'' then USG_BILLED_QUANTITY/1000/1000/1000',
'            when USG_CONSUMED_UNITS = ''MB'' then USG_BILLED_QUANTITY/1000/1000',
'            when USG_CONSUMED_UNITS = ''GB'' then USG_BILLED_QUANTITY/1000',
'            when USG_CONSUMED_UNITS = ''TB'' then USG_BILLED_QUANTITY',
'        end',
'    ),2) as USG_BILLED_QUANTITY',
'from ',
'(',
'    select ',
'        tag_special,',
'        prd_service, ',
'        sum(',
'            case when USG_CONSUMED_UNITS like ''%MS%'' ',
'            then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000',
'            else USG_BILLED_QUANTITY',
'            end ',
'        ) as USG_BILLED_QUANTITY,',
'        case when USG_CONSUMED_UNITS like ''%MS%'' ',
'            then replace(replace(USG_CONSUMED_UNITS,''MS'',''''),''_'','''')',
'            else USG_CONSUMED_UNITS',
'        end as USG_CONSUMED_UNITS',
'    from oci_usage',
'    where ',
'        tenant_name=:P2_TENANT_NAME and',
'        (:P2_COMPARTMENT_NAME is null or prd_compartment_name = :P2_COMPARTMENT_NAME) and',
'        (:P2_PRODUCT_SERVICE is null or prd_service = :P2_PRODUCT_SERVICE) and',
'        (:P2_PRODUCT_REGION is null or prd_region = :P2_PRODUCT_REGION) and',
'        (:P2_COMPARTMENT_TOP is null or prd_compartment_path like :P2_COMPARTMENT_TOP ||''%'') and',
'        (:P2_PRODUCT_RESOURCE is null or prd_resource = :P2_PRODUCT_RESOURCE) and',
'        (:P2_TENANT_ID is null or tenant_id = :P2_TENANT_ID) and',
'        (:P2_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'        (:P2_TAG_KEY is null or tags_data like ''%#'' || :P2_TAG_KEY || ''=%'') and',
'        (:P2_TAG_DATA is null or tags_data like ''%#'' || nvl(:P2_TAG_KEY,''%'') || ''='' || :P2_TAG_DATA || ''#%'') and',
'        (:P2_TAG_SPECIAL is null or tag_special = :P2_TAG_SPECIAL) and',
'        USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'') and',
'        USG_BILLED_QUANTITY>0 and',
'        USG_CONSUMED_MEASURE=''STORAGE_SIZE'' and',
'        tag_special is not null',
'    group by ',
'        tag_special,',
'        prd_service,',
'        USG_CONSUMED_UNITS',
')',
'group by tag_special, prd_service order by 3 desc',
'',
'',
''))
,p_series_name_column_name=>'PRD_SERVICE'
,p_items_value_column_name=>'USG_BILLED_QUANTITY'
,p_group_short_desc_column_name=>'USG_BILLED_QUANTITY'
,p_items_label_column_name=>'TAG_SPECIAL'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'insideBarEdge'
,p_items_label_font_family=>'Arial'
,p_items_label_font_style=>'normal'
,p_items_label_font_size=>'8'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(11790068420177233)
,p_chart_id=>wwv_flow_api.id(11789895535177231)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(11790159375177234)
,p_chart_id=>wwv_flow_api.id(11789895535177231)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9907890048740529)
,p_plug_name=>'Choose Tenant'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>20
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_source=>'No Data Found, Please Choose Tenant, Date and press Submit.'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'ITEM_IS_ZERO'
,p_plug_display_when_condition=>'P2_ROWS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_button(
 p_id=>wwv_flow_api.id(9907440231740525)
,p_button_sequence=>160
,p_button_plug_id=>wwv_flow_api.id(9905068422740501)
,p_button_name=>'P2_SUBMIT'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#:t-Button--large:t-Button--stretch:t-Button--gapTop'
,p_button_template_id=>wwv_flow_api.id(9821119233688096)
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Submit'
,p_button_position=>'BODY'
,p_grid_new_row=>'Y'
,p_grid_column_span=>2
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9905170083740502)
,p_name=>'P2_TENANT_NAME'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_prompt=>'Tenant Name'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'select distinct tenant_name o, tenant_name r from oci_usage order by 1'
,p_lov_display_null=>'YES'
,p_lov_null_text=>'Please Choose...'
,p_cHeight=>1
,p_tag_attributes=>'style="background-color:#e0f0f0"'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9906284166740513)
,p_name=>'P2_COMPARTMENT_NAME'
,p_item_sequence=>180
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_prompt=>'Compartment'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct prd_compartment_name o, prd_compartment_name r from ',
'oci_usage ',
'where',
'tenant_name=:P2_TENANT_NAME',
'    and USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'')',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P2_TENANT_NAME,P2_DATE'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9907304843740524)
,p_name=>'P2_COMPARTMENT_TOP'
,p_item_sequence=>130
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_prompt=>'Top Level Compartment'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select top_level_compartment o, top_level_compartment r',
'from ',
'(',
'    select distinct ',
'        case when prd_compartment_path like ''%/%'' then substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) ',
'        else prd_compartment_path',
'        end top_level_compartment ',
'    from oci_usage',
'    where prd_compartment_path is not null and tenant_name=:P2_TENANT_NAME',
'    and USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'')',
') where top_level_compartment is not null order by 1',
''))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P2_TENANT_NAME,P2_DATE'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9908424606740535)
,p_name=>'P2_ROWS'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_use_cache_before_default=>'NO'
,p_format_mask=>'999G999G999G999G999G999G990'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    count(*) cnt',
'from oci_usage',
'where ',
'    tenant_name=:P2_TENANT_NAME and',
'    (:P2_COMPARTMENT_NAME is null or prd_compartment_name = :P2_COMPARTMENT_NAME) and',
'    (:P2_PRODUCT_SERVICE is null or prd_service = :P2_PRODUCT_SERVICE) and',
'    (:P2_PRODUCT_REGION is null or prd_region = :P2_PRODUCT_REGION) and',
'    (:P2_COMPARTMENT_TOP is null or prd_compartment_path like :P2_COMPARTMENT_TOP ||''%'') and',
'    (:P2_PRODUCT_RESOURCE is null or prd_resource = :P2_PRODUCT_RESOURCE) and',
'    (:P2_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and    ',
'    (:P2_TAG_KEY is null or tags_data like ''%#'' || :P2_TAG_KEY || ''=%'') and',
'    (:P2_TAG_DATA is null or tags_data like ''%#'' || nvl(:P2_TAG_KEY,''%'') || ''='' || :P2_TAG_DATA || ''#%'') and',
'    (:P2_TAG_SPECIAL is null or tag_special = :P2_TAG_SPECIAL) and',
'    USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'') and',
'    USG_BILLED_QUANTITY>0'))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9922959205716101)
,p_name=>'P2_PRODUCT_SERVICE'
,p_item_sequence=>120
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_prompt=>'Product Service'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct prd_service o, prd_service r ',
'from ',
'    oci_usage ',
'where',
'    tenant_name=:P2_TENANT_NAME',
'    and USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'')',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P2_TENANT_NAME,P2_DATE'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9924098385716112)
,p_name=>'P2_PRODUCT_REGION'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_prompt=>'Product Region'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct prd_region o, prd_region r from ',
'oci_usage ',
'where',
'    tenant_name=:P2_TENANT_NAME ',
'    and USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'')',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P2_TENANT_NAME,P2_DATE'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9924729288716119)
,p_name=>'P2_DATE'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_item_default=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'') R',
'from ',
'(',
'    select ',
'        USAGE_INTERVAL_START, ',
'        dense_rank() over (partition by null order by USAGE_INTERVAL_START desc) rn ',
'    from oci_usage_stats ',
'    where tenant_name=:P2_TENANT_NAME    ',
') where rn=3',
''))
,p_item_default_type=>'SQL_QUERY'
,p_prompt=>'Date'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'') O, to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'') R',
'from oci_usage_stats',
'where ',
'    tenant_name=:P2_TENANT_NAME and ',
'    USAGE_INTERVAL_START > trunc(sysdate-3)',
'union',
'select to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'') O, to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'') R',
'from oci_usage_stats ',
'where ',
'    tenant_name=:P2_TENANT_NAME and ',
'    USAGE_INTERVAL_START between trunc(sysdate-60) and trunc(sysdate-3) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'union',
'select to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'') O, to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'') R',
'from oci_usage_stats ',
'where ',
'    tenant_name=:P2_TENANT_NAME and ',
'    USAGE_INTERVAL_START < trunc(sysdate-60) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START) and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),5)=1',
'order by 1 desc'))
,p_lov_cascade_parent_items=>'P2_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_tag_attributes=>'style="background-color:#e0f0f0"'
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(10809491249953662)
,p_name=>'P2_TAG_DATA'
,p_item_sequence=>140
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_prompt=>'Tag Data Filter'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>30
,p_begin_on_new_line=>'N'
,p_colspan=>4
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'N'
,p_attribute_02=>'N'
,p_attribute_04=>'TEXT'
,p_attribute_05=>'BOTH'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(10813894822165710)
,p_name=>'P2_PRODUCT_RESOURCE'
,p_item_sequence=>170
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_prompt=>'Product Resource'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct prd_resource o, prd_resource r ',
'from ',
'    oci_usage ',
'where',
'    tenant_name=:P2_TENANT_NAME',
'    and USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'')',
'    and prd_resource is not null',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P2_TENANT_NAME,P2_DATE'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(10814109748165713)
,p_name=>'P2_WINDOWS_OCPUS'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_prompt=>'Inc Win OCPUs ?'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'STATIC2:No;N'
,p_lov_display_null=>'YES'
,p_lov_null_text=>'Yes'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(10814210740165714)
,p_name=>'P2_LAST_DATE_LOADED'
,p_item_sequence=>150
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Last Date Loaded'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    to_char(max(USAGE_INTERVAL_START),''DD-MON-YYYY DY HH24:MI'') dte',
'from oci_usage_stats',
'where ',
'    tenant_name=:P2_TENANT_NAME'))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_grid_column=>11
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11790270500177235)
,p_name=>'P2_TAG_SPECIAL'
,p_item_sequence=>190
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_prompt=>'Tag Special Data'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct tag_special o, tag_special r ',
'from ',
'    oci_usage ',
'where',
'    tenant_name=:P2_TENANT_NAME',
'    and USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'')',
'and tag_special is not null',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P2_TENANT_NAME,P2_DATE'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>4
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11931232277191605)
,p_name=>'P2_TAG_KEY'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_prompt=>'Tag Key'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct tag_key o, tag_key r ',
'from ',
'    oci_usage_tag_keys',
'where',
'    tenant_name=:P2_TENANT_NAME',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P2_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11978661800439218)
,p_name=>'P2_TAG_SPECIAL_KEY_DISPLAY'
,p_item_sequence=>200
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Tag Special Key'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select MIN(ref_name) o',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P2_TENANT_NAME',
'    and ref_type=''TAG_SPECIAL_KEY''',
'order by 1'))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11979797429439229)
,p_name=>'P2_ROWS_DISPLAY'
,p_item_sequence=>100
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Rows Filtered'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    to_char(count(*),''999,999,999'') cnt',
'from oci_usage',
'where ',
'    tenant_name=:P2_TENANT_NAME and',
'    (:P2_COMPARTMENT_NAME is null or prd_compartment_name = :P2_COMPARTMENT_NAME) and',
'    (:P2_PRODUCT_SERVICE is null or prd_service = :P2_PRODUCT_SERVICE) and',
'    (:P2_PRODUCT_REGION is null or prd_region = :P2_PRODUCT_REGION) and',
'    (:P2_COMPARTMENT_TOP is null or prd_compartment_path like :P2_COMPARTMENT_TOP ||''%'') and',
'    (:P2_PRODUCT_RESOURCE is null or prd_resource = :P2_PRODUCT_RESOURCE) and',
'    (:P2_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and    ',
'    (:P2_TAG_KEY is null or tags_data like ''%#'' || :P2_TAG_KEY || ''=%'') and',
'    (:P2_TAG_DATA is null or tags_data like ''%#'' || nvl(:P2_TAG_KEY,''%'') || ''='' || :P2_TAG_DATA || ''#%'') and',
'    (:P2_TAG_SPECIAL is null or tag_special = :P2_TAG_SPECIAL) and',
'    USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'') and',
'    USG_BILLED_QUANTITY>0'))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12305652747574228)
,p_name=>'P2_TENANT_ID'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_api.id(9905068422740501)
,p_prompt=>'Tenant Id'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct tenant_id o, tenant_id r ',
'from ',
'    oci_usage ',
'where',
'    tenant_name=:P2_TENANT_NAME',
'    and USAGE_INTERVAL_START = to_date(:P2_DATE,''YYYY-MM-DD HH24:MI'')',
'    and tenant_id is not null',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P2_TENANT_NAME,P2_DATE'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(12278115700302648)
,p_computation_sequence=>10
,p_computation_item=>'P2_TENANT_NAME'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'QUERY'
,p_computation=>'select tenant_name from oci_usage where rownum<2'
,p_compute_when=>'P2_TENANT_NAME'
,p_compute_when_type=>'ITEM_IS_NULL'
);
end;
/
begin
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(9924897922716120)
,p_computation_sequence=>20
,p_computation_item=>'P2_DATE'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'QUERY'
,p_computation=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'') R',
'from ',
'(',
'    select ',
'        USAGE_INTERVAL_START, ',
'        dense_rank() over (partition by null order by USAGE_INTERVAL_START desc) rn ',
'    from oci_usage_stats ',
'    where tenant_name=:P2_TENANT_NAME    ',
') where rn=3',
''))
,p_compute_when=>'P2_DATE'
,p_compute_when_type=>'ITEM_IS_NULL'
);
null;
end;
/
prompt --application/pages/page_00003
begin
wwv_flow_api.create_page(
 p_id=>3
,p_user_interface_id=>wwv_flow_api.id(9843694399688199)
,p_name=>'Usage Over Time'
,p_step_title=>'Usage Over Time'
,p_warn_on_unsaved_changes=>'N'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_last_updated_by=>'ADIZOHAR'
,p_last_upd_yyyymmddhh24miss=>'20210329143553'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9908591071740536)
,p_plug_name=>'ChooseTenant'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>20
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_source=>'No Data Found, Please Choose Tenant, Date and press Submit.'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'ITEM_IS_ZERO'
,p_plug_display_when_condition=>'P3_ROWS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9908767434740538)
,p_plug_name=>'ShowCharts'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'ITEM_IS_NOT_ZERO'
,p_plug_display_when_condition=>'P3_ROWS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(19898398982635585)
,p_plug_name=>'Daily OCPUs Chart'
,p_parent_plug_id=>wwv_flow_api.id(9908767434740538)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>10
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(9986341223919550)
,p_region_id=>wwv_flow_api.id(19898398982635585)
,p_chart_type=>'bar'
,p_height=>'400'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
,p_overview_rendered=>'off'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(9988037120919551)
,p_chart_id=>wwv_flow_api.id(9986341223919550)
,p_seq=>10
,p_name=>'OCPUs per Service'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    case when :P3_TIMEFRAME is null or :P3_TIMEFRAME >=30 then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'    else to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'')',
'    end USAGE_INTERVAL_START,',
'    prd_service, ',
'    sum(',
'		case when USG_CONSUMED_UNITS like ''%MS%'' ',
'        then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000',
'		else USG_BILLED_QUANTITY',
'		end ',
'	) as USG_BILLED_QUANTITY',
'from oci_usage',
'where ',
'    tenant_name=:P3_TENANT_NAME and',
'    (:P3_COMPARTMENT_NAME is null or prd_compartment_name = :P3_COMPARTMENT_NAME) and',
'    (:P3_COMPARTMENT_TOP is null or prd_compartment_path like :P3_COMPARTMENT_TOP ||''%'') and',
'    (:P3_PRODUCT_SERVICE is null or prd_service = :P3_PRODUCT_SERVICE) and',
'    (:P3_PRODUCT_REGION is null or prd_region = :P3_PRODUCT_REGION) and',
'    (:P3_PRODUCT_RESOURCE is null or prd_resource = :P3_PRODUCT_RESOURCE) and',
'    (:P3_TENANT_ID is null or tenant_id = :P3_TENANT_ID) and',
'    (:P3_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'    (:P3_TAG_KEY is null or tags_data like ''%#'' || :P3_TAG_KEY || ''=%'') and',
'    (:P3_TAG_DATA is null or tags_data like ''%#'' || nvl(:P3_TAG_KEY,''%'') || ''='' || :P3_TAG_DATA || ''#%'') and',
'    USAGE_INTERVAL_START >= trunc(sysdate)-1-(nvl(:P3_TIMEFRAME,30)) and',
'    (',
'        (:P3_TIMEFRAME < 3)',
'        or',
'        (:P3_TIMEFRAME = 3 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),3) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 7 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),6) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 30 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),2) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 60 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),3) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 90 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),4) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 180 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),6) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME >= 360 and  mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),12) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'    ) and',
'    USG_BILLED_QUANTITY>0 and',
'    USG_CONSUMED_MEASURE=''OCPUS''',
'group by ',
'    case when :P3_TIMEFRAME is null or :P3_TIMEFRAME >=30 then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'    else to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'')',
'    end,',
'    prd_service',
'order by 2 desc',
'',
'',
'',
''))
,p_series_name_column_name=>'PRD_SERVICE'
,p_items_value_column_name=>'USG_BILLED_QUANTITY'
,p_group_short_desc_column_name=>'USG_BILLED_QUANTITY'
,p_items_label_column_name=>'USAGE_INTERVAL_START'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'auto'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9986886731919550)
,p_chart_id=>wwv_flow_api.id(9986341223919550)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9987437023919551)
,p_chart_id=>wwv_flow_api.id(9986341223919550)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(19898910510635590)
,p_plug_name=>'Daily Storage Chart in TB'
,p_parent_plug_id=>wwv_flow_api.id(9908767434740538)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>20
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(9988970219919552)
,p_region_id=>wwv_flow_api.id(19898910510635590)
,p_chart_type=>'bar'
,p_height=>'400'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
,p_overview_rendered=>'off'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(9990659651919553)
,p_chart_id=>wwv_flow_api.id(9988970219919552)
,p_seq=>10
,p_name=>'Storage per Service in TB'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    USAGE_INTERVAL_START,',
'    prd_service,',
'    round(sum(',
'        case ',
'            when USG_CONSUMED_UNITS = ''KB'' then USG_BILLED_QUANTITY/1000/1000/1000',
'            when USG_CONSUMED_UNITS = ''MB'' then USG_BILLED_QUANTITY/1000/1000',
'            when USG_CONSUMED_UNITS = ''GB'' then USG_BILLED_QUANTITY/1000',
'            when USG_CONSUMED_UNITS = ''TB'' then USG_BILLED_QUANTITY',
'        end',
'    ),2) as USG_BILLED_QUANTITY',
'from ',
'(',
'    select ',
'        case when :P3_TIMEFRAME is null or :P3_TIMEFRAME >=30 then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        else to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'')',
'        end USAGE_INTERVAL_START,',
'        prd_service, ',
'        sum(',
'            case when USG_CONSUMED_UNITS like ''%MS%'' ',
'            then USG_BILLED_QUANTITY/((USAGE_INTERVAL_END-USAGE_INTERVAL_START)*24*60*60)/1000',
'            else USG_BILLED_QUANTITY',
'            end ',
'        ) as USG_BILLED_QUANTITY,',
'        case when USG_CONSUMED_UNITS like ''%MS%'' ',
'            then replace(replace(USG_CONSUMED_UNITS,''MS'',''''),''_'','''')',
'            else USG_CONSUMED_UNITS',
'        end as USG_CONSUMED_UNITS',
'    from oci_usage',
'    where ',
'        tenant_name=:P3_TENANT_NAME and',
'        (:P3_COMPARTMENT_NAME is null or prd_compartment_name = :P3_COMPARTMENT_NAME) and',
'        (:P3_PRODUCT_SERVICE is null or prd_service = :P3_PRODUCT_SERVICE) and',
'        (:P3_PRODUCT_REGION is null or prd_region = :P3_PRODUCT_REGION) and',
'        (:P3_COMPARTMENT_TOP is null or prd_compartment_path like :P3_COMPARTMENT_TOP ||''%'') and',
'        (:P3_PRODUCT_RESOURCE is null or prd_resource = :P3_PRODUCT_RESOURCE) and',
'        (:P3_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'        (:P3_TENANT_ID is null or tenant_id = :P3_TENANT_ID) and',
'        (:P3_TAG_KEY is null or tags_data like ''%#'' || :P3_TAG_KEY || ''=%'') and',
'        (:P3_TAG_DATA is null or tags_data like ''%#'' || nvl(:P3_TAG_KEY,''%'') || ''='' || :P3_TAG_DATA || ''#%'') and',
'        USAGE_INTERVAL_START >= trunc(sysdate)-1-nvl(:P3_TIMEFRAME,30) and',
'        (',
'            (:P3_TIMEFRAME < 3)',
'            or',
'            (:P3_TIMEFRAME = 3 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),3) = 0) ',
'            or',
'            (:P3_TIMEFRAME = 7 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),6) = 0) ',
'            or',
'            (:P3_TIMEFRAME = 30 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),2) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'            or',
'            (:P3_TIMEFRAME = 60 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),3) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'            or',
'            (:P3_TIMEFRAME = 90 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),4) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'            or',
'            (:P3_TIMEFRAME = 180 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),6) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'            or',
'            (:P3_TIMEFRAME >= 360 and  mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),12) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        ) and',
'        USG_BILLED_QUANTITY>0 and',
'        USG_CONSUMED_MEASURE=''STORAGE_SIZE''',
'    group by ',
'        case when :P3_TIMEFRAME is null or :P3_TIMEFRAME >=30 then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        else to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24:MI'')',
'        end,',
'        prd_service,',
'        USG_CONSUMED_UNITS',
')',
'group by USAGE_INTERVAL_START,prd_service order by 1,2 desc',
'',
'',
''))
,p_series_name_column_name=>'PRD_SERVICE'
,p_items_value_column_name=>'USG_BILLED_QUANTITY'
,p_group_short_desc_column_name=>'USG_BILLED_QUANTITY'
,p_items_label_column_name=>'USAGE_INTERVAL_START'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'auto'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9989436754919552)
,p_chart_id=>wwv_flow_api.id(9988970219919552)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(9990058752919552)
,p_chart_id=>wwv_flow_api.id(9988970219919552)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(19880437765659984)
,p_plug_name=>'Filter'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_button(
 p_id=>wwv_flow_api.id(9907630617740527)
,p_button_sequence=>100
,p_button_plug_id=>wwv_flow_api.id(19880437765659984)
,p_button_name=>'P3_BUTTON'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#:t-Button--large:t-Button--stretch:t-Button--gapTop'
,p_button_template_id=>wwv_flow_api.id(9821119233688096)
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Submit'
,p_button_position=>'BODY'
,p_grid_new_row=>'Y'
,p_grid_column_span=>1
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9908613557740537)
,p_name=>'P3_ROWS'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_use_cache_before_default=>'NO'
,p_format_mask=>'999G999G999G999G999G999G990'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    count(*) cnt',
'from oci_usage',
'where ',
'    tenant_name=:P3_TENANT_NAME and',
'    (:P3_COMPARTMENT_NAME is null or prd_compartment_name = :P3_COMPARTMENT_NAME) and',
'    (:P3_COMPARTMENT_TOP is null or prd_compartment_path like :P3_COMPARTMENT_TOP ||''%'') and',
'    (:P3_PRODUCT_SERVICE is null or prd_service = :P3_PRODUCT_SERVICE) and',
'    (:P3_PRODUCT_REGION is null or prd_region = :P3_PRODUCT_REGION) and',
'    (:P3_PRODUCT_RESOURCE is null or prd_resource = :P3_PRODUCT_RESOURCE) and',
'    (:P3_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'    (:P3_TAG_KEY is null or tags_data like ''%#'' || :P3_TAG_KEY || ''=%'') and',
'    (:P3_TAG_DATA is null or tags_data like ''%#'' || nvl(:P3_TAG_KEY,''%'') || ''=%'' || :P3_TAG_DATA || ''#'') and',
'    USAGE_INTERVAL_START >= trunc(sysdate)-1-(nvl(:P3_TIMEFRAME,3)) and',
'    USG_BILLED_QUANTITY>0',
'    and (',
'        (:P3_TIMEFRAME < 3)',
'        or',
'        (:P3_TIMEFRAME = 3 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),3) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 7 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),6) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 30 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),2) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 60 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),3) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 90 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),4) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 180 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),6) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME >= 360 and  mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),12) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'    )'))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9909310480740544)
,p_name=>'P3_LAST_DATE_LOADED'
,p_item_sequence=>160
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Last Date Loaded'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    to_char(max(USAGE_INTERVAL_START),''DD-MON-YYYY DY HH24:MI'') dte',
'from oci_usage_stats',
'where ',
'    tenant_name=:P3_TENANT_NAME'))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_begin_on_new_line=>'N'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9925196553716123)
,p_name=>'P3_TIMEFRAME'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_item_default=>'1'
,p_prompt=>'Time Frame'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'STATIC2:1 Day;1,3 Days;3,7 Days;7,1 Month;30,2 Months;60,3 Months;90,6 Months;180,1 Year;365,2 Years;730'
,p_cHeight=>1
,p_tag_attributes=>'style="background-color:#e0f0f0"'
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9978951613919528)
,p_name=>'P3_TENANT_NAME'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_prompt=>'Tenant Name'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'select distinct tenant_name o, tenant_name r from oci_usage order by 1'
,p_lov_display_null=>'YES'
,p_lov_null_text=>'Please Choose...'
,p_cHeight=>1
,p_tag_attributes=>'style="background-color:#e0f0f0"'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9979740759919533)
,p_name=>'P3_PRODUCT_REGION'
,p_item_sequence=>120
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_prompt=>'Product Region'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct prd_region o, prd_region r from ',
'oci_usage ',
'where',
'    tenant_name=:P3_TENANT_NAME ',
'    and USAGE_INTERVAL_START >= trunc(sysdate)-1-(nvl(:P3_TIMEFRAME,3))',
'    and (',
'        (:P3_TIMEFRAME < 3)',
'        or',
'        (:P3_TIMEFRAME = 3 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),3) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 7 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),6) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 30 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),2) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 60 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),3) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 90 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),4) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 180 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),6) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME >= 360 and  mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),12) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'    ) ',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P3_TENANT_NAME,P3_TIMEFRAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9980109116919533)
,p_name=>'P3_COMPARTMENT_TOP'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_prompt=>'Top Level Compartment'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select top_level_compartment o, top_level_compartment r',
'from ',
'(',
'    select distinct ',
'        case when prd_compartment_path like ''%/%'' then substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) ',
'        else prd_compartment_path',
'        end top_level_compartment ',
'    from oci_usage',
'    where prd_compartment_path is not null and tenant_name=:P3_TENANT_NAME',
'    and USAGE_INTERVAL_START >= trunc(sysdate)-1-(nvl(:P3_TIMEFRAME,3))',
'    and (',
'        (:P3_TIMEFRAME < 3)',
'        or',
'        (:P3_TIMEFRAME = 3 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),3) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 7 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),6) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 30 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),2) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 60 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),3) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 90 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),4) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 180 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),6) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME >= 360 and  mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),12) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'    ) ',
') where top_level_compartment is not null order by 1',
''))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P3_TENANT_NAME,P3_TIMEFRAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9980531759919534)
,p_name=>'P3_COMPARTMENT_NAME'
,p_item_sequence=>130
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_prompt=>'Compartment'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct prd_compartment_name o, prd_compartment_name r from ',
'oci_usage ',
'where',
'tenant_name=:P3_TENANT_NAME and',
'prd_compartment_name is not null',
'    and USAGE_INTERVAL_START >= trunc(sysdate)-1-(nvl(:P3_TIMEFRAME,3))',
'    and (',
'        (:P3_TIMEFRAME < 3)',
'        or',
'        (:P3_TIMEFRAME = 3 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),3) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 7 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),6) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 30 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),2) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 60 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),3) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 90 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),4) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 180 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),6) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME >= 360 and  mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),12) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'    ) ',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P3_TENANT_NAME,P3_TIMEFRAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9980954475919534)
,p_name=>'P3_PRODUCT_SERVICE'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_prompt=>'Product'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct prd_service o, prd_service r ',
'from ',
'    oci_usage ',
'where',
'    tenant_name=:P3_TENANT_NAME',
'    and prd_service is not null',
'    and USAGE_INTERVAL_START >= trunc(sysdate)-1-(nvl(:P3_TIMEFRAME,3))',
'    and (',
'        (:P3_TIMEFRAME < 3)',
'        or',
'        (:P3_TIMEFRAME = 3 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),3) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 7 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),6) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 30 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),2) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 60 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),3) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 90 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),4) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 180 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),6) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME >= 360 and  mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),12) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'    ) ',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P3_TENANT_NAME,P3_TIMEFRAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(10814336125165715)
,p_name=>'P3_TAG_DATA'
,p_item_sequence=>150
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_prompt=>'Filter Tag Data'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>30
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'N'
,p_attribute_02=>'N'
,p_attribute_04=>'TEXT'
,p_attribute_05=>'BOTH'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(10841489486360734)
,p_name=>'P3_WINDOWS_OCPUS'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_prompt=>'Inc Win OCPUs ?'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'STATIC2:No;N'
,p_lov_display_null=>'YES'
,p_lov_null_text=>'Yes'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>1
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(10841724869362885)
,p_name=>'P3_PRODUCT_RESOURCE'
,p_item_sequence=>140
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_prompt=>'Product Resource'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct prd_resource o, prd_resource r ',
'from ',
'    oci_usage ',
'where',
'    tenant_name=:P3_TENANT_NAME',
'    and prd_resource is not null',
'    and USAGE_INTERVAL_START >= trunc(sysdate)-1-(nvl(:P3_TIMEFRAME,3))',
'    and (',
'        (:P3_TIMEFRAME < 3)',
'        or',
'        (:P3_TIMEFRAME = 3 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),3) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 7 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),6) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 30 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),2) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 60 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),3) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 90 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),4) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 180 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),6) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME >= 360 and  mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),12) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'    ) ',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P3_TENANT_NAME,P3_TIMEFRAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11959520800325148)
,p_name=>'P3_TAG_KEY'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_prompt=>'Tag Key'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct tag_key o, tag_key r ',
'from ',
'    oci_usage_tag_keys',
'where',
'    tenant_name=:P3_TENANT_NAME',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P2_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11979854855439230)
,p_name=>'P3_ROWS_DISPLAY'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Rows Filtered'
,p_format_mask=>'999G999G999G999G999G999G990'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    to_char(count(*),''999,999,999'') cnt',
'from oci_usage',
'where ',
'    tenant_name=:P3_TENANT_NAME and',
'    (:P3_COMPARTMENT_NAME is null or prd_compartment_name = :P3_COMPARTMENT_NAME) and',
'    (:P3_COMPARTMENT_TOP is null or prd_compartment_path like :P3_COMPARTMENT_TOP ||''%'') and',
'    (:P3_PRODUCT_SERVICE is null or prd_service = :P3_PRODUCT_SERVICE) and',
'    (:P3_PRODUCT_REGION is null or prd_region = :P3_PRODUCT_REGION) and',
'    (:P3_PRODUCT_RESOURCE is null or prd_resource = :P3_PRODUCT_RESOURCE) and',
'    (:P3_WINDOWS_OCPUS is null or prd_resource not like ''%WINDOW%'') and',
'    (:P3_TAG_KEY is null or tags_data like ''%#'' || :P3_TAG_KEY || ''=%'') and',
'    (:P3_TAG_DATA is null or tags_data like ''%#'' || nvl(:P3_TAG_KEY,''%'') || ''=%'' || :P3_TAG_DATA || ''#'') and',
'    USAGE_INTERVAL_START >= trunc(sysdate)-1-(nvl(:P3_TIMEFRAME,3)) and',
'    USG_BILLED_QUANTITY>0',
'    and (',
'        (:P3_TIMEFRAME < 3)',
'        or',
'        (:P3_TIMEFRAME = 3 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),3) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 7 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),6) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 30 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),2) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 60 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),3) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 90 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),4) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 180 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),6) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME >= 360 and  mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),12) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'    )'))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_begin_on_new_line=>'N'
,p_colspan=>1
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
end;
/
begin
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12305899776574230)
,p_name=>'P3_TENANT_ID'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_api.id(19880437765659984)
,p_prompt=>'Tenant Id'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct tenant_id o, tenant_id r ',
'from ',
'    oci_usage ',
'where',
'    tenant_name=:P3_TENANT_NAME',
'    and prd_service is not null',
'    and USAGE_INTERVAL_START >= trunc(sysdate)-1-(nvl(:P3_TIMEFRAME,3))',
'    and (',
'        (:P3_TIMEFRAME < 3)',
'        or',
'        (:P3_TIMEFRAME = 3 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),3) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 7 and mod(to_number(to_char(USAGE_INTERVAL_START,''HH24'')),6) = 0) ',
'        or',
'        (:P3_TIMEFRAME = 30 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),2) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 60 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),3) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 90 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),4) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME = 180 and mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),6) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'        or',
'        (:P3_TIMEFRAME >= 360 and  mod(to_number(to_char(USAGE_INTERVAL_START,''DD'')),12) = 0) and USAGE_INTERVAL_START = trunc(USAGE_INTERVAL_START)',
'    ) ',
'    and tenant_id is not null',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P3_TENANT_NAME,P3_TIMEFRAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>1
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(12278049021302647)
,p_computation_sequence=>10
,p_computation_item=>'P3_TENANT_NAME'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'QUERY'
,p_computation=>'select tenant_name from oci_usage where rownum<2'
,p_compute_when=>'P3_TENANT_NAME'
,p_compute_when_type=>'ITEM_IS_NULL'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(13350423906239101)
,p_computation_sequence=>10
,p_computation_item=>'P3_TIMEFRAME'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'STATIC_ASSIGNMENT'
,p_computation=>'3'
,p_compute_when=>'P3_TIMEFRAME'
,p_compute_when_type=>'ITEM_IS_NULL'
);
end;
/
prompt --application/pages/page_00004
begin
wwv_flow_api.create_page(
 p_id=>4
,p_user_interface_id=>wwv_flow_api.id(9843694399688199)
,p_name=>'Cost Analysis'
,p_step_title=>'Cost Analysis'
,p_warn_on_unsaved_changes=>'N'
,p_autocomplete_on_off=>'OFF'
,p_inline_css=>wwv_flow_string.join(wwv_flow_t_varchar2(
'.a-IRR-table tr td[headers*="rep_col_grey"]',
'{',
'    background-color: #efffff;',
'}',
'',
'.a-IRR-table tr td[headers*="rep_col_pink"]',
'{',
'    background-color: #ffefff;',
'}',
'',
'#P4_COST_DISPLAY {',
'  background-color: #F5FBB4; font-weight: bold; font-size: 14px;',
'}',
'#P4_YEARLY_DISPLAY {',
'  background-color: #F5FBB4; font-weight: bold; font-size: 14px;',
'}',
'#P4_INFO_DISPLAY {',
'  background-color: #FfFff0; font-size: 12px;',
'}',
'#P4_REPORT_SELECTOR { background-color: #F5FBB4; font-weight: bold; font-size: 13px;}',
'',
'#cost_explorer .t-fht-thead{',
'  overflow: auto !important;',
'}',
'',
'#resource_report .t-fht-thead{',
'  overflow: auto !important;',
'}',
'',
'#cost_report .t-fht-thead{',
'  overflow: auto !important;',
'}',
''))
,p_page_template_options=>'#DEFAULT#'
,p_last_updated_by=>'ADIZOHAR'
,p_last_upd_yyyymmddhh24miss=>'20210329152107'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(10816553122165737)
,p_plug_name=>' Filter'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--accent12:t-Region--scrollBody:t-Form--noPadding:margin-top-none:margin-left-none:margin-right-none'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_grid_column_span=>9
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(10817046393165742)
,p_plug_name=>'Stats Info'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--accent12:t-Region--scrollBody:margin-top-none:margin-bottom-none:margin-left-none:margin-right-none'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>20
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_new_grid_row=>false
,p_plug_grid_column_span=>3
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(21608843544513693)
,p_plug_name=>'ShowGraphs'
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding:t-Region--removeHeader:t-Region--noUI:t-Region--scrollBody:t-Form--noPadding:margin-top-none:margin-bottom-none:margin-left-none:margin-right-none'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>40
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'ITEM_IS_NOT_ZERO'
,p_plug_display_when_condition=>'P4_ROWS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(10814860863165720)
,p_plug_name=>'Cost Per SKU'
,p_parent_plug_id=>wwv_flow_api.id(21608843544513693)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>60
,p_plug_new_grid_row=>false
,p_plug_new_grid_column=>false
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P4_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Cost Per SKU'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(10814955580165721)
,p_region_id=>wwv_flow_api.id(10814860863165720)
,p_chart_type=>'donut'
,p_height=>'400'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hover_behavior=>'none'
,p_stack=>'off'
,p_stack_label=>'off'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_value_format_type=>'decimal'
,p_value_decimal_places=>1
,p_value_format_scaling=>'auto'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'off'
,p_legend_position=>'auto'
,p_overview_rendered=>'off'
,p_pie_other_threshold=>0
,p_pie_selection_effect=>'highlight'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(10815028626165722)
,p_chart_id=>wwv_flow_api.id(10814955580165721)
,p_seq=>10
,p_name=>'Cost Per Product SKU'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    COST_PRODUCT_SKU||'' ''||min(prd_description) as COST_PRODUCT_SKU,',
'    min(prd_description || '' - ''||prd_resource) as prd_description, ',
'    sum(COST_MY_COST) as COST_MY_COST',
'from oci_cost',
'where ',
'    tenant_name=:P4_TENANT_NAME and',
'    (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'    (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'    (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'    (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'    (:P4_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P4_COST_PRODUCT_SKU) and',
'    (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'    (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'    (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'    (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'    USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'') and',
'    COST_MY_COST > 0',
'    and :P4_REPORT_SELECTOR = ''Cost Per SKU''',
'group by ',
'	COST_PRODUCT_SKU ',
'having sum(COST_MY_COST) > 0',
'order by 3 desc',
'',
'',
'',
''))
,p_items_value_column_name=>'COST_MY_COST'
,p_items_label_column_name=>'COST_PRODUCT_SKU'
,p_items_label_rendered=>true
,p_items_label_position=>'insideBarEdge'
,p_items_label_display_as=>'ALL'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(10815862618165730)
,p_plug_name=>'Cost Per Top Compartment'
,p_parent_plug_id=>wwv_flow_api.id(21608843544513693)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>70
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P4_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Cost Per Top Compartment'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(10815918798165731)
,p_region_id=>wwv_flow_api.id(10815862618165730)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'horizontal'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_sorting=>'value-desc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'off'
,p_legend_position=>'auto'
,p_overview_rendered=>'off'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(10816022718165732)
,p_chart_id=>wwv_flow_api.id(10815918798165731)
,p_seq=>10
,p_name=>'Cost per Top Compartment'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    case',
'        when prd_compartment_path is null then ''No Compartment''',
'        when prd_compartment_path like ''%/%'' then nvl(substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1),''(root)'') ',
'    else prd_compartment_path',
'    end top_level_compartment ,',
'    sum(COST_MY_COST) as COST_MY_COST',
'from oci_cost',
'where ',
'    tenant_name=:P4_TENANT_NAME and',
'    (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'    (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'    (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'    (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'    (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'    (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'    USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'') and',
'    (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'    (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'    COST_MY_COST>0 ',
'    and :P4_REPORT_SELECTOR = ''Cost Per Top Compartment''',
'group by ',
'    case ',
'    when prd_compartment_path is null then ''No Compartment''',
'    when prd_compartment_path like ''%/%'' then nvl(substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1),''(root)'') ',
'    else prd_compartment_path',
'    end  ',
'order by 2 desc',
'',
'',
'',
''))
,p_items_value_column_name=>'COST_MY_COST'
,p_items_label_column_name=>'TOP_LEVEL_COMPARTMENT'
,p_color=>'#34AADC'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'insideBarEdge'
,p_items_label_font_style=>'normal'
,p_items_label_font_size=>'8'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(10816181831165733)
,p_chart_id=>wwv_flow_api.id(10815918798165731)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(10816213077165734)
,p_chart_id=>wwv_flow_api.id(10815918798165731)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(11931816111191611)
,p_plug_name=>'Cost Per Day'
,p_parent_plug_id=>wwv_flow_api.id(21608843544513693)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>20
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P4_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Cost Per Day'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(11931950151191612)
,p_region_id=>wwv_flow_api.id(11931816111191611)
,p_chart_type=>'bar'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hover_behavior=>'none'
,p_stack=>'off'
,p_stack_label=>'off'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'off'
,p_legend_position=>'auto'
,p_overview_rendered=>'off'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(11932020693191613)
,p_chart_id=>wwv_flow_api.id(11931950151191612)
,p_seq=>10
,p_name=>'Cost Per Day'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') as USAGE_DAY, ',
'    sum(COST_MY_COST) as COST_MY_COST',
'from oci_cost',
'where ',
'    tenant_name=:P4_TENANT_NAME and',
'    (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'    (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'    (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'    (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'    (:P4_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P4_COST_PRODUCT_SKU) and',
'    (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'    (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'    (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'    (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'    USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'')',
'    and COST_MY_COST > 0',
'    and not (:P4_TENANT_ID is null and :P4_COMPARTMENT_NAME is null and :P4_PRODUCT_SERVICE is null and :P4_PRODUCT_REGION is null and :P4_COMPARTMENT_TOP is null and :P4_TAG_KEY is null and :P4_TAG_DATA is null and :P4_COST_PRODUCT_SKU is null and :'
||'P4_TAG_SPECIAL is null)',
'    and :P4_REPORT_SELECTOR = ''Cost Per Day''',
'group by ',
'	to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'')',
'union all',
'select ',
'    to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') as USAGE_DAY, ',
'    sum(COST_MY_COST) as COST_MY_COST',
'from oci_cost_stats',
'where ',
'    tenant_name=:P4_TENANT_NAME and',
'    USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'')',
'    and COST_MY_COST > 0',
'    and (:P4_TENANT_ID is null and :P4_COMPARTMENT_NAME is null and :P4_PRODUCT_SERVICE is null and :P4_PRODUCT_REGION is null and :P4_COMPARTMENT_TOP is null and :P4_TAG_KEY is null and :P4_TAG_DATA is null and :P4_COST_PRODUCT_SKU is null and :P4_T'
||'AG_SPECIAL is null)',
'    and :P4_REPORT_SELECTOR = ''Cost Per Day''',
'group by ',
'	to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'')',
'order by 1',
'',
'',
'',
''))
,p_items_value_column_name=>'COST_MY_COST'
,p_items_label_column_name=>'USAGE_DAY'
,p_color=>'#34AADC'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'auto'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(11932199654191614)
,p_chart_id=>wwv_flow_api.id(11931950151191612)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_type=>'date-short'
,p_numeric_pattern=>'DD-MON-YYYY'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_tick_label_font_size=>'10'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(11932208487191615)
,p_chart_id=>wwv_flow_api.id(11931950151191612)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(11932315365191616)
,p_plug_name=>'Cost Per Service'
,p_parent_plug_id=>wwv_flow_api.id(21608843544513693)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>50
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P4_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Cost Per Service'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(11932427454191617)
,p_region_id=>wwv_flow_api.id(11932315365191616)
,p_chart_type=>'donut'
,p_height=>'400'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hover_behavior=>'none'
,p_stack=>'off'
,p_stack_label=>'off'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_value_format_type=>'decimal'
,p_value_decimal_places=>1
,p_value_format_scaling=>'auto'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'off'
,p_legend_position=>'auto'
,p_overview_rendered=>'off'
,p_pie_other_threshold=>0
,p_pie_selection_effect=>'highlight'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(11932548617191618)
,p_chart_id=>wwv_flow_api.id(11932427454191617)
,p_seq=>10
,p_name=>'Cost Per Service'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    replace(nvl(prd_service,COST_PRODUCT_SKU),''_'','' '') prd_service,',
'    sum(COST_MY_COST) as COST_MY_COST',
'from oci_cost',
'where ',
'    tenant_name=:P4_TENANT_NAME and',
'    (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'    (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'    (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'    (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'    (:P4_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P4_COST_PRODUCT_SKU) and',
'    (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'    (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'    (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'    (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'    USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'') and',
'    COST_MY_COST > 0',
'    and :P4_REPORT_SELECTOR = ''Cost Per Service''',
'',
'group by ',
'	replace(nvl(prd_service,COST_PRODUCT_SKU),''_'','' '')',
'order by 2 desc',
'',
'',
'',
''))
,p_items_value_column_name=>'COST_MY_COST'
,p_items_label_column_name=>'PRD_SERVICE'
,p_items_label_rendered=>true
,p_items_label_position=>'insideBarEdge'
,p_items_label_display_as=>'LBL_VAL'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(11978878827439220)
,p_plug_name=>'Cost Per Tag Special'
,p_parent_plug_id=>wwv_flow_api.id(21608843544513693)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>90
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P4_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Cost Per Tag Special'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(11978966613439221)
,p_region_id=>wwv_flow_api.id(11978878827439220)
,p_chart_type=>'bar'
,p_height=>'700'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'horizontal'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_sorting=>'value-desc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'off'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(11979065634439222)
,p_chart_id=>wwv_flow_api.id(11978966613439221)
,p_seq=>10
,p_name=>'Cost per Special Tag'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    nvl(tag_special,''No Tag'') as prd_compartment_name,',
'    sum(COST_MY_COST) as COST_MY_COST',
'from oci_cost',
'where ',
'    tenant_name=:P4_TENANT_NAME and',
'    (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'    (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'    (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'    (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'    (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'    USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'') and',
'    (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'    (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'    (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'    COST_MY_COST>0 ',
'    and :P4_REPORT_SELECTOR = ''Cost Per Tag Special''',
'group by ',
'	nvl(tag_special,''No Tag'')',
'order by 2 desc',
'',
'',
'',
''))
,p_items_value_column_name=>'COST_MY_COST'
,p_items_label_column_name=>'PRD_COMPARTMENT_NAME'
,p_color=>'#34AADC'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'insideBarEdge'
,p_items_label_font_style=>'normal'
,p_items_label_font_size=>'8'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(11979188991439223)
,p_chart_id=>wwv_flow_api.id(11978966613439221)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(11979240048439224)
,p_chart_id=>wwv_flow_api.id(11978966613439221)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(12303794643574209)
,p_plug_name=>'Cost Resource Report'
,p_region_name=>'resource_report'
,p_parent_plug_id=>wwv_flow_api.id(21608843544513693)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>110
,p_plug_display_point=>'BODY'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'with data as',
'(',
'    select ',
'        a.tenant_name,',
'        a.USG_RESOURCE_ID as RESOURCE_ID,',
'        min(a.COST_PRODUCT_SKU || '' '' || replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '','''')) as PRODUCT,',
'        min(COST_BILLING_UNIT) COST_BILLING_UNIT,',
'        max(COST_UNIT_PRICE) RATE,',
'        min(COST_CURRENCY_CODE) CURRENCY,',
'        case when count(distinct USAGE_INTERVAL_START) > 0 then',
'            case ',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%HOUR%'' then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%GIB%''  then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%TIB%''  then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%GIGA%'' then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%GB%''   then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%TB%''   then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(PRD_DESCRIPTION))             like ''%HOUR%'' then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)',
'                when min(upper(PRD_DESCRIPTION))             like ''%GIB%''  then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(PRD_DESCRIPTION))             like ''%TIB%''  then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%REQUESTS%'' then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%EMAILS%''   then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%ASSETS%''   then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                else null',
'            end',
'        end SINGLE_QUANTITY,',
'        count(distinct USAGE_INTERVAL_START) HOURS_QUANTITY,',
'        sum(USG_BILLED_QUANTITY) TOTAL_QUANTITY,',
'        sum(COST_MY_COST_OVERAGE) OVERAGE_COST,',
'        sum(COST_MY_COST) USAGE_COST,',
'        sum(COST_MY_COST)*(24 * 31 / count(distinct USAGE_INTERVAL_START)) ESTIMATE_MONTH_31,',
'        sum(COST_MY_COST)*(24 * 365 / count(distinct USAGE_INTERVAL_START)) ESTIMATE_YEAR',
'    from oci_cost a',
'    where ',
'        tenant_name=:P4_TENANT_NAME and',
'        (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'        (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'        (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'        (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'        (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'        (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'        (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'        (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'        (:P4_COST_PRODUCT_SKU is null or a.COST_PRODUCT_SKU = :P4_COST_PRODUCT_SKU) and',
'        USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'')',
'        and COST_MY_COST<>0',
'        and :P4_REPORT_SELECTOR = ''Cost Resource Report''',
'    group by ',
'        a.tenant_name,a.USG_RESOURCE_ID',
')',
'select ',
'    RESOURCE_ID,',
'    PRODUCT,',
'    COST_BILLING_UNIT,',
'    RATE,',
'    CURRENCY,',
'    SINGLE_QUANTITY,',
'    HOURS_QUANTITY,',
'    TOTAL_QUANTITY,',
'    USAGE_COST,',
'    ESTIMATE_MONTH_31,',
'    ESTIMATE_YEAR',
'from',
'    data a',
'order by 1',
'',
''))
,p_plug_source_type=>'NATIVE_IR'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P4_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Cost Resource Report'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
,p_prn_border_color=>'#666666'
);
wwv_flow_api.create_worksheet(
 p_id=>wwv_flow_api.id(12303874435574210)
,p_max_row_count=>'1000000'
,p_allow_save_rpt_public=>'Y'
,p_show_nulls_as=>'-'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_show_display_row_count=>'Y'
,p_report_list_mode=>'TABS'
,p_show_detail_link=>'N'
,p_show_rows_per_page=>'N'
,p_show_notify=>'Y'
,p_download_formats=>'CSV:HTML:EMAIL:XLSX:PDF:RTF'
,p_owner=>'ADIZOHAR'
,p_internal_uid=>12303874435574210
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12305231371574224)
,p_db_column_name=>'RESOURCE_ID'
,p_display_order=>10
,p_column_identifier=>'K'
,p_column_label=>'Resource Id'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12303914004574211)
,p_db_column_name=>'PRODUCT'
,p_display_order=>20
,p_column_identifier=>'A'
,p_column_label=>'Product'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12304097099574212)
,p_db_column_name=>'COST_BILLING_UNIT'
,p_display_order=>30
,p_column_identifier=>'B'
,p_column_label=>'Cost Billing Unit'
,p_column_html_expression=>'<span style="white-space:nowrap;">#COST_BILLING_UNIT#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12304164237574213)
,p_db_column_name=>'RATE'
,p_display_order=>40
,p_column_identifier=>'C'
,p_column_label=>'Customer Rate'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D000'
);
end;
/
begin
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12304936216574221)
,p_db_column_name=>'CURRENCY'
,p_display_order=>50
,p_column_identifier=>'J'
,p_column_label=>'Cur'
,p_column_type=>'STRING'
,p_column_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12304255716574214)
,p_db_column_name=>'SINGLE_QUANTITY'
,p_display_order=>60
,p_column_identifier=>'D'
,p_column_label=>'Single Quantity'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D0'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12304320208574215)
,p_db_column_name=>'HOURS_QUANTITY'
,p_display_order=>70
,p_column_identifier=>'E'
,p_column_label=>'Hours Quantity'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D0'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12304485477574216)
,p_db_column_name=>'TOTAL_QUANTITY'
,p_display_order=>80
,p_column_identifier=>'F'
,p_column_label=>'Total Quantity'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D0'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12304690528574218)
,p_db_column_name=>'USAGE_COST'
,p_display_order=>90
,p_column_identifier=>'G'
,p_column_label=>'Usage Cost'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D000'
,p_static_id=>'rep_col_grey'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12304770770574219)
,p_db_column_name=>'ESTIMATE_MONTH_31'
,p_display_order=>100
,p_column_identifier=>'H'
,p_column_label=>'Estimate Month 31'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12304821038574220)
,p_db_column_name=>'ESTIMATE_YEAR'
,p_display_order=>110
,p_column_identifier=>'I'
,p_column_label=>'Estimate Year'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_rpt(
 p_id=>wwv_flow_api.id(14406108569189301)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'144062'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'RESOURCE_ID:PRODUCT:COST_BILLING_UNIT:RATE:CURRENCY:SINGLE_QUANTITY:HOURS_QUANTITY:TOTAL_QUANTITY:USAGE_COST:ESTIMATE_MONTH_31:ESTIMATE_YEAR'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(12317143055646735)
,p_plug_name=>'Cost Explorer'
,p_region_name=>'cost_explorer'
,p_parent_plug_id=>wwv_flow_api.id(21608843544513693)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>120
,p_plug_display_point=>'BODY'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    TENANT_ID,',
'    USAGE_INTERVAL_START    ,',
'    USAGE_INTERVAL_END      ,',
'    FILE_ID                 ,',
'    PRD_COMPARTMENT_ID      ,',
'    PRD_COMPARTMENT_NAME    ,',
'    PRD_COMPARTMENT_PATH    ,',
'    PRD_AVAILABILITY_DOMAIN ,',
'    PRD_REGION              ,',
'    PRD_SERVICE             ,',
'    USG_RESOURCE_ID         ,',
'    USG_BILLED_QUANTITY     ,',
'    USG_BILLED_QUANTITY_OVERAGE,',
'    COST_SUBSCRIPTION_ID    ,',
'    COST_PRODUCT_SKU        ,',
'    PRD_DESCRIPTION         ,',
'    COST_UNIT_PRICE         ,',
'    COST_UNIT_PRICE_OVERAGE ,',
'    COST_MY_COST            ,',
'    COST_MY_COST_OVERAGE    ,',
'    COST_CURRENCY_CODE      ,',
'    COST_BILLING_UNIT       ,',
'    COST_OVERAGE_FLAG       ,',
'    decode(IS_CORRECTION,''True'',''Y'',''N'') IS_CORRECTION ,',
'    TAG_SPECIAL,',
'    TAGS_DATA               ',
'from oci_cost',
'where ',
'    tenant_name=:P4_TENANT_NAME and',
'    (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'    (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'    (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'    (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'    (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'    (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'    (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'    (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'    (:P4_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P4_COST_PRODUCT_SKU) and',
'    USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'')',
'    and USG_BILLED_QUANTITY <> 0',
'    and :P4_REPORT_SELECTOR = ''Cost Explorer''',
'order by FILE_ID, USAGE_INTERVAL_START, PRD_COMPARTMENT_PATH, PRD_RESOURCE',
'',
'',
'',
''))
,p_plug_source_type=>'NATIVE_IR'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P4_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Cost Explorer'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet(
 p_id=>wwv_flow_api.id(12317206225646736)
,p_max_row_count=>'1000000'
,p_max_rows_per_page=>'20'
,p_allow_save_rpt_public=>'Y'
,p_show_nulls_as=>'-'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_show_display_row_count=>'Y'
,p_report_list_mode=>'TABS'
,p_show_detail_link=>'N'
,p_show_rows_per_page=>'N'
,p_show_notify=>'Y'
,p_download_formats=>'CSV:HTML:EMAIL:XLSX:PDF:RTF'
,p_owner=>'ADI.ZOHAR@ORACLE.COM'
,p_internal_uid=>12317206225646736
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12318514508646749)
,p_db_column_name=>'FILE_ID'
,p_display_order=>10
,p_column_identifier=>'D'
,p_column_label=>'File Id'
,p_column_html_expression=>'<span style="white-space:nowrap;">#FILE_ID#</span>'
,p_column_type=>'STRING'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12318340567646747)
,p_db_column_name=>'USAGE_INTERVAL_START'
,p_display_order=>30
,p_column_identifier=>'B'
,p_column_label=>'Interval Start'
,p_column_html_expression=>'<span style="white-space:nowrap;">#USAGE_INTERVAL_START#</span>'
,p_column_type=>'DATE'
,p_column_alignment=>'CENTER'
,p_format_mask=>'DD-MON-YYYY HH24:MI'
,p_tz_dependent=>'N'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12318447863646748)
,p_db_column_name=>'USAGE_INTERVAL_END'
,p_display_order=>40
,p_column_identifier=>'C'
,p_column_label=>'Interval End'
,p_column_html_expression=>'<span style="white-space:nowrap;">#USAGE_INTERVAL_END#</span>'
,p_column_type=>'DATE'
,p_column_alignment=>'CENTER'
,p_format_mask=>'DD-MON-YYYY HH24:MI'
,p_tz_dependent=>'N'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12318697159646750)
,p_db_column_name=>'PRD_COMPARTMENT_ID'
,p_display_order=>50
,p_column_identifier=>'E'
,p_column_label=>'Compartment Id'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12550371015313301)
,p_db_column_name=>'PRD_COMPARTMENT_NAME'
,p_display_order=>60
,p_column_identifier=>'F'
,p_column_label=>'Compartment Name'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRD_COMPARTMENT_NAME#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12550421380313302)
,p_db_column_name=>'PRD_COMPARTMENT_PATH'
,p_display_order=>70
,p_column_identifier=>'G'
,p_column_label=>'Compartment Path'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRD_COMPARTMENT_PATH#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12550503973313303)
,p_db_column_name=>'PRD_AVAILABILITY_DOMAIN'
,p_display_order=>80
,p_column_identifier=>'H'
,p_column_label=>'Availability Domain'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRD_AVAILABILITY_DOMAIN#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12550637746313304)
,p_db_column_name=>'PRD_REGION'
,p_display_order=>90
,p_column_identifier=>'I'
,p_column_label=>'Region'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRD_REGION#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12550721084313305)
,p_db_column_name=>'PRD_SERVICE'
,p_display_order=>100
,p_column_identifier=>'J'
,p_column_label=>'Service'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRD_SERVICE#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12550943472313307)
,p_db_column_name=>'USG_RESOURCE_ID'
,p_display_order=>120
,p_column_identifier=>'L'
,p_column_label=>'Resource Id'
,p_column_html_expression=>'<span style="white-space:nowrap;">#USG_RESOURCE_ID#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12551058313313308)
,p_db_column_name=>'USG_BILLED_QUANTITY'
,p_display_order=>130
,p_column_identifier=>'M'
,p_column_label=>'Billed Quantity'
,p_column_html_expression=>'<span style="white-space:nowrap;">#USG_BILLED_QUANTITY#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D0000'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12551167767313309)
,p_db_column_name=>'USG_BILLED_QUANTITY_OVERAGE'
,p_display_order=>140
,p_column_identifier=>'N'
,p_column_label=>'Billed Quantity Overage'
,p_column_html_expression=>'<span style="white-space:nowrap;">#USG_BILLED_QUANTITY_OVERAGE#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D0000'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12551209084313310)
,p_db_column_name=>'COST_SUBSCRIPTION_ID'
,p_display_order=>150
,p_column_identifier=>'O'
,p_column_label=>'Subscription Id'
,p_column_type=>'NUMBER'
,p_column_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12551341636313311)
,p_db_column_name=>'COST_PRODUCT_SKU'
,p_display_order=>160
,p_column_identifier=>'P'
,p_column_label=>'Product SKU'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12551463557313312)
,p_db_column_name=>'PRD_DESCRIPTION'
,p_display_order=>170
,p_column_identifier=>'Q'
,p_column_label=>'Prd Description'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRD_DESCRIPTION#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12317467759646738)
,p_db_column_name=>'COST_BILLING_UNIT'
,p_display_order=>180
,p_column_identifier=>'A'
,p_column_label=>'Billing Unit'
,p_column_html_expression=>'<span style="white-space:nowrap;">#COST_BILLING_UNIT#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12551570285313313)
,p_db_column_name=>'COST_UNIT_PRICE'
,p_display_order=>190
,p_column_identifier=>'R'
,p_column_label=>'Unit Price'
,p_column_html_expression=>'<span style="white-space:nowrap;">#COST_UNIT_PRICE#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D000'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12551656460313314)
,p_db_column_name=>'COST_UNIT_PRICE_OVERAGE'
,p_display_order=>200
,p_column_identifier=>'S'
,p_column_label=>'Unit Price Overage'
,p_column_html_expression=>'<span style="white-space:nowrap;">#COST_UNIT_PRICE_OVERAGE#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D000'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12551774048313315)
,p_db_column_name=>'COST_MY_COST'
,p_display_order=>210
,p_column_identifier=>'T'
,p_column_label=>'My Cost'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D000'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12551878308313316)
,p_db_column_name=>'COST_MY_COST_OVERAGE'
,p_display_order=>220
,p_column_identifier=>'U'
,p_column_label=>'My Cost Overage'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D000'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12551944694313317)
,p_db_column_name=>'COST_CURRENCY_CODE'
,p_display_order=>230
,p_column_identifier=>'V'
,p_column_label=>'Currency Code'
,p_column_type=>'STRING'
,p_column_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12552058152313318)
,p_db_column_name=>'COST_OVERAGE_FLAG'
,p_display_order=>240
,p_column_identifier=>'W'
,p_column_label=>'Overage Flag'
,p_column_type=>'STRING'
,p_column_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12552156824313319)
,p_db_column_name=>'IS_CORRECTION'
,p_display_order=>250
,p_column_identifier=>'X'
,p_column_label=>'Is Correction'
,p_column_type=>'STRING'
,p_column_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12552208351313320)
,p_db_column_name=>'TAGS_DATA'
,p_display_order=>260
,p_column_identifier=>'Y'
,p_column_label=>'Tags Data'
,p_column_html_expression=>'<span style="white-space:nowrap;">#TAGS_DATA#</span>'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12306098680574232)
,p_db_column_name=>'TENANT_ID'
,p_display_order=>270
,p_column_identifier=>'Z'
,p_column_label=>'Tenant Id'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11790616588177239)
,p_db_column_name=>'TAG_SPECIAL'
,p_display_order=>280
,p_column_identifier=>'AA'
,p_column_label=>'Tag Special'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_rpt(
 p_id=>wwv_flow_api.id(12563360882328556)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'125634'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_display_rows=>20
,p_report_columns=>'TENANT_ID:FILE_ID:USAGE_INTERVAL_START:USAGE_INTERVAL_END:PRD_COMPARTMENT_NAME:PRD_COMPARTMENT_PATH:PRD_AVAILABILITY_DOMAIN:PRD_REGION:PRD_SERVICE:COST_PRODUCT_SKU:PRD_DESCRIPTION:USG_BILLED_QUANTITY:USG_BILLED_QUANTITY_OVERAGE:COST_BILLING_UNIT:COST'
||'_UNIT_PRICE:COST_UNIT_PRICE_OVERAGE:COST_MY_COST:COST_MY_COST_OVERAGE:COST_CURRENCY_CODE:COST_OVERAGE_FLAG:IS_CORRECTION:TAG_SPECIAL:TAGS_DATA:USG_RESOURCE_ID:'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(13974097805041417)
,p_plug_name=>'Cost Per Day Accumulated'
,p_parent_plug_id=>wwv_flow_api.id(21608843544513693)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>30
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P4_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Cost Per Day Accumulated'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(13974102550041418)
,p_region_id=>wwv_flow_api.id(13974097805041417)
,p_chart_type=>'lineWithArea'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'on'
,p_data_cursor_behavior=>'snap'
,p_hover_behavior=>'none'
,p_stack=>'off'
,p_stack_label=>'off'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'off'
,p_legend_position=>'auto'
,p_overview_rendered=>'off'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(13974239454041419)
,p_chart_id=>wwv_flow_api.id(13974102550041418)
,p_seq=>10
,p_name=>'Cost Per Day Accumulated'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    USAGE_DAY,',
'    cost_my_cost,',
'    sum(cost_my_cost) over (partition by null order by usage_day) cost_accumulated',
'from',
'(',
'    select ',
'        to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') as USAGE_DAY, ',
'        sum(COST_MY_COST) as COST_MY_COST',
'    from oci_cost',
'    where ',
'        tenant_name=:P4_TENANT_NAME and',
'        (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'        (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'        (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'        (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'        (:P4_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P4_COST_PRODUCT_SKU) and',
'        (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'        (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'        (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'        (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'        USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'')',
'        and COST_MY_COST > 0',
'        and not (:P4_TENANT_ID is null and :P4_COMPARTMENT_NAME is null and :P4_PRODUCT_SERVICE is null and :P4_PRODUCT_REGION is null and :P4_COMPARTMENT_TOP is null and :P4_TAG_KEY is null and :P4_TAG_DATA is null and :P4_COST_PRODUCT_SKU is null a'
||'nd :P4_TAG_SPECIAL is null )',
'        and :P4_REPORT_SELECTOR = ''Cost Per Day Accumulated''',
'    group by ',
'        to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'')',
'    union all',
'    select ',
'        to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') as USAGE_DAY, ',
'        sum(COST_MY_COST) as COST_MY_COST',
'    from oci_cost_stats',
'    where ',
'        tenant_name=:P4_TENANT_NAME and',
'        USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'')',
'        and COST_MY_COST > 0',
'        and (:P4_TENANT_ID is null and :P4_COMPARTMENT_NAME is null and :P4_PRODUCT_SERVICE is null and :P4_PRODUCT_REGION is null and :P4_COMPARTMENT_TOP is null and :P4_TAG_KEY is null and :P4_TAG_DATA is null and :P4_COST_PRODUCT_SKU is null and :'
||'P4_TAG_SPECIAL is null)',
'        and :P4_REPORT_SELECTOR = ''Cost Per Day Accumulated''',
'    group by ',
'        to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'')',
')',
'order by 1',
'',
'',
'',
''))
,p_items_value_column_name=>'COST_ACCUMULATED'
,p_items_label_column_name=>'USAGE_DAY'
,p_color=>'#34AADC'
,p_line_style=>'solid'
,p_line_type=>'auto'
,p_marker_rendered=>'on'
,p_marker_shape=>'diamond'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'aboveMarker'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(13974468820041421)
,p_chart_id=>wwv_flow_api.id(13974102550041418)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_title=>'Cost Accumulated'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'bottom'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'on'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(13974384360041420)
,p_chart_id=>wwv_flow_api.id(13974102550041418)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_type=>'date-short'
,p_numeric_pattern=>'DD-MON-YYYY'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_tick_label_font_size=>'10'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(21606421457513668)
,p_plug_name=>'Cost Report'
,p_region_name=>'cost_report'
,p_parent_plug_id=>wwv_flow_api.id(21608843544513693)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>100
,p_plug_display_point=>'BODY'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'with data as',
'(',
'    select ',
'        a.tenant_name,',
'        a.COST_PRODUCT_SKU || '' '' || replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '','''') as PRODUCT,',
'        a.COST_PRODUCT_SKU,',
'        min(COST_BILLING_UNIT) COST_BILLING_UNIT,',
'        max(COST_UNIT_PRICE) RATE,',
'        min(COST_CURRENCY_CODE) CURRENCY,',
'        case when count(distinct USAGE_INTERVAL_START) > 0 then',
'            case ',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%HOUR%'' then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%GIB%''  then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%TIB%''  then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%GIGA%'' then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%GB%''   then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%TB%''   then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(PRD_DESCRIPTION))             like ''%HOUR%'' then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)',
'                when min(upper(PRD_DESCRIPTION))             like ''%GIB%''  then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(PRD_DESCRIPTION))             like ''%TIB%''  then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%REQUESTS%'' then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%EMAILS%''   then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                when min(upper(nvl(COST_BILLING_UNIT,''ZZ''))) like ''%ASSETS%''   then sum(USG_BILLED_QUANTITY)/count(distinct USAGE_INTERVAL_START)*744',
'                else null',
'            end',
'        end SINGLE_QUANTITY,',
'        count(distinct USAGE_INTERVAL_START) HOURS_QUANTITY,',
'        sum(USG_BILLED_QUANTITY) TOTAL_QUANTITY,',
'        sum(COST_MY_COST_OVERAGE) OVERAGE_COST,',
'        sum(COST_MY_COST) USAGE_COST,',
'        sum(COST_MY_COST)*(24 * 31 / count(distinct USAGE_INTERVAL_START)) ESTIMATE_MONTH_31,',
'        sum(COST_MY_COST)*(24 * 365 / count(distinct USAGE_INTERVAL_START)) ESTIMATE_YEAR',
'    from oci_cost a',
'    where ',
'        tenant_name=:P4_TENANT_NAME and',
'        (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'        (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'        (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'        (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'        (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'        (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'        (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'        (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'        (:P4_COST_PRODUCT_SKU is null or a.COST_PRODUCT_SKU = :P4_COST_PRODUCT_SKU) and',
'        USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'')',
'        and COST_MY_COST<>0',
'        and :P4_REPORT_SELECTOR = ''Cost Report''',
'    group by ',
'        a.tenant_name,a.COST_PRODUCT_SKU , replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '','''')',
')',
'select ',
'    PRODUCT,',
'    COST_BILLING_UNIT,',
'    case when RATE_MONTHLY_FLEX_PRICE = 0 then null else RATE_MONTHLY_FLEX_PRICE end PUBLIC_RATE,',
'	CASE WHEN RATE_MONTHLY_FLEX_PRICE > 0  AND RATE_MONTHLY_FLEX_PRICE IS NOT NULL and RATE>0 THEN',
'	    ROUND((RATE_MONTHLY_FLEX_PRICE - RATE )/RATE_MONTHLY_FLEX_PRICE * 100,1)',
'	ELSE NULL END PCT_MONTH,',
'    RATE,',
'    CURRENCY,',
'    SINGLE_QUANTITY,',
'    HOURS_QUANTITY,',
'    TOTAL_QUANTITY,',
'    OVERAGE_COST,',
'    USAGE_COST,',
'    ESTIMATE_MONTH_31,',
'    ESTIMATE_YEAR',
'from',
'    data a,',
'    oci_price_list b',
'where    ',
'    a.tenant_name = b.tenant_name (+) and',
'    a.COST_PRODUCT_SKU = b.COST_PRODUCT_SKU (+)',
'order by USAGE_COST',
'',
''))
,p_plug_source_type=>'NATIVE_IR'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P4_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Cost Report'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet(
 p_id=>wwv_flow_api.id(11934457225191637)
,p_max_row_count=>'1000000'
,p_allow_save_rpt_public=>'Y'
,p_show_nulls_as=>'-'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_show_display_row_count=>'Y'
,p_report_list_mode=>'TABS'
,p_show_detail_link=>'N'
,p_show_rows_per_page=>'N'
,p_show_notify=>'Y'
,p_download_formats=>'CSV:HTML:EMAIL:XLSX:PDF:RTF'
,p_owner=>'ADI.ZOHAR@ORACLE.COM'
,p_internal_uid=>11934457225191637
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11934599799191638)
,p_db_column_name=>'PRODUCT'
,p_display_order=>10
,p_column_identifier=>'A'
,p_column_label=>'Product'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11934676427191639)
,p_db_column_name=>'COST_BILLING_UNIT'
,p_display_order=>20
,p_column_identifier=>'B'
,p_column_label=>'Cost Billing Unit'
,p_column_html_expression=>'<span style="white-space:nowrap;">#COST_BILLING_UNIT#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(14188271974270023)
,p_db_column_name=>'PUBLIC_RATE'
,p_display_order=>30
,p_column_identifier=>'L'
,p_column_label=>'Public Rate'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D000'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(14188353163270024)
,p_db_column_name=>'PCT_MONTH'
,p_display_order=>40
,p_column_identifier=>'M'
,p_column_label=>'% Discount'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D0'
,p_static_id=>'rep_col_pink'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11934736538191640)
,p_db_column_name=>'RATE'
,p_display_order=>50
,p_column_identifier=>'C'
,p_column_label=>'Customer Rate'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D000'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12552301614313321)
,p_db_column_name=>'CURRENCY'
,p_display_order=>60
,p_column_identifier=>'K'
,p_column_label=>'Cur'
,p_column_type=>'STRING'
,p_column_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11934801837191641)
,p_db_column_name=>'SINGLE_QUANTITY'
,p_display_order=>70
,p_column_identifier=>'D'
,p_column_label=>'Single Quantity'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D0'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11934932235191642)
,p_db_column_name=>'HOURS_QUANTITY'
,p_display_order=>80
,p_column_identifier=>'E'
,p_column_label=>'Hours Quantity'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D0'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11935047811191643)
,p_db_column_name=>'TOTAL_QUANTITY'
,p_display_order=>90
,p_column_identifier=>'F'
,p_column_label=>'Total Quantity'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D0'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11935139954191644)
,p_db_column_name=>'OVERAGE_COST'
,p_display_order=>100
,p_column_identifier=>'G'
,p_column_label=>'Overage Cost'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D000'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11935274061191645)
,p_db_column_name=>'USAGE_COST'
,p_display_order=>110
,p_column_identifier=>'H'
,p_column_label=>'Usage Cost'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D000'
,p_static_id=>'rep_col_grey'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11935309095191646)
,p_db_column_name=>'ESTIMATE_MONTH_31'
,p_display_order=>120
,p_column_identifier=>'I'
,p_column_label=>'Estimate Month 31'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
end;
/
begin
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11935491613191647)
,p_db_column_name=>'ESTIMATE_YEAR'
,p_display_order=>130
,p_column_identifier=>'J'
,p_column_label=>'Estimate Year'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_rpt(
 p_id=>wwv_flow_api.id(12264955888332662)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'122650'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'PRODUCT:COST_BILLING_UNIT:CURRENCY:PUBLIC_RATE:PCT_MONTH:RATE:SINGLE_QUANTITY:USAGE_COST:ESTIMATE_MONTH_31:ESTIMATE_YEAR:'
,p_sum_columns_on_break=>'OVERAGE_COST:USAGE_COST:ESTIMATE_MONTH_31:ESTIMATE_YEAR'
);
wwv_flow_api.create_worksheet_rpt(
 p_id=>wwv_flow_api.id(16442242263079381)
,p_application_user=>'APXWS_ALTERNATIVE'
,p_name=>'Compact'
,p_report_seq=>10
,p_report_alias=>'164423'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'PRODUCT:CURRENCY:PCT_MONTH:RATE:SINGLE_QUANTITY:OVERAGE_COST:USAGE_COST:ESTIMATE_MONTH_31:ESTIMATE_YEAR'
,p_sum_columns_on_break=>'OVERAGE_COST:USAGE_COST:ESTIMATE_MONTH_31:ESTIMATE_YEAR'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(21607460724513679)
,p_plug_name=>'Cost Per Single Compartment'
,p_parent_plug_id=>wwv_flow_api.id(21608843544513693)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>80
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P4_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Cost Per Single Compartment'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(11710134020773204)
,p_region_id=>wwv_flow_api.id(21607460724513679)
,p_chart_type=>'bar'
,p_height=>'700'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'horizontal'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_sorting=>'value-desc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'off'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(11711871269773205)
,p_chart_id=>wwv_flow_api.id(11710134020773204)
,p_seq=>10
,p_name=>'Cost per Single Compartment'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    nvl(prd_compartment_name,''No Compartment'') as prd_compartment_name,',
'    sum(COST_MY_COST) as COST_MY_COST',
'from oci_cost',
'where ',
'    tenant_name=:P4_TENANT_NAME and',
'    (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'    (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'    (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'    (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'    (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'    USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'') and',
'    (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'    (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'    (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'    COST_MY_COST>0 ',
'    and :P4_REPORT_SELECTOR = ''Cost Per Single Compartment''',
'group by ',
'	nvl(prd_compartment_name,''No Compartment'')',
'order by 2 desc',
'',
'',
'',
''))
,p_items_value_column_name=>'COST_MY_COST'
,p_items_label_column_name=>'PRD_COMPARTMENT_NAME'
,p_color=>'#34AADC'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'insideBarEdge'
,p_items_label_font_style=>'normal'
,p_items_label_font_size=>'8'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(11711229189773204)
,p_chart_id=>wwv_flow_api.id(11710134020773204)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(11710677057773204)
,p_chart_id=>wwv_flow_api.id(11710134020773204)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'none'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(21624153346489267)
,p_plug_name=>'Cost Per Region'
,p_parent_plug_id=>wwv_flow_api.id(21608843544513693)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>40
,p_plug_grid_column_span=>12
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P4_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Cost Per Region'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(11715360383773208)
,p_region_id=>wwv_flow_api.id(21624153346489267)
,p_chart_type=>'donut'
,p_height=>'400'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hover_behavior=>'dim'
,p_stack=>'off'
,p_stack_label=>'off'
,p_connect_nulls=>'Y'
,p_value_position=>'auto'
,p_value_format_type=>'decimal'
,p_value_decimal_places=>1
,p_value_format_scaling=>'auto'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_show_label=>true
,p_show_row=>true
,p_show_start=>true
,p_show_end=>true
,p_show_progress=>true
,p_show_baseline=>true
,p_legend_rendered=>'off'
,p_legend_position=>'auto'
,p_overview_rendered=>'off'
,p_pie_other_threshold=>0
,p_pie_selection_effect=>'highlight'
,p_horizontal_grid=>'auto'
,p_vertical_grid=>'auto'
,p_gauge_orientation=>'circular'
,p_gauge_plot_area=>'on'
,p_show_gauge_value=>true
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(11717080104773209)
,p_chart_id=>wwv_flow_api.id(11715360383773208)
,p_seq=>10
,p_name=>'Cost Per Region'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    prd_region, ',
'    sum(COST_MY_COST) as COST_MY_COST',
'from oci_cost',
'where ',
'    tenant_name=:P4_TENANT_NAME and',
'    (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'    (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'    (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'    (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'    (:P4_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P4_COST_PRODUCT_SKU) and',
'    (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'    (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'    (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'    (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'    USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'') and',
'    COST_MY_COST > 0',
'    and :P4_REPORT_SELECTOR = ''Cost Per Region''',
'group by ',
'	prd_region',
'order by 2 desc',
'',
'',
'',
''))
,p_series_name_column_name=>'PRD_REGION'
,p_items_value_column_name=>'COST_MY_COST'
,p_items_label_column_name=>'PRD_REGION'
,p_items_label_rendered=>true
,p_items_label_position=>'aboveMarker'
,p_items_label_display_as=>'ALL'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(21609013755513694)
,p_plug_name=>'Choose Tenant'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_source=>'No Data Found, Please Choose Tenant, Date and press Submit.'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'ITEM_IS_ZERO'
,p_plug_display_when_condition=>'P4_ROWS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_button(
 p_id=>wwv_flow_api.id(11702195950773187)
,p_button_sequence=>130
,p_button_plug_id=>wwv_flow_api.id(10816553122165737)
,p_button_name=>'P4_SUBMIT'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#:t-Button--large:t-Button--stretch:t-Button--gapTop'
,p_button_template_id=>wwv_flow_api.id(9821119233688096)
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Submit'
,p_button_position=>'BODY'
,p_grid_new_row=>'Y'
,p_grid_column_span=>3
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(10814789813165719)
,p_name=>'P4_COST_PRODUCT_SKU'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'Product SKU'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, substr(ref_name,1,6) r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P4_TENANT_NAME',
'    and ref_type=''COST_PRODUCT_SKU''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P4_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(10816373180165735)
,p_name=>'P4_DATE_FROM'
,p_is_required=>true
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'From Date'
,p_format_mask=>'DD-MON-YYYY HH24:MI'
,p_display_as=>'NATIVE_DATE_PICKER'
,p_cSize=>30
,p_tag_attributes=>'style="background-color:#e0f0f0"'
,p_begin_on_new_line=>'N'
,p_colspan=>3
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_02=>'01-JAN-2018'
,p_attribute_03=>'31-DEC-2025'
,p_attribute_04=>'button'
,p_attribute_05=>'N'
,p_attribute_07=>'MONTH_AND_YEAR'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(10816408250165736)
,p_name=>'P4_DATE_TO'
,p_is_required=>true
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'To Date (Not Inclusive)'
,p_format_mask=>'DD-MON-YYYY HH24:MI'
,p_display_as=>'NATIVE_DATE_PICKER'
,p_cSize=>30
,p_tag_attributes=>'style="background-color:#e0f0f0"'
,p_begin_on_new_line=>'N'
,p_colspan=>3
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_02=>'01-JAN-2018'
,p_attribute_03=>'31-DEC-2025'
,p_attribute_04=>'button'
,p_attribute_05=>'N'
,p_attribute_07=>'MONTH_AND_YEAR'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(10817497071165746)
,p_name=>'P4_FULL_DAYS_BETWEEN'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_api.id(10817046393165742)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Days of Data'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select to_char(count(*)/24,''99999.0'') DAYS',
'from',
'(',
'    select distinct',
'        USAGE_INTERVAL_START DATE_HOUR',
'    from oci_cost_stats',
'    where',
'        tenant_name=:P4_TENANT_NAME and',
'        USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'')',
')'))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_begin_on_new_line=>'N'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11702579323773190)
,p_name=>'P4_TENANT_NAME'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'Tenant Name'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'select distinct tenant_name o, tenant_name r from oci_cost order by 1'
,p_lov_display_null=>'YES'
,p_lov_null_text=>'Please Choose...'
,p_cHeight=>1
,p_tag_attributes=>'style="background-color:#e0f0f0"'
,p_colspan=>3
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11703393658773192)
,p_name=>'P4_COMPARTMENT_TOP'
,p_item_sequence=>100
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'Top Level Compartment'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P4_TENANT_NAME',
'    and ref_type=''PRD_COMPARTMENT_PATH''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P4_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11703792963773193)
,p_name=>'P4_PRODUCT_SERVICE'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'Product Service'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P4_TENANT_NAME',
'    and ref_type=''PRD_SERVICE''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P4_TENANT_NAME,P4_DATE_FROM, P4_DATE_TO'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11704568115773193)
,p_name=>'P4_ROWS'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_api.id(10817046393165742)
,p_format_mask=>'999G999G999G999G999G999G990'
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11704902453773194)
,p_name=>'P4_PRODUCT_REGION'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'Product Region'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P4_TENANT_NAME',
'    and ref_type=''PRD_REGION''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P4_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11705301552773194)
,p_name=>'P4_COMPARTMENT_NAME'
,p_item_sequence=>150
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'Compartment'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P4_TENANT_NAME',
'    and ref_type=''PRD_COMPARTMENT_NAME''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P4_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11706169664773195)
,p_name=>'P4_TAG_DATA'
,p_item_sequence=>120
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'Tag Data Filter'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>30
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'N'
,p_attribute_02=>'N'
,p_attribute_04=>'TEXT'
,p_attribute_05=>'BOTH'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11706547559773195)
,p_name=>'P4_LAST_DATE_LOADED'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_api.id(10817046393165742)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Last Date Loaded'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    to_char(max(USAGE_INTERVAL_START),''MM/DD/YY HH24:MI'') dte',
'from oci_cost_stats',
'where ',
'    tenant_name=:P4_TENANT_NAME'))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11790511673177238)
,p_name=>'P4_TAG_SPECIAL'
,p_item_sequence=>170
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'Tag Special Data'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P4_TENANT_NAME',
'    and ref_type=''TAG_SPECIAL''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P4_TENANT_NAME,P4_DATE_FROM, P4_DATE_TO'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11932857596191621)
,p_name=>'P4_COST'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(10817046393165742)
,p_prompt=>'Total Cost'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11933008339191623)
,p_name=>'P4_SUBSCRIPTION'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_api.id(10817046393165742)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Subscription Id'
,p_format_mask=>'FML999G999G999G999G990D00'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P4_TENANT_NAME',
'    and ref_type=''COST_SUBSCRIPTION_ID''',
'order by 1'))
,p_source_type=>'QUERY_COLON'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_begin_on_new_line=>'N'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11963890951367066)
,p_name=>'P4_TAG_KEY'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'Tag Key'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct tag_key o, tag_key r ',
'from ',
'    oci_cost_tag_keys',
'where',
'    tenant_name=:P4_TENANT_NAME',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P4_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11978704127439219)
,p_name=>'P4_TAG_SPECIAL_KEY_DISPLAY'
,p_item_sequence=>160
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Tag Special Key'
,p_format_mask=>'FML999G999G999G999G990D00'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P4_TENANT_NAME',
'    and ref_type=''TAG_SPECIAL_KEY''',
'order by 1'))
,p_source_type=>'QUERY_COLON'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_begin_on_new_line=>'N'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11979915795439231)
,p_name=>'P4_ROWS_DISPLAY'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_api.id(10817046393165742)
,p_prompt=>'Cost Rows Filtered'
,p_format_mask=>'999G999G999G999G999G999G990'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12305919376574231)
,p_name=>'P4_TENANT_ID'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'Tenant Id'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P4_TENANT_NAME',
'    and ref_type=''TENANT_ID''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P4_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_colspan=>3
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(13968875950017111)
,p_name=>'P4_REPORT_SELECTOR'
,p_item_sequence=>140
,p_item_plug_id=>wwv_flow_api.id(10816553122165737)
,p_prompt=>'Chart/Report Selector'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'STATIC2:Cost Per Day;Cost Per Day,Cost Per Day Accumulated;Cost Per Day Accumulated,Cost Per Region;Cost Per Region,Cost Per Service;Cost Per Service,Cost Per SKU;Cost Per SKU,Cost Per Top Compartment;Cost Per Top Compartment,Cost Per Single Compartm'
||'ent;Cost Per Single Compartment,Cost Per Tag Special;Cost Per Tag Special,Cost Report;Cost Report,Cost Explorer;Cost Explorer,Cost Resource Report;Cost Resource Report'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>3
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(14186142698270002)
,p_name=>'P4_YEARLY'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_api.id(10817046393165742)
,p_prompt=>'Yearly Prediction'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_begin_on_new_line=>'N'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(12277763069302644)
,p_computation_sequence=>5
,p_computation_item=>'P4_TENANT_NAME'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'QUERY'
,p_computation=>'select tenant_name from oci_cost where rownum=1'
,p_compute_when=>'P4_TENANT_NAME'
,p_compute_when_type=>'ITEM_IS_NULL'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(12277888687302645)
,p_computation_sequence=>10
,p_computation_item=>'P4_DATE_TO'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(max(trunc(USAGE_INTERVAL_START)),''DD-MON-YYYY HH24:MI'') from oci_cost_stats where tenant_name=:P4_TENANT_NAME'
,p_compute_when=>'P4_DATE_TO'
,p_compute_when_type=>'ITEM_IS_NULL'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(12277987624302646)
,p_computation_sequence=>10
,p_computation_item=>'P4_DATE_FROM'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'QUERY'
,p_computation=>'select to_Char(trunc(max(USAGE_INTERVAL_START)-7),''DD-MON-YYYY HH24:MI'') from oci_cost_stats where tenant_name=:P4_TENANT_NAME'
,p_compute_when=>'P4_DATE_FROM'
,p_compute_when_type=>'ITEM_IS_NULL'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(13973979841041416)
,p_computation_sequence=>10
,p_computation_item=>'P4_REPORT_SELECTOR'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'STATIC_ASSIGNMENT'
,p_computation=>'Cost Per Day'
,p_compute_when=>'P4_REPORT_SELECTOR'
,p_compute_when_type=>'ITEM_IS_NULL'
);
wwv_flow_api.create_page_process(
 p_id=>wwv_flow_api.id(11790470140177237)
,p_process_sequence=>10
,p_process_point=>'AFTER_HEADER'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'PreFill'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'begin',
'    select ',
'        to_char(nvl(sum(COST_MY_COST),0),''999,999,999,990.00'')||'' ''||min(COST_CURRENCY_CODE) MY_COST,',
'        to_char(nvl(sum(COST_MY_COST),0),''999,999,999,990'')||'' ''||min(COST_CURRENCY_CODE) MY_COST_YEAR,',
'        SUM(CNT) as TOTAL_ROWS,',
'        to_char(SUM(CNT),''999,999,999'') as TOTAL_ROWS',
'    into',
'        :P4_COST,',
'        :P4_YEARLY,',
'        :P4_ROWS,',
'        :P4_ROWS_DISPLAY',
'    from',
'    (',
'        select ',
'            sum(COST_MY_COST) COST_MY_COST,',
'            sum(COST_MY_COST)*(24 * 365 / count(distinct USAGE_INTERVAL_START)) COST_YEAR,',
'            min(COST_CURRENCY_CODE) COST_CURRENCY_CODE,',
'            count(*) cnt',
'        from oci_cost',
'        where ',
'            tenant_name=:P4_TENANT_NAME and',
'            (:P4_COMPARTMENT_NAME is null or prd_compartment_name = :P4_COMPARTMENT_NAME) and',
'            (:P4_PRODUCT_SERVICE is null or prd_service = :P4_PRODUCT_SERVICE) and',
'            (:P4_PRODUCT_REGION is null or prd_region = :P4_PRODUCT_REGION) and',
'            (:P4_TENANT_ID is null or tenant_id = :P4_TENANT_ID) and',
'            (:P4_COMPARTMENT_TOP is null or prd_compartment_path like :P4_COMPARTMENT_TOP ||''%'') and',
'            (:P4_TAG_KEY is null or tags_data like ''%#'' || :P4_TAG_KEY || ''=%'') and',
'            (:P4_TAG_DATA is null or tags_data like ''%#'' || nvl(:P4_TAG_KEY,''%'') || ''='' || :P4_TAG_DATA || ''#%'') and',
'            (:P4_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P4_COST_PRODUCT_SKU) and',
'            (:P4_TAG_SPECIAL is null or TAG_SPECIAL = :P4_TAG_SPECIAL) and',
'            USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'') and',
'            not (:P4_TENANT_ID is null and :P4_COMPARTMENT_NAME is null and :P4_PRODUCT_SERVICE is null and :P4_PRODUCT_REGION is null and :P4_COMPARTMENT_TOP is null and ',
'            :P4_TAG_KEY is null and :P4_TAG_DATA is null and :P4_COST_PRODUCT_SKU is null and :P4_TAG_SPECIAL is null)',
'        union all',
'        select ',
'            sum(COST_MY_COST) COST_MY_COST,',
'            sum(COST_MY_COST)*(24 * 365 / count(distinct USAGE_INTERVAL_START)) COST_YEAR,',
'            min(COST_CURRENCY_CODE) COST_CURRENCY_CODE,',
'            sum(num_rows) cnt',
'        from oci_cost_stats',
'        where ',
'            tenant_name=:P4_TENANT_NAME and',
'            USAGE_INTERVAL_START >= to_date(:P4_DATE_FROM,''DD-MON-YYYY HH24:MI'') and USAGE_INTERVAL_START < to_date(:P4_DATE_TO,''DD-MON-YYYY HH24:MI'') and',
'            (:P4_COMPARTMENT_NAME is null and :P4_PRODUCT_SERVICE is null and :P4_PRODUCT_REGION is null and :P4_COMPARTMENT_TOP is null and ',
'            :P4_TAG_KEY is null and :P4_TAG_DATA is null and :P4_COST_PRODUCT_SKU is null and :P4_TENANT_ID is null and :P4_TAG_SPECIAL is null)',
'    );',
'end;',
''))
,p_process_clob_language=>'PLSQL'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
);
end;
/
prompt --application/pages/page_00005
begin
wwv_flow_api.create_page(
 p_id=>5
,p_user_interface_id=>wwv_flow_api.id(9843694399688199)
,p_name=>'Cost Over Time'
,p_step_title=>'Cost Over Time'
,p_warn_on_unsaved_changes=>'N'
,p_autocomplete_on_off=>'OFF'
,p_inline_css=>wwv_flow_string.join(wwv_flow_t_varchar2(
'.a-IRR-table tr td[headers*="rep_col_grey"]',
'{',
'    background-color: #efffff;',
'}',
'',
'#P5_COST_DISPLAY{',
'  background-color: #F5FBB4; font-weight: bold; font-size: 14px;',
'}',
'#P5_YEARLY_DISPLAY{',
'  background-color: #F5FBB4; font-weight: bold; font-size: 14px;',
'}',
'#P5_REPORT_GROUP { background-color: #F5FBB4; }',
'#P5_INFO_DISPLAY {',
'  background-color: #FfFff0; font-size: 12px;',
'}',
'#P5_REPORT_SELECTOR { background-color: #F5FBB4; font-weight: bold; font-size: 13px;}',
'',
'#report .t-fht-thead{',
'  overflow: auto !important;',
'}',
''))
,p_page_template_options=>'#DEFAULT#'
,p_last_updated_by=>'ADIZOHAR'
,p_last_upd_yyyymmddhh24miss=>'20210329152118'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(22846551592241693)
,p_plug_name=>'Filter'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--accent12:t-Region--scrollBody:t-Form--noPadding:margin-top-none:margin-bottom-none:margin-left-none:margin-right-none'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_grid_column_span=>9
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(22847044863241698)
,p_plug_name=>'Stats Info'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--accent12:t-Region--scrollBody:margin-top-none:margin-bottom-none:margin-left-none:margin-right-none'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>20
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_new_grid_row=>false
,p_plug_grid_column_span=>3
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(33638842014589649)
,p_plug_name=>'ShowGraphs'
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding:t-Region--removeHeader:t-Region--noUI:t-Region--scrollBody:margin-top-none:margin-bottom-none:margin-left-none:margin-right-none'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>40
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'ITEM_IS_NOT_ZERO'
,p_plug_display_when_condition=>'P5_ROWS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_report_region(
 p_id=>wwv_flow_api.id(9926750244716139)
,p_name=>'Monthly Cost Report'
,p_region_name=>'report'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_template=>wwv_flow_api.id(9765042323688020)
,p_display_sequence=>90
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--altRowsDefault:t-Report--rowHighlight'
,p_display_point=>'BODY'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'SELECT ',
'	case ',
'		when :P5_REPORT_GROUP = ''Product'' or :P5_REPORT_GROUP is null then COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'')',
'		when :P5_REPORT_GROUP = ''Region'' then prd_region',
'		when :P5_REPORT_GROUP = ''Tag Special'' then tag_special',
'		when :P5_REPORT_GROUP = ''Top Compartment'' then ',
'			case ',
'                when prd_compartment_path is null then ''No Compartment''',
'                when prd_compartment_path like ''%/%'' then nvl(substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) ,''(Root)'')',
'                else prd_compartment_path ',
'            end ',
'		when :P5_REPORT_GROUP = ''Compartment'' then nvl(prd_compartment_name,''No Compartment'')',
'        when :P5_REPORT_GROUP = ''Tenant'' then nvl(tenant_id,''No TenantId'')',
'	end product_name,',
'    sum(COST_MY_COST) TOTAL,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''01'' then COST_MY_COST else null end) Jan,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''02'' then COST_MY_COST else null end) Feb,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''03'' then COST_MY_COST else null end) Mar,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''04'' then COST_MY_COST else null end) Apr,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''05'' then COST_MY_COST else null end) May,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''06'' then COST_MY_COST else null end) Jun,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''07'' then COST_MY_COST else null end) Jul,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''08'' then COST_MY_COST else null end) Aug,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''09'' then COST_MY_COST else null end) Sep,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''10'' then COST_MY_COST else null end) Oct,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''11'' then COST_MY_COST else null end) Nov,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''12'' then COST_MY_COST else null end) Dec',
'FROM ',
'    oci_cost ',
'WHERE ',
'    tenant_name=:P5_TENANT_NAME and',
'    :P5_PERIOD=''Monthly'' and ',
'	to_char(USAGE_INTERVAL_START,''YYYY'') = :P5_PERIOD_RANGE and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    :P5_REPORT_SELECTOR = ''Monthly Cost Report''',
'GROUP BY ',
'	case ',
'		when :P5_REPORT_GROUP = ''Product'' or :P5_REPORT_GROUP is null then COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'')',
'		when :P5_REPORT_GROUP = ''Region'' then prd_region',
'		when :P5_REPORT_GROUP = ''Tag Special'' then tag_special',
'		when :P5_REPORT_GROUP = ''Top Compartment'' then ',
'			case ',
'                when prd_compartment_path is null then ''No Compartment''',
'                when prd_compartment_path like ''%/%'' then nvl(substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) ,''(Root)'')',
'                else prd_compartment_path ',
'            end ',
'		when :P5_REPORT_GROUP = ''Compartment'' then nvl(prd_compartment_name,''No Compartment'')',
'        when :P5_REPORT_GROUP = ''Tenant'' then nvl(tenant_id,''No TenantId'')',
'	end',
'having sum(COST_MY_COST)>0;',
''))
,p_display_when_condition=>'P5_REPORT_SELECTOR'
,p_display_when_cond2=>'Monthly Cost Report'
,p_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_ajax_enabled=>'Y'
,p_query_row_template=>wwv_flow_api.id(9790776953688052)
,p_query_num_rows=>9999
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'Y'
,p_csv_output_link_text=>'Download'
,p_prn_output=>'Y'
,p_prn_format=>'PDF'
,p_prn_output_link_text=>'Print'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width_units=>'PERCENTAGE'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12090606356870207)
,p_query_column_id=>1
,p_column_alias=>'PRODUCT_NAME'
,p_column_display_sequence=>1
,p_column_heading=>'&P5_REPORT_GROUP.'
,p_use_as_row_header=>'N'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT_NAME#</span>'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12090747620870208)
,p_query_column_id=>2
,p_column_alias=>'TOTAL'
,p_column_display_sequence=>2
,p_column_heading=>'Total'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12090858100870209)
,p_query_column_id=>3
,p_column_alias=>'JAN'
,p_column_display_sequence=>3
,p_column_heading=>'Jan &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12090923679870210)
,p_query_column_id=>4
,p_column_alias=>'FEB'
,p_column_display_sequence=>4
,p_column_heading=>'Feb &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12091031376870211)
,p_query_column_id=>5
,p_column_alias=>'MAR'
,p_column_display_sequence=>5
,p_column_heading=>'Mar &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12091161924870212)
,p_query_column_id=>6
,p_column_alias=>'APR'
,p_column_display_sequence=>6
,p_column_heading=>'Apr &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12091282554870213)
,p_query_column_id=>7
,p_column_alias=>'MAY'
,p_column_display_sequence=>7
,p_column_heading=>'May &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12091301329870214)
,p_query_column_id=>8
,p_column_alias=>'JUN'
,p_column_display_sequence=>8
,p_column_heading=>'Jun &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12091498823870215)
,p_query_column_id=>9
,p_column_alias=>'JUL'
,p_column_display_sequence=>9
,p_column_heading=>'Jul &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12091521530870216)
,p_query_column_id=>10
,p_column_alias=>'AUG'
,p_column_display_sequence=>10
,p_column_heading=>'Aug &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12091680237870217)
,p_query_column_id=>11
,p_column_alias=>'SEP'
,p_column_display_sequence=>11
,p_column_heading=>'Sep &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12091726985870218)
,p_query_column_id=>12
,p_column_alias=>'OCT'
,p_column_display_sequence=>12
,p_column_heading=>'Oct &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12091864068870219)
,p_query_column_id=>13
,p_column_alias=>'NOV'
,p_column_display_sequence=>13
,p_column_heading=>'Nov &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12091943147870220)
,p_query_column_id=>14
,p_column_alias=>'DEC'
,p_column_display_sequence=>14
,p_column_heading=>'Dec &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_region(
 p_id=>wwv_flow_api.id(12092029867870221)
,p_name=>'Daily Cost Report'
,p_region_name=>'report'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_template=>wwv_flow_api.id(9765042323688020)
,p_display_sequence=>110
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--altRowsDefault:t-Report--rowHighlight'
,p_display_point=>'BODY'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'SELECT ',
'	case ',
'		when :P5_REPORT_GROUP = ''Product'' or :P5_REPORT_GROUP is null then COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'')',
'		when :P5_REPORT_GROUP = ''Region'' then prd_region',
'		when :P5_REPORT_GROUP = ''Tag Special'' then tag_special',
'		when :P5_REPORT_GROUP = ''Top Compartment'' then ',
'			case ',
'                when prd_compartment_path is null then ''No Compartment''',
'                when prd_compartment_path like ''%/%'' then nvl(substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) ,''(Root)'')',
'                else prd_compartment_path ',
'            end ',
'		when :P5_REPORT_GROUP = ''Compartment'' then nvl(prd_compartment_name,''No Compartment'')',
'		when :P5_REPORT_GROUP = ''Tenant'' then nvl(tenant_id,''No TenantId'')',
'	end product_name,',
'    sum(COST_MY_COST) TOTAL,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''01'' then COST_MY_COST else null end) D01,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''02'' then COST_MY_COST else null end) D02,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''03'' then COST_MY_COST else null end) D03,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''04'' then COST_MY_COST else null end) D04,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''05'' then COST_MY_COST else null end) D05,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''06'' then COST_MY_COST else null end) D06,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''07'' then COST_MY_COST else null end) D07,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''08'' then COST_MY_COST else null end) D08,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''09'' then COST_MY_COST else null end) D09,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''10'' then COST_MY_COST else null end) D10,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''11'' then COST_MY_COST else null end) D11,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''12'' then COST_MY_COST else null end) D12,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''13'' then COST_MY_COST else null end) D13,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''14'' then COST_MY_COST else null end) D14,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''15'' then COST_MY_COST else null end) D15,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''16'' then COST_MY_COST else null end) D16,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''17'' then COST_MY_COST else null end) D17,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''18'' then COST_MY_COST else null end) D18,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''19'' then COST_MY_COST else null end) D19,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''20'' then COST_MY_COST else null end) D20,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''21'' then COST_MY_COST else null end) D21,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''22'' then COST_MY_COST else null end) D22,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''23'' then COST_MY_COST else null end) D23,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''24'' then COST_MY_COST else null end) D24,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''25'' then COST_MY_COST else null end) D25,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''26'' then COST_MY_COST else null end) D26,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''27'' then COST_MY_COST else null end) D27,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''28'' then COST_MY_COST else null end) D28,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''29'' then COST_MY_COST else null end) D29,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''30'' then COST_MY_COST else null end) D30,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''31'' then COST_MY_COST else null end) D31',
'FROM ',
'    oci_cost ',
'WHERE ',
'    tenant_name=:P5_TENANT_NAME and',
'    :P5_PERIOD=''Daily'' and ',
'	to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    :P5_REPORT_SELECTOR = ''Daily Cost Report''',
'GROUP BY ',
'	case ',
'		when :P5_REPORT_GROUP = ''Product'' or :P5_REPORT_GROUP is null then COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'')',
'		when :P5_REPORT_GROUP = ''Region'' then prd_region',
'		when :P5_REPORT_GROUP = ''Tag Special'' then tag_special',
'		when :P5_REPORT_GROUP = ''Top Compartment'' then ',
'			case ',
'                when prd_compartment_path is null then ''No Compartment''',
'                when prd_compartment_path like ''%/%'' then nvl(substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) ,''(Root)'')',
'                else prd_compartment_path ',
'            end ',
'		when :P5_REPORT_GROUP = ''Compartment'' then nvl(prd_compartment_name,''No Compartment'')',
'        when :P5_REPORT_GROUP = ''Tenant'' then nvl(tenant_id,''No TenantId'')',
'	end',
'having sum(COST_MY_COST)>0;'))
,p_display_when_condition=>'P5_REPORT_SELECTOR'
,p_display_when_cond2=>'Daily Cost Report'
,p_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_ajax_enabled=>'Y'
,p_query_row_template=>wwv_flow_api.id(9790776953688052)
,p_query_num_rows=>9999
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'Y'
,p_csv_output_link_text=>'Download'
,p_prn_output=>'Y'
,p_prn_format=>'PDF'
,p_prn_output_link_text=>'Print'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width_units=>'PERCENTAGE'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12092237711870223)
,p_query_column_id=>1
,p_column_alias=>'PRODUCT_NAME'
,p_column_display_sequence=>1
,p_column_heading=>'&P5_REPORT_GROUP.'
,p_use_as_row_header=>'N'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT_NAME#</span>'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12092391544870224)
,p_query_column_id=>2
,p_column_alias=>'TOTAL'
,p_column_display_sequence=>2
,p_column_heading=>'Total'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12093692537870237)
,p_query_column_id=>3
,p_column_alias=>'D01'
,p_column_display_sequence=>3
,p_column_heading=>'D01'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12093750640870238)
,p_query_column_id=>4
,p_column_alias=>'D02'
,p_column_display_sequence=>4
,p_column_heading=>'D02'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12093827305870239)
,p_query_column_id=>5
,p_column_alias=>'D03'
,p_column_display_sequence=>5
,p_column_heading=>'D03'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12093976093870240)
,p_query_column_id=>6
,p_column_alias=>'D04'
,p_column_display_sequence=>6
,p_column_heading=>'D04'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12094088905870241)
,p_query_column_id=>7
,p_column_alias=>'D05'
,p_column_display_sequence=>7
,p_column_heading=>'D05'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12094124767870242)
,p_query_column_id=>8
,p_column_alias=>'D06'
,p_column_display_sequence=>8
,p_column_heading=>'D06'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12094229333870243)
,p_query_column_id=>9
,p_column_alias=>'D07'
,p_column_display_sequence=>9
,p_column_heading=>'D07'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12094342859870244)
,p_query_column_id=>10
,p_column_alias=>'D08'
,p_column_display_sequence=>10
,p_column_heading=>'D08'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12094440927870245)
,p_query_column_id=>11
,p_column_alias=>'D09'
,p_column_display_sequence=>11
,p_column_heading=>'D09'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12094515475870246)
,p_query_column_id=>12
,p_column_alias=>'D10'
,p_column_display_sequence=>12
,p_column_heading=>'D10'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12094663202870247)
,p_query_column_id=>13
,p_column_alias=>'D11'
,p_column_display_sequence=>13
,p_column_heading=>'D11'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12094735623870248)
,p_query_column_id=>14
,p_column_alias=>'D12'
,p_column_display_sequence=>14
,p_column_heading=>'D12'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12094845760870249)
,p_query_column_id=>15
,p_column_alias=>'D13'
,p_column_display_sequence=>15
,p_column_heading=>'D13'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12094998665870250)
,p_query_column_id=>16
,p_column_alias=>'D14'
,p_column_display_sequence=>16
,p_column_heading=>'D14'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12139678917985901)
,p_query_column_id=>17
,p_column_alias=>'D15'
,p_column_display_sequence=>17
,p_column_heading=>'D15'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12139735715985902)
,p_query_column_id=>18
,p_column_alias=>'D16'
,p_column_display_sequence=>18
,p_column_heading=>'D16'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12139895368985903)
,p_query_column_id=>19
,p_column_alias=>'D17'
,p_column_display_sequence=>19
,p_column_heading=>'D17'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12139987734985904)
,p_query_column_id=>20
,p_column_alias=>'D18'
,p_column_display_sequence=>20
,p_column_heading=>'D18'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12140020957985905)
,p_query_column_id=>21
,p_column_alias=>'D19'
,p_column_display_sequence=>21
,p_column_heading=>'D19'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12140163374985906)
,p_query_column_id=>22
,p_column_alias=>'D20'
,p_column_display_sequence=>22
,p_column_heading=>'D20'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
end;
/
begin
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12140258272985907)
,p_query_column_id=>23
,p_column_alias=>'D21'
,p_column_display_sequence=>23
,p_column_heading=>'D21'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12140321246985908)
,p_query_column_id=>24
,p_column_alias=>'D22'
,p_column_display_sequence=>24
,p_column_heading=>'D22'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12140479961985909)
,p_query_column_id=>25
,p_column_alias=>'D23'
,p_column_display_sequence=>25
,p_column_heading=>'D23'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12140504386985910)
,p_query_column_id=>26
,p_column_alias=>'D24'
,p_column_display_sequence=>26
,p_column_heading=>'D24'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12140643012985911)
,p_query_column_id=>27
,p_column_alias=>'D25'
,p_column_display_sequence=>27
,p_column_heading=>'D25'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12140790548985912)
,p_query_column_id=>28
,p_column_alias=>'D26'
,p_column_display_sequence=>28
,p_column_heading=>'D26'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12140854110985913)
,p_query_column_id=>29
,p_column_alias=>'D27'
,p_column_display_sequence=>29
,p_column_heading=>'D27'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12140946436985914)
,p_query_column_id=>30
,p_column_alias=>'D28'
,p_column_display_sequence=>30
,p_column_heading=>'D28'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12141064503985915)
,p_query_column_id=>31
,p_column_alias=>'D29'
,p_column_display_sequence=>31
,p_column_heading=>'D29'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12141108047985916)
,p_query_column_id=>32
,p_column_alias=>'D30'
,p_column_display_sequence=>32
,p_column_heading=>'D30'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12141293941985917)
,p_query_column_id=>33
,p_column_alias=>'D31'
,p_column_display_sequence=>33
,p_column_heading=>'D31'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_region(
 p_id=>wwv_flow_api.id(12268418584281501)
,p_name=>'Weekly Cost Report'
,p_region_name=>'report'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_template=>wwv_flow_api.id(9765042323688020)
,p_display_sequence=>160
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--altRowsDefault:t-Report--rowHighlight'
,p_display_point=>'BODY'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
' SELECT ',
'	case ',
'		when :P5_REPORT_GROUP = ''Product'' or :P5_REPORT_GROUP is null then COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'')',
'		when :P5_REPORT_GROUP = ''Region'' then prd_region',
'		when :P5_REPORT_GROUP = ''Tag Special'' then tag_special',
'		when :P5_REPORT_GROUP = ''Top Compartment'' then ',
'			case ',
'                when prd_compartment_path is null then ''No Compartment''',
'                when prd_compartment_path like ''%/%'' then nvl(substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) ,''(Root)'')',
'                else prd_compartment_path ',
'            end ',
'		when :P5_REPORT_GROUP = ''Compartment'' then nvl(prd_compartment_name,''No Compartment'')',
'        when :P5_REPORT_GROUP = ''Tenant'' then nvl(tenant_id,''No TenantId'')',
'	end product_name,',
'    sum(COST_MY_COST) TOTAL,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''01'' then COST_MY_COST else null end) W01,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''02'' then COST_MY_COST else null end) W02,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''03'' then COST_MY_COST else null end) W03,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''04'' then COST_MY_COST else null end) W04,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''05'' then COST_MY_COST else null end) W05,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''06'' then COST_MY_COST else null end) W06,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''07'' then COST_MY_COST else null end) W07,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''08'' then COST_MY_COST else null end) W08,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''09'' then COST_MY_COST else null end) W09,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''10'' then COST_MY_COST else null end) W10,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''11'' then COST_MY_COST else null end) W11,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''12'' then COST_MY_COST else null end) W12,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''13'' then COST_MY_COST else null end) W13,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''14'' then COST_MY_COST else null end) W14,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''15'' then COST_MY_COST else null end) W15,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''16'' then COST_MY_COST else null end) W16,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''17'' then COST_MY_COST else null end) W17,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''18'' then COST_MY_COST else null end) W18,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''19'' then COST_MY_COST else null end) W19,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''20'' then COST_MY_COST else null end) W20,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''21'' then COST_MY_COST else null end) W21,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''22'' then COST_MY_COST else null end) W22,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''23'' then COST_MY_COST else null end) W23,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''24'' then COST_MY_COST else null end) W24,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''25'' then COST_MY_COST else null end) W25,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''26'' then COST_MY_COST else null end) W26,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''27'' then COST_MY_COST else null end) W27,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''28'' then COST_MY_COST else null end) W28,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''29'' then COST_MY_COST else null end) W29,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''30'' then COST_MY_COST else null end) W30,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''31'' then COST_MY_COST else null end) W31,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''32'' then COST_MY_COST else null end) W32,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''33'' then COST_MY_COST else null end) W33,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''34'' then COST_MY_COST else null end) W34,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''35'' then COST_MY_COST else null end) W35,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''36'' then COST_MY_COST else null end) W36,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''37'' then COST_MY_COST else null end) W37,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''38'' then COST_MY_COST else null end) W38,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''39'' then COST_MY_COST else null end) W39,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''40'' then COST_MY_COST else null end) W40,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''41'' then COST_MY_COST else null end) W41,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''42'' then COST_MY_COST else null end) W42,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''43'' then COST_MY_COST else null end) W43,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''44'' then COST_MY_COST else null end) W44,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''45'' then COST_MY_COST else null end) W45,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''46'' then COST_MY_COST else null end) W46,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''47'' then COST_MY_COST else null end) W47,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''48'' then COST_MY_COST else null end) W48,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''49'' then COST_MY_COST else null end) W49,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''50'' then COST_MY_COST else null end) W50,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''51'' then COST_MY_COST else null end) W51,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''52'' then COST_MY_COST else null end) W52',
'from',
'    oci_cost ',
'WHERE ',
'    tenant_name=:P5_TENANT_NAME and',
'    :P5_PERIOD=''Weekly'' and ',
'	to_char(USAGE_INTERVAL_START,''YYYY'') = :P5_PERIOD_RANGE and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    :P5_REPORT_SELECTOR = ''Weekly Cost Report''',
'GROUP BY ',
'	case ',
'		when :P5_REPORT_GROUP = ''Product'' or :P5_REPORT_GROUP is null then COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'')',
'		when :P5_REPORT_GROUP = ''Region'' then prd_region',
'		when :P5_REPORT_GROUP = ''Tag Special'' then tag_special',
'		when :P5_REPORT_GROUP = ''Top Compartment'' then ',
'			case ',
'                when prd_compartment_path is null then ''No Compartment''',
'                when prd_compartment_path like ''%/%'' then nvl(substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) ,''(Root)'')',
'                else prd_compartment_path ',
'            end ',
'		when :P5_REPORT_GROUP = ''Compartment'' then nvl(prd_compartment_name,''No Compartment'')',
'        when :P5_REPORT_GROUP = ''Tenant'' then nvl(tenant_id,''No TenantId'')',
'	end',
'having sum(COST_MY_COST)>0;'))
,p_display_when_condition=>'P5_REPORT_SELECTOR'
,p_display_when_cond2=>'Weekly Cost Report'
,p_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_ajax_enabled=>'Y'
,p_query_row_template=>wwv_flow_api.id(9790776953688052)
,p_query_num_rows=>9999
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'Y'
,p_csv_output_link_text=>'Download'
,p_prn_output=>'Y'
,p_prn_format=>'PDF'
,p_prn_output_link_text=>'Print'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width_units=>'PERCENTAGE'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12268590997281502)
,p_query_column_id=>1
,p_column_alias=>'PRODUCT_NAME'
,p_column_display_sequence=>1
,p_column_heading=>'&P5_REPORT_GROUP.'
,p_use_as_row_header=>'N'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT_NAME#</span>'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12268609294281503)
,p_query_column_id=>2
,p_column_alias=>'TOTAL'
,p_column_display_sequence=>2
,p_column_heading=>'Total'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12271849943281535)
,p_query_column_id=>3
,p_column_alias=>'W01'
,p_column_display_sequence=>3
,p_column_heading=>'W01'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12271922117281536)
,p_query_column_id=>4
,p_column_alias=>'W02'
,p_column_display_sequence=>4
,p_column_heading=>'W02'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12272064052281537)
,p_query_column_id=>5
,p_column_alias=>'W03'
,p_column_display_sequence=>5
,p_column_heading=>'W03'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12272113865281538)
,p_query_column_id=>6
,p_column_alias=>'W04'
,p_column_display_sequence=>6
,p_column_heading=>'W04'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12272243446281539)
,p_query_column_id=>7
,p_column_alias=>'W05'
,p_column_display_sequence=>7
,p_column_heading=>'W05'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12272385986281540)
,p_query_column_id=>8
,p_column_alias=>'W06'
,p_column_display_sequence=>8
,p_column_heading=>'W06'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12272403641281541)
,p_query_column_id=>9
,p_column_alias=>'W07'
,p_column_display_sequence=>9
,p_column_heading=>'W07'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12272581297281542)
,p_query_column_id=>10
,p_column_alias=>'W08'
,p_column_display_sequence=>10
,p_column_heading=>'W08'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12272666822281543)
,p_query_column_id=>11
,p_column_alias=>'W09'
,p_column_display_sequence=>11
,p_column_heading=>'W09'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12272781545281544)
,p_query_column_id=>12
,p_column_alias=>'W10'
,p_column_display_sequence=>12
,p_column_heading=>'W10'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12272800678281545)
,p_query_column_id=>13
,p_column_alias=>'W11'
,p_column_display_sequence=>13
,p_column_heading=>'W11'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12272954271281546)
,p_query_column_id=>14
,p_column_alias=>'W12'
,p_column_display_sequence=>14
,p_column_heading=>'W12'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12273090465281547)
,p_query_column_id=>15
,p_column_alias=>'W13'
,p_column_display_sequence=>15
,p_column_heading=>'W13'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12273100018281548)
,p_query_column_id=>16
,p_column_alias=>'W14'
,p_column_display_sequence=>16
,p_column_heading=>'W14'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12273274284281549)
,p_query_column_id=>17
,p_column_alias=>'W15'
,p_column_display_sequence=>17
,p_column_heading=>'W15'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12273314693281550)
,p_query_column_id=>18
,p_column_alias=>'W16'
,p_column_display_sequence=>18
,p_column_heading=>'W16'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12273417671302601)
,p_query_column_id=>19
,p_column_alias=>'W17'
,p_column_display_sequence=>19
,p_column_heading=>'W17'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12273518738302602)
,p_query_column_id=>20
,p_column_alias=>'W18'
,p_column_display_sequence=>20
,p_column_heading=>'W18'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12273631791302603)
,p_query_column_id=>21
,p_column_alias=>'W19'
,p_column_display_sequence=>21
,p_column_heading=>'W19'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12273722103302604)
,p_query_column_id=>22
,p_column_alias=>'W20'
,p_column_display_sequence=>22
,p_column_heading=>'W20'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12273856019302605)
,p_query_column_id=>23
,p_column_alias=>'W21'
,p_column_display_sequence=>23
,p_column_heading=>'W21'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12273912482302606)
,p_query_column_id=>24
,p_column_alias=>'W22'
,p_column_display_sequence=>24
,p_column_heading=>'W22'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12274009294302607)
,p_query_column_id=>25
,p_column_alias=>'W23'
,p_column_display_sequence=>25
,p_column_heading=>'W23'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12274156886302608)
,p_query_column_id=>26
,p_column_alias=>'W24'
,p_column_display_sequence=>26
,p_column_heading=>'W24'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12274252620302609)
,p_query_column_id=>27
,p_column_alias=>'W25'
,p_column_display_sequence=>27
,p_column_heading=>'W25'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12274346901302610)
,p_query_column_id=>28
,p_column_alias=>'W26'
,p_column_display_sequence=>28
,p_column_heading=>'W26'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12274492299302611)
,p_query_column_id=>29
,p_column_alias=>'W27'
,p_column_display_sequence=>29
,p_column_heading=>'W27'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12274596332302612)
,p_query_column_id=>30
,p_column_alias=>'W28'
,p_column_display_sequence=>30
,p_column_heading=>'W28'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12274617770302613)
,p_query_column_id=>31
,p_column_alias=>'W29'
,p_column_display_sequence=>31
,p_column_heading=>'W29'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12274731414302614)
,p_query_column_id=>32
,p_column_alias=>'W30'
,p_column_display_sequence=>32
,p_column_heading=>'W30'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12274880307302615)
,p_query_column_id=>33
,p_column_alias=>'W31'
,p_column_display_sequence=>33
,p_column_heading=>'W31'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12274918064302616)
,p_query_column_id=>34
,p_column_alias=>'W32'
,p_column_display_sequence=>34
,p_column_heading=>'W32'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12275037247302617)
,p_query_column_id=>35
,p_column_alias=>'W33'
,p_column_display_sequence=>35
,p_column_heading=>'W33'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12275100382302618)
,p_query_column_id=>36
,p_column_alias=>'W34'
,p_column_display_sequence=>36
,p_column_heading=>'W34'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12275206549302619)
,p_query_column_id=>37
,p_column_alias=>'W35'
,p_column_display_sequence=>37
,p_column_heading=>'W35'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12275390261302620)
,p_query_column_id=>38
,p_column_alias=>'W36'
,p_column_display_sequence=>38
,p_column_heading=>'W36'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12275471481302621)
,p_query_column_id=>39
,p_column_alias=>'W37'
,p_column_display_sequence=>39
,p_column_heading=>'W37'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12275571350302622)
,p_query_column_id=>40
,p_column_alias=>'W38'
,p_column_display_sequence=>40
,p_column_heading=>'W38'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12275692242302623)
,p_query_column_id=>41
,p_column_alias=>'W39'
,p_column_display_sequence=>41
,p_column_heading=>'W39'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12275746424302624)
,p_query_column_id=>42
,p_column_alias=>'W40'
,p_column_display_sequence=>42
,p_column_heading=>'W40'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12275841433302625)
,p_query_column_id=>43
,p_column_alias=>'W41'
,p_column_display_sequence=>43
,p_column_heading=>'W41'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12275927638302626)
,p_query_column_id=>44
,p_column_alias=>'W42'
,p_column_display_sequence=>44
,p_column_heading=>'W42'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12276079598302627)
,p_query_column_id=>45
,p_column_alias=>'W43'
,p_column_display_sequence=>45
,p_column_heading=>'W43'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12276169395302628)
,p_query_column_id=>46
,p_column_alias=>'W44'
,p_column_display_sequence=>46
,p_column_heading=>'W44'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12276235425302629)
,p_query_column_id=>47
,p_column_alias=>'W45'
,p_column_display_sequence=>47
,p_column_heading=>'W45'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12276379436302630)
,p_query_column_id=>48
,p_column_alias=>'W46'
,p_column_display_sequence=>48
,p_column_heading=>'W46'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
end;
/
begin
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12276461513302631)
,p_query_column_id=>49
,p_column_alias=>'W47'
,p_column_display_sequence=>49
,p_column_heading=>'W47'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12276525506302632)
,p_query_column_id=>50
,p_column_alias=>'W48'
,p_column_display_sequence=>50
,p_column_heading=>'W48'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12276645471302633)
,p_query_column_id=>51
,p_column_alias=>'W49'
,p_column_display_sequence=>51
,p_column_heading=>'W49'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12276782464302634)
,p_query_column_id=>52
,p_column_alias=>'W50'
,p_column_display_sequence=>52
,p_column_heading=>'W50'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12276887785302635)
,p_query_column_id=>53
,p_column_alias=>'W51'
,p_column_display_sequence=>53
,p_column_heading=>'W51'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12276941950302636)
,p_query_column_id=>54
,p_column_alias=>'W52'
,p_column_display_sequence=>54
,p_column_heading=>'W52'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_region(
 p_id=>wwv_flow_api.id(12278275925302649)
,p_name=>'Daily Product Unit Report - Single'
,p_region_name=>'report'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_template=>wwv_flow_api.id(9765042323688020)
,p_display_sequence=>130
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--altRowsDefault:t-Report--rowHighlight'
,p_display_point=>'BODY'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
' SELECT ',
'	product_name,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''01'' then SINGLE_QUANTITY else null end) D01,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''02'' then SINGLE_QUANTITY else null end) D02,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''03'' then SINGLE_QUANTITY else null end) D03,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''04'' then SINGLE_QUANTITY else null end) D04,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''05'' then SINGLE_QUANTITY else null end) D05,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''06'' then SINGLE_QUANTITY else null end) D06,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''07'' then SINGLE_QUANTITY else null end) D07,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''08'' then SINGLE_QUANTITY else null end) D08,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''09'' then SINGLE_QUANTITY else null end) D09,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''10'' then SINGLE_QUANTITY else null end) D10,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''11'' then SINGLE_QUANTITY else null end) D11,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''12'' then SINGLE_QUANTITY else null end) D12,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''13'' then SINGLE_QUANTITY else null end) D13,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''14'' then SINGLE_QUANTITY else null end) D14,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''15'' then SINGLE_QUANTITY else null end) D15,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''16'' then SINGLE_QUANTITY else null end) D16,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''17'' then SINGLE_QUANTITY else null end) D17,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''18'' then SINGLE_QUANTITY else null end) D18,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''19'' then SINGLE_QUANTITY else null end) D19,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''20'' then SINGLE_QUANTITY else null end) D20,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''21'' then SINGLE_QUANTITY else null end) D21,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''22'' then SINGLE_QUANTITY else null end) D22,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''23'' then SINGLE_QUANTITY else null end) D23,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''24'' then SINGLE_QUANTITY else null end) D24,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''25'' then SINGLE_QUANTITY else null end) D25,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''26'' then SINGLE_QUANTITY else null end) D26,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''27'' then SINGLE_QUANTITY else null end) D27,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''28'' then SINGLE_QUANTITY else null end) D28,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''29'' then SINGLE_QUANTITY else null end) D29,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''30'' then SINGLE_QUANTITY else null end) D30,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''31'' then SINGLE_QUANTITY else null end) D31',
'FROM ',
'(',
'	SELECT ',
'		COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'') PRODUCT_NAME,',
'		USAGE_INTERVAL_START,',
'		case ',
'			when upper(PRD_DESCRIPTION) like ''%HOUR%'' then USG_BILLED_QUANTITY/24',
'			when upper(COST_BILLING_UNIT) like ''%HOUR%'' then USG_BILLED_QUANTITY/24',
'			when upper(COST_BILLING_UNIT) like ''%GIB%'' then USG_BILLED_QUANTITY*31',
'			when upper(COST_BILLING_UNIT) like ''%GB%'' then USG_BILLED_QUANTITY*31',
'			when upper(COST_BILLING_UNIT) like ''%GIGA%'' then USG_BILLED_QUANTITY*31',
'			when upper(COST_BILLING_UNIT) like ''%TIB%'' then USG_BILLED_QUANTITY*31',
'			when upper(PRD_DESCRIPTION) like ''%GiB%'' then USG_BILLED_QUANTITY*31',
'			when upper(PRD_DESCRIPTION) like ''%GB%'' then USG_BILLED_QUANTITY*31',
'			when upper(PRD_DESCRIPTION) like ''%GIGA%'' then USG_BILLED_QUANTITY*31',
'			when upper(PRD_DESCRIPTION) like ''%TIB%'' then USG_BILLED_QUANTITY*31',
'			when upper(PRD_DESCRIPTION) like ''%TB%'' then USG_BILLED_QUANTITY*31',
'			else null',
'		end SINGLE_QUANTITY',
'	FROM',
'    	oci_cost ',
'	WHERE ',
'		tenant_name=:P5_TENANT_NAME and',
'		:P5_PERIOD=''Daily'' and ',
'		to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE and',
'		(:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'		(:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'		(:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'		(:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'        (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'		(:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'        (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'		(:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'		(:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') AND',
'        :P5_REPORT_SELECTOR = ''Daily Product Unit Report - Single''',
')',
'GROUP BY PRODUCT_NAME',
'having sum(SINGLE_QUANTITY)>0;'))
,p_display_when_condition=>'P5_REPORT_SELECTOR'
,p_display_when_cond2=>'Daily Product Unit Report - Single'
,p_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_ajax_enabled=>'Y'
,p_query_row_template=>wwv_flow_api.id(9790776953688052)
,p_query_num_rows=>9999
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'Y'
,p_csv_output_link_text=>'Download'
,p_prn_output=>'Y'
,p_prn_format=>'PDF'
,p_prn_output_link_text=>'Print'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width_units=>'PERCENTAGE'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12278312242302650)
,p_query_column_id=>1
,p_column_alias=>'PRODUCT_NAME'
,p_column_display_sequence=>1
,p_column_heading=>'Product'
,p_use_as_row_header=>'N'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT_NAME#</span>'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12313806573646702)
,p_query_column_id=>2
,p_column_alias=>'D01'
,p_column_display_sequence=>2
,p_column_heading=>'D01'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12313930619646703)
,p_query_column_id=>3
,p_column_alias=>'D02'
,p_column_display_sequence=>3
,p_column_heading=>'D02'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12314024970646704)
,p_query_column_id=>4
,p_column_alias=>'D03'
,p_column_display_sequence=>4
,p_column_heading=>'D03'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12314142295646705)
,p_query_column_id=>5
,p_column_alias=>'D04'
,p_column_display_sequence=>5
,p_column_heading=>'D04'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12314272931646706)
,p_query_column_id=>6
,p_column_alias=>'D05'
,p_column_display_sequence=>6
,p_column_heading=>'D05'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12314395490646707)
,p_query_column_id=>7
,p_column_alias=>'D06'
,p_column_display_sequence=>7
,p_column_heading=>'D06'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12314429071646708)
,p_query_column_id=>8
,p_column_alias=>'D07'
,p_column_display_sequence=>8
,p_column_heading=>'D07'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12314554865646709)
,p_query_column_id=>9
,p_column_alias=>'D08'
,p_column_display_sequence=>9
,p_column_heading=>'D08'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12314646673646710)
,p_query_column_id=>10
,p_column_alias=>'D09'
,p_column_display_sequence=>10
,p_column_heading=>'D09'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12314709889646711)
,p_query_column_id=>11
,p_column_alias=>'D10'
,p_column_display_sequence=>11
,p_column_heading=>'D10'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12314867891646712)
,p_query_column_id=>12
,p_column_alias=>'D11'
,p_column_display_sequence=>12
,p_column_heading=>'D11'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12314914340646713)
,p_query_column_id=>13
,p_column_alias=>'D12'
,p_column_display_sequence=>13
,p_column_heading=>'D12'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12315044130646714)
,p_query_column_id=>14
,p_column_alias=>'D13'
,p_column_display_sequence=>14
,p_column_heading=>'D13'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12315198189646715)
,p_query_column_id=>15
,p_column_alias=>'D14'
,p_column_display_sequence=>15
,p_column_heading=>'D14'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12315242353646716)
,p_query_column_id=>16
,p_column_alias=>'D15'
,p_column_display_sequence=>16
,p_column_heading=>'D15'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12315389787646717)
,p_query_column_id=>17
,p_column_alias=>'D16'
,p_column_display_sequence=>17
,p_column_heading=>'D16'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12315413076646718)
,p_query_column_id=>18
,p_column_alias=>'D17'
,p_column_display_sequence=>18
,p_column_heading=>'D17'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12315521712646719)
,p_query_column_id=>19
,p_column_alias=>'D18'
,p_column_display_sequence=>19
,p_column_heading=>'D18'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12315656693646720)
,p_query_column_id=>20
,p_column_alias=>'D19'
,p_column_display_sequence=>20
,p_column_heading=>'D19'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12315765218646721)
,p_query_column_id=>21
,p_column_alias=>'D20'
,p_column_display_sequence=>21
,p_column_heading=>'D20'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12315886293646722)
,p_query_column_id=>22
,p_column_alias=>'D21'
,p_column_display_sequence=>22
,p_column_heading=>'D21'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12315903959646723)
,p_query_column_id=>23
,p_column_alias=>'D22'
,p_column_display_sequence=>23
,p_column_heading=>'D22'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12316089237646724)
,p_query_column_id=>24
,p_column_alias=>'D23'
,p_column_display_sequence=>24
,p_column_heading=>'D23'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12316110465646725)
,p_query_column_id=>25
,p_column_alias=>'D24'
,p_column_display_sequence=>25
,p_column_heading=>'D24'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12316267637646726)
,p_query_column_id=>26
,p_column_alias=>'D25'
,p_column_display_sequence=>26
,p_column_heading=>'D25'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12316333791646727)
,p_query_column_id=>27
,p_column_alias=>'D26'
,p_column_display_sequence=>27
,p_column_heading=>'D26'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12316474340646728)
,p_query_column_id=>28
,p_column_alias=>'D27'
,p_column_display_sequence=>28
,p_column_heading=>'D27'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12316584562646729)
,p_query_column_id=>29
,p_column_alias=>'D28'
,p_column_display_sequence=>29
,p_column_heading=>'D28'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12316632025646730)
,p_query_column_id=>30
,p_column_alias=>'D29'
,p_column_display_sequence=>30
,p_column_heading=>'D29'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12316744797646731)
,p_query_column_id=>31
,p_column_alias=>'D30'
,p_column_display_sequence=>31
,p_column_heading=>'D30'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(12316880220646732)
,p_query_column_id=>32
,p_column_alias=>'D31'
,p_column_display_sequence=>32
,p_column_heading=>'D31'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(13976669023041443)
,p_plug_name=>'Cost Over Time - Total - &P5_PERIOD.'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>30
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VALUE_OF_ITEM_IN_CONDITION_IN_COLON_DELIMITED_LIST'
,p_plug_display_when_condition=>'P5_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Hourly Cost Over Time - Total:Daily Cost Over Time - Total:Weekly Cost Over Time - Total:Monthly Cost Over Time - Total'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(13976741456041444)
,p_region_id=>wwv_flow_api.id(13976669023041443)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'off'
,p_connect_nulls=>'Y'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(13976866910041445)
,p_chart_id=>wwv_flow_api.id(13976741456041444)
,p_seq=>10
,p_name=>'Usage'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end PERIOD,',
'    sum(COST_MY_COST) as COST_USAGE',
'from oci_cost',
'where ',
'    tenant_name=:P5_TENANT_NAME and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YY'
||'YY'') = :P5_PERIOD_RANGE) and',
'    not (:P5_TAG_SPECIAL is null and :P5_TENANT_ID is null and :P5_COMPARTMENT_NAME is null and :P5_PRODUCT_SERVICE is null and :P5_PRODUCT_REGION is null and :P5_COMPARTMENT_TOP is null and :P5_TAG_KEY is null and :P5_TAG_DATA is null and :P5_COST_P'
||'RODUCT_SKU is null) and',
'    :P5_REPORT_SELECTOR in (''Hourly Cost Over Time - Total'',''Daily Cost Over Time - Total'',''Weekly Cost Over Time - Total'',''Monthly Cost Over Time - Total'')    ',
'    group by ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end',
'union all',
'select ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end PERIOD,',
'    sum(COST_MY_COST) as COST_USAGE',
'from oci_cost_stats',
'where ',
'    tenant_name=:P5_TENANT_NAME and',
'    (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YY'
||'YY'') = :P5_PERIOD_RANGE) and',
'    (:P5_TAG_SPECIAL is null and :P5_TENANT_ID is null and :P5_COMPARTMENT_NAME is null and :P5_PRODUCT_SERVICE is null and :P5_PRODUCT_REGION is null and :P5_COMPARTMENT_TOP is null and :P5_TAG_KEY is null and :P5_TAG_DATA is null and :P5_COST_PRODU'
||'CT_SKU is null) and',
'    :P5_REPORT_SELECTOR in (''Hourly Cost Over Time - Total'',''Daily Cost Over Time - Total'',''Weekly Cost Over Time - Total'',''Monthly Cost Over Time - Total'')    ',
'    group by ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end',
'order by 1',
'',
'',
'',
''))
,p_items_value_column_name=>'COST_USAGE'
,p_items_label_column_name=>'PERIOD'
,p_color=>'#34AADC'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'center'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(13977078966041447)
,p_chart_id=>wwv_flow_api.id(13976741456041444)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_type=>'date-short'
,p_numeric_pattern=>'DD-MON-YYYY'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(13977108905041448)
,p_chart_id=>wwv_flow_api.id(13976741456041444)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(14186462781270005)
,p_plug_name=>'Cost By Region - &P5_PERIOD.'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>70
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VALUE_OF_ITEM_IN_CONDITION_IN_COLON_DELIMITED_LIST'
,p_plug_display_when_condition=>'P5_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Hourly Cost By Region:Daily Cost By Region:Weekly Cost By Region:Monthly Cost By Region'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(14186570488270006)
,p_region_id=>wwv_flow_api.id(14186462781270005)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'on'
,p_legend_position=>'end'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(14186672156270007)
,p_chart_id=>wwv_flow_api.id(14186570488270006)
,p_seq=>10
,p_name=>'Usage'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end PERIOD,',
'    prd_region as region,',
'    sum(COST_MY_COST) as COST_USAGE',
'from oci_cost',
'where ',
'    tenant_name=:P5_TENANT_NAME and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YY'
||'YY'') = :P5_PERIOD_RANGE) and',
'    :P5_REPORT_SELECTOR in (''Hourly Cost By Region'',''Daily Cost By Region'',''Weekly Cost By Region'',''Monthly Cost By Region'')    ',
'    group by ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end,',
'    prd_region ',
'order by 1,2'))
,p_series_name_column_name=>'REGION'
,p_items_value_column_name=>'COST_USAGE'
,p_items_label_column_name=>'PERIOD'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'center'
,p_items_label_font_size=>'10'
);
end;
/
begin
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(14186828501270009)
,p_chart_id=>wwv_flow_api.id(14186570488270006)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_type=>'date-short'
,p_numeric_pattern=>'DD-MON-YYYY'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(14186775683270008)
,p_chart_id=>wwv_flow_api.id(14186570488270006)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(15050972044989901)
,p_plug_name=>'Cost By Service - &P5_PERIOD.'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>40
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VALUE_OF_ITEM_IN_CONDITION_IN_COLON_DELIMITED_LIST'
,p_plug_display_when_condition=>'P5_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Hourly Cost By Service:Daily Cost By Service:Weekly Cost By Service:Monthly Cost By Service'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(15051010405989902)
,p_region_id=>wwv_flow_api.id(15050972044989901)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'on'
,p_legend_position=>'end'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(15051132224989903)
,p_chart_id=>wwv_flow_api.id(15051010405989902)
,p_seq=>10
,p_name=>'Usage'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end PERIOD,',
'    nvl(PRD_SERVICE,''-'') PRD_SERVICE,',
'    sum(COST_MY_COST) as COST_USAGE',
'from oci_cost',
'where ',
'    tenant_name=:P5_TENANT_NAME and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YY'
||'YY'') = :P5_PERIOD_RANGE) and',
'    :P5_REPORT_SELECTOR in (''Hourly Cost By Service'',''Daily Cost By Service'',''Weekly Cost By Service'',''Monthly Cost By Service'')    ',
'    group by ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end,',
'    nvl(PRD_SERVICE,''-'') ',
'order by 1,2'))
,p_series_name_column_name=>'PRD_SERVICE'
,p_items_value_column_name=>'COST_USAGE'
,p_items_label_column_name=>'PERIOD'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'center'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(15051343629989905)
,p_chart_id=>wwv_flow_api.id(15051010405989902)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_type=>'date-short'
,p_numeric_pattern=>'DD-MON-YYYY'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(15051263494989904)
,p_chart_id=>wwv_flow_api.id(15051010405989902)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(15051727286989909)
,p_plug_name=>'Cost By Compartment - &P5_PERIOD.'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>60
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VALUE_OF_ITEM_IN_CONDITION_IN_COLON_DELIMITED_LIST'
,p_plug_display_when_condition=>'P5_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Hourly Cost By Compartment:Daily Cost By Compartment:Weekly Cost By Compartment:Monthly Cost By Compartment'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(15051899660989910)
,p_region_id=>wwv_flow_api.id(15051727286989909)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'on'
,p_legend_position=>'end'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(15051945799989911)
,p_chart_id=>wwv_flow_api.id(15051899660989910)
,p_seq=>10
,p_name=>'Usage'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end PERIOD,',
'    nvl(prd_compartment_name,''-'') compartment_name,',
'    sum(COST_MY_COST) as COST_USAGE',
'from oci_cost',
'where ',
'    tenant_name=:P5_TENANT_NAME and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YY'
||'YY'') = :P5_PERIOD_RANGE) and',
'    :P5_REPORT_SELECTOR in (''Hourly Cost By Compartment'',''Daily Cost By Compartment'',''Weekly Cost By Compartment'',''Monthly Cost By Compartment'')    ',
'    group by ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end,',
'    nvl(prd_compartment_name,''-'') ',
'order by 1,2'))
,p_series_name_column_name=>'COMPARTMENT_NAME'
,p_items_value_column_name=>'COST_USAGE'
,p_items_label_column_name=>'PERIOD'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'center'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(15052096900989912)
,p_chart_id=>wwv_flow_api.id(15051899660989910)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(15052126213989913)
,p_chart_id=>wwv_flow_api.id(15051899660989910)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_type=>'date-short'
,p_numeric_pattern=>'DD-MON-YYYY'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(15052505519989917)
,p_plug_name=>'Cost By Top Compartment - &P5_PERIOD.'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>80
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VALUE_OF_ITEM_IN_CONDITION_IN_COLON_DELIMITED_LIST'
,p_plug_display_when_condition=>'P5_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Hourly Cost By Top Compartment:Daily Cost By Top Compartment:Weekly Cost By Top Compartment:Monthly Cost By Top Compartment'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(15052674611989918)
,p_region_id=>wwv_flow_api.id(15052505519989917)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'on'
,p_legend_position=>'end'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(15052776181989919)
,p_chart_id=>wwv_flow_api.id(15052674611989918)
,p_seq=>10
,p_name=>'Usage'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end PERIOD,',
'    nvl(case when prd_compartment_path like ''%/%'' then substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) else prd_compartment_path end,''-'') as top_compartment,',
'    sum(COST_MY_COST) as COST_USAGE',
'from oci_cost',
'where ',
'    tenant_name=:P5_TENANT_NAME and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YY'
||'YY'') = :P5_PERIOD_RANGE) and',
'    :P5_REPORT_SELECTOR in (''Hourly Cost By Top Compartment'',''Daily Cost By Top Compartment'',''Weekly Cost By Top Compartment'',''Monthly Cost By Compartment'')    ',
'    group by ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end,',
'    nvl(case when prd_compartment_path like ''%/%'' then substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) else prd_compartment_path end,''-'')',
'order by 1,2'))
,p_series_name_column_name=>'TOP_COMPARTMENT'
,p_items_value_column_name=>'COST_USAGE'
,p_items_label_column_name=>'PERIOD'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'center'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(15052900863989921)
,p_chart_id=>wwv_flow_api.id(15052674611989918)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_type=>'date-short'
,p_numeric_pattern=>'DD-MON-YYYY'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(15052897038989920)
,p_chart_id=>wwv_flow_api.id(15052674611989918)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_report_region(
 p_id=>wwv_flow_api.id(15053388277989925)
,p_name=>'Daily Product Unit Report - Total'
,p_region_name=>'report'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_template=>wwv_flow_api.id(9765042323688020)
,p_display_sequence=>140
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--altRowsDefault:t-Report--rowHighlight'
,p_display_point=>'BODY'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
' SELECT ',
'	product_name,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''01'' then USG_BILLED_QUANTITY else null end) D01,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''02'' then USG_BILLED_QUANTITY else null end) D02,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''03'' then USG_BILLED_QUANTITY else null end) D03,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''04'' then USG_BILLED_QUANTITY else null end) D04,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''05'' then USG_BILLED_QUANTITY else null end) D05,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''06'' then USG_BILLED_QUANTITY else null end) D06,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''07'' then USG_BILLED_QUANTITY else null end) D07,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''08'' then USG_BILLED_QUANTITY else null end) D08,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''09'' then USG_BILLED_QUANTITY else null end) D09,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''10'' then USG_BILLED_QUANTITY else null end) D10,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''11'' then USG_BILLED_QUANTITY else null end) D11,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''12'' then USG_BILLED_QUANTITY else null end) D12,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''13'' then USG_BILLED_QUANTITY else null end) D13,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''14'' then USG_BILLED_QUANTITY else null end) D14,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''15'' then USG_BILLED_QUANTITY else null end) D15,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''16'' then USG_BILLED_QUANTITY else null end) D16,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''17'' then USG_BILLED_QUANTITY else null end) D17,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''18'' then USG_BILLED_QUANTITY else null end) D18,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''19'' then USG_BILLED_QUANTITY else null end) D19,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''20'' then USG_BILLED_QUANTITY else null end) D20,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''21'' then USG_BILLED_QUANTITY else null end) D21,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''22'' then USG_BILLED_QUANTITY else null end) D22,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''23'' then USG_BILLED_QUANTITY else null end) D23,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''24'' then USG_BILLED_QUANTITY else null end) D24,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''25'' then USG_BILLED_QUANTITY else null end) D25,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''26'' then USG_BILLED_QUANTITY else null end) D26,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''27'' then USG_BILLED_QUANTITY else null end) D27,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''28'' then USG_BILLED_QUANTITY else null end) D28,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''29'' then USG_BILLED_QUANTITY else null end) D29,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''30'' then USG_BILLED_QUANTITY else null end) D30,',
'    sum(case when to_char(USAGE_INTERVAL_START,''DD'') = ''31'' then USG_BILLED_QUANTITY else null end) D31',
'FROM ',
'(',
'	SELECT ',
'		COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'') PRODUCT_NAME,',
'		USAGE_INTERVAL_START,',
'		USG_BILLED_QUANTITY',
'	FROM',
'    	oci_cost ',
'	WHERE ',
'		tenant_name=:P5_TENANT_NAME and',
'		:P5_PERIOD=''Daily'' and ',
'		to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE and',
'		(:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'		(:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'		(:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'		(:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'		(:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'        (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'        (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'		(:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'		(:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') AND',
'        :P5_REPORT_SELECTOR = ''Daily Product Unit Report - Total''',
')',
'GROUP BY PRODUCT_NAME',
'having sum(USG_BILLED_QUANTITY)>0;'))
,p_display_when_condition=>'P5_REPORT_SELECTOR'
,p_display_when_cond2=>'Daily Product Unit Report - Total'
,p_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_ajax_enabled=>'Y'
,p_query_row_template=>wwv_flow_api.id(9790776953688052)
,p_query_num_rows=>9999
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'Y'
,p_csv_output_link_text=>'Download'
,p_prn_output=>'Y'
,p_prn_format=>'PDF'
,p_prn_output_link_text=>'Print'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width_units=>'PERCENTAGE'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15053433541989926)
,p_query_column_id=>1
,p_column_alias=>'PRODUCT_NAME'
,p_column_display_sequence=>1
,p_column_heading=>'Product '
,p_use_as_row_header=>'N'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT_NAME#</span>'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15053563987989927)
,p_query_column_id=>2
,p_column_alias=>'D01'
,p_column_display_sequence=>2
,p_column_heading=>'D01'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15053624349989928)
,p_query_column_id=>3
,p_column_alias=>'D02'
,p_column_display_sequence=>3
,p_column_heading=>'D02'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15053743811989929)
,p_query_column_id=>4
,p_column_alias=>'D03'
,p_column_display_sequence=>4
,p_column_heading=>'D03'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15053869231989930)
,p_query_column_id=>5
,p_column_alias=>'D04'
,p_column_display_sequence=>5
,p_column_heading=>'D04'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15053922930989931)
,p_query_column_id=>6
,p_column_alias=>'D05'
,p_column_display_sequence=>6
,p_column_heading=>'D05'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15054086645989932)
,p_query_column_id=>7
,p_column_alias=>'D06'
,p_column_display_sequence=>7
,p_column_heading=>'D06'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15054183423989933)
,p_query_column_id=>8
,p_column_alias=>'D07'
,p_column_display_sequence=>8
,p_column_heading=>'D07'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15054217436989934)
,p_query_column_id=>9
,p_column_alias=>'D08'
,p_column_display_sequence=>9
,p_column_heading=>'D08'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15054344186989935)
,p_query_column_id=>10
,p_column_alias=>'D09'
,p_column_display_sequence=>10
,p_column_heading=>'D09'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15054464066989936)
,p_query_column_id=>11
,p_column_alias=>'D10'
,p_column_display_sequence=>11
,p_column_heading=>'D10'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15054557070989937)
,p_query_column_id=>12
,p_column_alias=>'D11'
,p_column_display_sequence=>12
,p_column_heading=>'D11'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15054691637989938)
,p_query_column_id=>13
,p_column_alias=>'D12'
,p_column_display_sequence=>13
,p_column_heading=>'D12'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15054790560989939)
,p_query_column_id=>14
,p_column_alias=>'D13'
,p_column_display_sequence=>14
,p_column_heading=>'D13'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15054863300989940)
,p_query_column_id=>15
,p_column_alias=>'D14'
,p_column_display_sequence=>15
,p_column_heading=>'D14'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15054915534989941)
,p_query_column_id=>16
,p_column_alias=>'D15'
,p_column_display_sequence=>16
,p_column_heading=>'D15'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15055014112989942)
,p_query_column_id=>17
,p_column_alias=>'D16'
,p_column_display_sequence=>17
,p_column_heading=>'D16'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15055160230989943)
,p_query_column_id=>18
,p_column_alias=>'D17'
,p_column_display_sequence=>18
,p_column_heading=>'D17'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
end;
/
begin
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15055299314989944)
,p_query_column_id=>19
,p_column_alias=>'D18'
,p_column_display_sequence=>19
,p_column_heading=>'D18'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15055397376989945)
,p_query_column_id=>20
,p_column_alias=>'D19'
,p_column_display_sequence=>20
,p_column_heading=>'D19'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15055425307989946)
,p_query_column_id=>21
,p_column_alias=>'D20'
,p_column_display_sequence=>21
,p_column_heading=>'D20'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15055594708989947)
,p_query_column_id=>22
,p_column_alias=>'D21'
,p_column_display_sequence=>22
,p_column_heading=>'D21'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15055632633989948)
,p_query_column_id=>23
,p_column_alias=>'D22'
,p_column_display_sequence=>23
,p_column_heading=>'D22'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15055763819989949)
,p_query_column_id=>24
,p_column_alias=>'D23'
,p_column_display_sequence=>24
,p_column_heading=>'D23'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15055862777989950)
,p_query_column_id=>25
,p_column_alias=>'D24'
,p_column_display_sequence=>25
,p_column_heading=>'D24'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15082638529497501)
,p_query_column_id=>26
,p_column_alias=>'D25'
,p_column_display_sequence=>26
,p_column_heading=>'D25'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15082758458497502)
,p_query_column_id=>27
,p_column_alias=>'D26'
,p_column_display_sequence=>27
,p_column_heading=>'D26'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15082822849497503)
,p_query_column_id=>28
,p_column_alias=>'D27'
,p_column_display_sequence=>28
,p_column_heading=>'D27'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15082940860497504)
,p_query_column_id=>29
,p_column_alias=>'D28'
,p_column_display_sequence=>29
,p_column_heading=>'D28'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15083079467497505)
,p_query_column_id=>30
,p_column_alias=>'D29'
,p_column_display_sequence=>30
,p_column_heading=>'D29'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15083179032497506)
,p_query_column_id=>31
,p_column_alias=>'D30'
,p_column_display_sequence=>31
,p_column_heading=>'D30'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15083290532497507)
,p_query_column_id=>32
,p_column_alias=>'D31'
,p_column_display_sequence=>32
,p_column_heading=>'D31'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_region(
 p_id=>wwv_flow_api.id(15083635722497511)
,p_name=>'Weekly Product Unit Report'
,p_region_name=>'report'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_template=>wwv_flow_api.id(9765042323688020)
,p_display_sequence=>170
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--altRowsDefault:t-Report--rowHighlight'
,p_display_point=>'BODY'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
' SELECT ',
'	COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'') as product_name,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''01'' then USG_BILLED_QUANTITY else null end) W01,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''02'' then USG_BILLED_QUANTITY else null end) W02,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''03'' then USG_BILLED_QUANTITY else null end) W03,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''04'' then USG_BILLED_QUANTITY else null end) W04,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''05'' then USG_BILLED_QUANTITY else null end) W05,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''06'' then USG_BILLED_QUANTITY else null end) W06,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''07'' then USG_BILLED_QUANTITY else null end) W07,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''08'' then USG_BILLED_QUANTITY else null end) W08,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''09'' then USG_BILLED_QUANTITY else null end) W09,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''10'' then USG_BILLED_QUANTITY else null end) W10,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''11'' then USG_BILLED_QUANTITY else null end) W11,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''12'' then USG_BILLED_QUANTITY else null end) W12,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''13'' then USG_BILLED_QUANTITY else null end) W13,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''14'' then USG_BILLED_QUANTITY else null end) W14,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''15'' then USG_BILLED_QUANTITY else null end) W15,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''16'' then USG_BILLED_QUANTITY else null end) W16,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''17'' then USG_BILLED_QUANTITY else null end) W17,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''18'' then USG_BILLED_QUANTITY else null end) W18,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''19'' then USG_BILLED_QUANTITY else null end) W19,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''20'' then USG_BILLED_QUANTITY else null end) W20,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''21'' then USG_BILLED_QUANTITY else null end) W21,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''22'' then USG_BILLED_QUANTITY else null end) W22,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''23'' then USG_BILLED_QUANTITY else null end) W23,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''24'' then USG_BILLED_QUANTITY else null end) W24,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''25'' then USG_BILLED_QUANTITY else null end) W25,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''26'' then USG_BILLED_QUANTITY else null end) W26,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''27'' then USG_BILLED_QUANTITY else null end) W27,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''28'' then USG_BILLED_QUANTITY else null end) W28,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''29'' then USG_BILLED_QUANTITY else null end) W29,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''30'' then USG_BILLED_QUANTITY else null end) W30,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''31'' then USG_BILLED_QUANTITY else null end) W31,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''32'' then USG_BILLED_QUANTITY else null end) W32,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''33'' then USG_BILLED_QUANTITY else null end) W33,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''34'' then USG_BILLED_QUANTITY else null end) W34,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''35'' then USG_BILLED_QUANTITY else null end) W35,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''36'' then USG_BILLED_QUANTITY else null end) W36,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''37'' then USG_BILLED_QUANTITY else null end) W37,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''38'' then USG_BILLED_QUANTITY else null end) W38,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''39'' then USG_BILLED_QUANTITY else null end) W39,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''40'' then USG_BILLED_QUANTITY else null end) W40,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''41'' then USG_BILLED_QUANTITY else null end) W41,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''42'' then USG_BILLED_QUANTITY else null end) W42,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''43'' then USG_BILLED_QUANTITY else null end) W43,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''44'' then USG_BILLED_QUANTITY else null end) W44,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''45'' then USG_BILLED_QUANTITY else null end) W45,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''46'' then USG_BILLED_QUANTITY else null end) W46,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''47'' then USG_BILLED_QUANTITY else null end) W47,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''48'' then USG_BILLED_QUANTITY else null end) W48,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''49'' then USG_BILLED_QUANTITY else null end) W49,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''50'' then USG_BILLED_QUANTITY else null end) W50,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''51'' then USG_BILLED_QUANTITY else null end) W51,',
'    sum(case when to_char(USAGE_INTERVAL_START,''WW'') = ''52'' then USG_BILLED_QUANTITY else null end) W52',
'from',
'    oci_cost ',
'WHERE ',
'    tenant_name=:P5_TENANT_NAME and',
'    :P5_PERIOD=''Weekly'' and ',
'	to_char(USAGE_INTERVAL_START,''YYYY'') = :P5_PERIOD_RANGE and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    :P5_REPORT_SELECTOR = ''Weekly Product Unit Report''',
'GROUP BY ',
'    COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'')',
'having sum(USG_BILLED_QUANTITY)>0;'))
,p_display_when_condition=>'P5_REPORT_SELECTOR'
,p_display_when_cond2=>'Weekly Product Unit Report'
,p_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_ajax_enabled=>'Y'
,p_query_row_template=>wwv_flow_api.id(9790776953688052)
,p_query_num_rows=>9999
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'Y'
,p_csv_output_link_text=>'Download'
,p_prn_output=>'Y'
,p_prn_format=>'PDF'
,p_prn_output_link_text=>'Print'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width_units=>'PERCENTAGE'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15083882458497513)
,p_query_column_id=>1
,p_column_alias=>'PRODUCT_NAME'
,p_column_display_sequence=>1
,p_column_heading=>'Product'
,p_use_as_row_header=>'N'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT_NAME#</span>'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15084020372497515)
,p_query_column_id=>2
,p_column_alias=>'W01'
,p_column_display_sequence=>2
,p_column_heading=>'W01'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15084196664497516)
,p_query_column_id=>3
,p_column_alias=>'W02'
,p_column_display_sequence=>3
,p_column_heading=>'W02'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15084234533497517)
,p_query_column_id=>4
,p_column_alias=>'W03'
,p_column_display_sequence=>4
,p_column_heading=>'W03'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15084309261497518)
,p_query_column_id=>5
,p_column_alias=>'W04'
,p_column_display_sequence=>5
,p_column_heading=>'W04'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15084429391497519)
,p_query_column_id=>6
,p_column_alias=>'W05'
,p_column_display_sequence=>6
,p_column_heading=>'W05'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15084526180497520)
,p_query_column_id=>7
,p_column_alias=>'W06'
,p_column_display_sequence=>7
,p_column_heading=>'W06'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15084637150497521)
,p_query_column_id=>8
,p_column_alias=>'W07'
,p_column_display_sequence=>8
,p_column_heading=>'W07'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15084797622497522)
,p_query_column_id=>9
,p_column_alias=>'W08'
,p_column_display_sequence=>9
,p_column_heading=>'W08'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15084836140497523)
,p_query_column_id=>10
,p_column_alias=>'W09'
,p_column_display_sequence=>10
,p_column_heading=>'W09'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15084995246497524)
,p_query_column_id=>11
,p_column_alias=>'W10'
,p_column_display_sequence=>11
,p_column_heading=>'W10'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15085033317497525)
,p_query_column_id=>12
,p_column_alias=>'W11'
,p_column_display_sequence=>12
,p_column_heading=>'W11'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15085177774497526)
,p_query_column_id=>13
,p_column_alias=>'W12'
,p_column_display_sequence=>13
,p_column_heading=>'W12'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15085250160497527)
,p_query_column_id=>14
,p_column_alias=>'W13'
,p_column_display_sequence=>14
,p_column_heading=>'W13'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15085385329497528)
,p_query_column_id=>15
,p_column_alias=>'W14'
,p_column_display_sequence=>15
,p_column_heading=>'W14'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15085480365497529)
,p_query_column_id=>16
,p_column_alias=>'W15'
,p_column_display_sequence=>16
,p_column_heading=>'W15'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15085576532497530)
,p_query_column_id=>17
,p_column_alias=>'W16'
,p_column_display_sequence=>17
,p_column_heading=>'W16'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15085669628497531)
,p_query_column_id=>18
,p_column_alias=>'W17'
,p_column_display_sequence=>18
,p_column_heading=>'W17'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15085797503497532)
,p_query_column_id=>19
,p_column_alias=>'W18'
,p_column_display_sequence=>19
,p_column_heading=>'W18'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15085831898497533)
,p_query_column_id=>20
,p_column_alias=>'W19'
,p_column_display_sequence=>20
,p_column_heading=>'W19'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15085995417497534)
,p_query_column_id=>21
,p_column_alias=>'W20'
,p_column_display_sequence=>21
,p_column_heading=>'W20'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15086033795497535)
,p_query_column_id=>22
,p_column_alias=>'W21'
,p_column_display_sequence=>22
,p_column_heading=>'W21'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15086169388497536)
,p_query_column_id=>23
,p_column_alias=>'W22'
,p_column_display_sequence=>23
,p_column_heading=>'W22'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15086256237497537)
,p_query_column_id=>24
,p_column_alias=>'W23'
,p_column_display_sequence=>24
,p_column_heading=>'W23'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15086305029497538)
,p_query_column_id=>25
,p_column_alias=>'W24'
,p_column_display_sequence=>25
,p_column_heading=>'W24'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15086424118497539)
,p_query_column_id=>26
,p_column_alias=>'W25'
,p_column_display_sequence=>26
,p_column_heading=>'W25'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15086575044497540)
,p_query_column_id=>27
,p_column_alias=>'W26'
,p_column_display_sequence=>27
,p_column_heading=>'W26'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15086644472497541)
,p_query_column_id=>28
,p_column_alias=>'W27'
,p_column_display_sequence=>28
,p_column_heading=>'W27'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15086736459497542)
,p_query_column_id=>29
,p_column_alias=>'W28'
,p_column_display_sequence=>29
,p_column_heading=>'W28'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15086866979497543)
,p_query_column_id=>30
,p_column_alias=>'W29'
,p_column_display_sequence=>30
,p_column_heading=>'W29'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15083737349497512)
,p_query_column_id=>31
,p_column_alias=>'W30'
,p_column_display_sequence=>31
,p_column_heading=>'W30'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15086972484497544)
,p_query_column_id=>32
,p_column_alias=>'W31'
,p_column_display_sequence=>32
,p_column_heading=>'W31'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15087043653497545)
,p_query_column_id=>33
,p_column_alias=>'W32'
,p_column_display_sequence=>33
,p_column_heading=>'W32'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15087140332497546)
,p_query_column_id=>34
,p_column_alias=>'W33'
,p_column_display_sequence=>34
,p_column_heading=>'W33'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15087212537497547)
,p_query_column_id=>35
,p_column_alias=>'W34'
,p_column_display_sequence=>35
,p_column_heading=>'W34'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15087301471497548)
,p_query_column_id=>36
,p_column_alias=>'W35'
,p_column_display_sequence=>36
,p_column_heading=>'W35'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15087435183497549)
,p_query_column_id=>37
,p_column_alias=>'W36'
,p_column_display_sequence=>37
,p_column_heading=>'W36'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15087578148497550)
,p_query_column_id=>38
,p_column_alias=>'W37'
,p_column_display_sequence=>38
,p_column_heading=>'W37'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15101314487532001)
,p_query_column_id=>39
,p_column_alias=>'W38'
,p_column_display_sequence=>39
,p_column_heading=>'W38'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15101467741532002)
,p_query_column_id=>40
,p_column_alias=>'W39'
,p_column_display_sequence=>40
,p_column_heading=>'W39'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15101501587532003)
,p_query_column_id=>41
,p_column_alias=>'W40'
,p_column_display_sequence=>41
,p_column_heading=>'W40'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15101628599532004)
,p_query_column_id=>42
,p_column_alias=>'W41'
,p_column_display_sequence=>42
,p_column_heading=>'W41'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15101775120532005)
,p_query_column_id=>43
,p_column_alias=>'W42'
,p_column_display_sequence=>43
,p_column_heading=>'W42'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15101834422532006)
,p_query_column_id=>44
,p_column_alias=>'W43'
,p_column_display_sequence=>44
,p_column_heading=>'W43'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
end;
/
begin
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15101918299532007)
,p_query_column_id=>45
,p_column_alias=>'W44'
,p_column_display_sequence=>45
,p_column_heading=>'W44'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15102016850532008)
,p_query_column_id=>46
,p_column_alias=>'W45'
,p_column_display_sequence=>46
,p_column_heading=>'W45'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15102102479532009)
,p_query_column_id=>47
,p_column_alias=>'W46'
,p_column_display_sequence=>47
,p_column_heading=>'W46'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15102201934532010)
,p_query_column_id=>48
,p_column_alias=>'W47'
,p_column_display_sequence=>48
,p_column_heading=>'W47'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15102376964532011)
,p_query_column_id=>49
,p_column_alias=>'W48'
,p_column_display_sequence=>49
,p_column_heading=>'W48'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15102424245532012)
,p_query_column_id=>50
,p_column_alias=>'W49'
,p_column_display_sequence=>50
,p_column_heading=>'W49'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15102519216532013)
,p_query_column_id=>51
,p_column_alias=>'W50'
,p_column_display_sequence=>51
,p_column_heading=>'W50'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15102602847532014)
,p_query_column_id=>52
,p_column_alias=>'W51'
,p_column_display_sequence=>52
,p_column_heading=>'W51'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15102752424532015)
,p_query_column_id=>53
,p_column_alias=>'W52'
,p_column_display_sequence=>53
,p_column_heading=>'W52'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_region(
 p_id=>wwv_flow_api.id(15102859636532016)
,p_name=>'Monthly Product Unit Report'
,p_region_name=>'report'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_template=>wwv_flow_api.id(9765042323688020)
,p_display_sequence=>100
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--altRowsDefault:t-Report--rowHighlight'
,p_display_point=>'BODY'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'SELECT ',
'	COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'') as product_name,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''01'' then USG_BILLED_QUANTITY else null end) Jan,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''02'' then USG_BILLED_QUANTITY else null end) Feb,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''03'' then USG_BILLED_QUANTITY else null end) Mar,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''04'' then USG_BILLED_QUANTITY else null end) Apr,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''05'' then USG_BILLED_QUANTITY else null end) May,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''06'' then USG_BILLED_QUANTITY else null end) Jun,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''07'' then USG_BILLED_QUANTITY else null end) Jul,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''08'' then USG_BILLED_QUANTITY else null end) Aug,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''09'' then USG_BILLED_QUANTITY else null end) Sep,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''10'' then USG_BILLED_QUANTITY else null end) Oct,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''11'' then USG_BILLED_QUANTITY else null end) Nov,',
'    sum(case when to_char(USAGE_INTERVAL_START,''MM'') = ''12'' then USG_BILLED_QUANTITY else null end) Dec',
'FROM ',
'    oci_cost ',
'WHERE ',
'    tenant_name=:P5_TENANT_NAME and',
'    :P5_PERIOD=''Monthly'' and ',
'	to_char(USAGE_INTERVAL_START,''YYYY'') = :P5_PERIOD_RANGE and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    :P5_REPORT_SELECTOR = ''Monthly Product Unit Report''',
'GROUP BY ',
'	COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'')',
'having sum(USG_BILLED_QUANTITY)>0;',
''))
,p_display_when_condition=>'P5_REPORT_SELECTOR'
,p_display_when_cond2=>'Monthly Product Unit Report'
,p_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_ajax_enabled=>'Y'
,p_query_row_template=>wwv_flow_api.id(9790776953688052)
,p_query_num_rows=>9999
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'Y'
,p_csv_output_link_text=>'Download'
,p_prn_output=>'Y'
,p_prn_format=>'PDF'
,p_prn_output_link_text=>'Print'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width_units=>'PERCENTAGE'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15102928440532017)
,p_query_column_id=>1
,p_column_alias=>'PRODUCT_NAME'
,p_column_display_sequence=>1
,p_column_heading=>'&P5_REPORT_GROUP.'
,p_use_as_row_header=>'N'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT_NAME#</span>'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15103149558532019)
,p_query_column_id=>2
,p_column_alias=>'JAN'
,p_column_display_sequence=>2
,p_column_heading=>'Jan &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15103207901532020)
,p_query_column_id=>3
,p_column_alias=>'FEB'
,p_column_display_sequence=>3
,p_column_heading=>'Feb &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15103381359532021)
,p_query_column_id=>4
,p_column_alias=>'MAR'
,p_column_display_sequence=>4
,p_column_heading=>'Mar &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15103471107532022)
,p_query_column_id=>5
,p_column_alias=>'APR'
,p_column_display_sequence=>5
,p_column_heading=>'Apr &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15103544868532023)
,p_query_column_id=>6
,p_column_alias=>'MAY'
,p_column_display_sequence=>6
,p_column_heading=>'May &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15103658490532024)
,p_query_column_id=>7
,p_column_alias=>'JUN'
,p_column_display_sequence=>7
,p_column_heading=>'Jun &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15103749937532025)
,p_query_column_id=>8
,p_column_alias=>'JUL'
,p_column_display_sequence=>8
,p_column_heading=>'Jul &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15103839728532026)
,p_query_column_id=>9
,p_column_alias=>'AUG'
,p_column_display_sequence=>9
,p_column_heading=>'Aug &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15103933986532027)
,p_query_column_id=>10
,p_column_alias=>'SEP'
,p_column_display_sequence=>10
,p_column_heading=>'Sep &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15104061393532028)
,p_query_column_id=>11
,p_column_alias=>'OCT'
,p_column_display_sequence=>11
,p_column_heading=>'Oct &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15104135848532029)
,p_query_column_id=>12
,p_column_alias=>'NOV'
,p_column_display_sequence=>12
,p_column_heading=>'Nov &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(15104268225532030)
,p_query_column_id=>13
,p_column_alias=>'DEC'
,p_column_display_sequence=>13
,p_column_heading=>'Dec &P5_PERIOD_RANGE.'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_report_column_width=>90
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(16359989459490324)
,p_plug_name=>'Cost By SKU - &P5_PERIOD.'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>50
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VALUE_OF_ITEM_IN_CONDITION_IN_COLON_DELIMITED_LIST'
,p_plug_display_when_condition=>'P5_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Hourly Cost By SKU:Daily Cost By SKU:Weekly Cost By SKU:Monthly Cost By SKU'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(16360042364490325)
,p_region_id=>wwv_flow_api.id(16359989459490324)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'on'
,p_connect_nulls=>'Y'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'on'
,p_legend_position=>'end'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(16360174750490326)
,p_chart_id=>wwv_flow_api.id(16360042364490325)
,p_seq=>10
,p_name=>'Usage'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end PERIOD,',
'    COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'') COST_PRODUCT_SKU,',
'    sum(COST_MY_COST) as COST_USAGE',
'from oci_cost',
'where ',
'    tenant_name=:P5_TENANT_NAME and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YY'
||'YY'') = :P5_PERIOD_RANGE) and',
'    :P5_REPORT_SELECTOR in (''Hourly Cost By SKU'',''Daily Cost By SKU'',''Weekly Cost By SKU'',''Monthly Cost By SKU'')    ',
'    group by ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end,',
'    COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'')',
'order by 1,2'))
,p_series_name_column_name=>'COST_PRODUCT_SKU'
,p_items_value_column_name=>'COST_USAGE'
,p_items_label_column_name=>'PERIOD'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'center'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(16360289843490327)
,p_chart_id=>wwv_flow_api.id(16360042364490325)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(16360351214490328)
,p_chart_id=>wwv_flow_api.id(16360042364490325)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_type=>'date-short'
,p_numeric_pattern=>'DD-MON-YYYY'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
);
wwv_flow_api.create_report_region(
 p_id=>wwv_flow_api.id(16361917406490344)
,p_name=>'Hourly Cost Report'
,p_region_name=>'report'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_template=>wwv_flow_api.id(9765042323688020)
,p_display_sequence=>120
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--altRowsDefault:t-Report--rowHighlight'
,p_display_point=>'BODY'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'SELECT ',
'	case ',
'		when :P5_REPORT_GROUP = ''Product'' or :P5_REPORT_GROUP is null then COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'')',
'		when :P5_REPORT_GROUP = ''Region'' then prd_region',
'		when :P5_REPORT_GROUP = ''Tag Special'' then tag_special',
'		when :P5_REPORT_GROUP = ''Top Compartment'' then ',
'			case ',
'                when prd_compartment_path is null then ''No Compartment''',
'                when prd_compartment_path like ''%/%'' then nvl(substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) ,''(Root)'')',
'                else prd_compartment_path ',
'            end ',
'		when :P5_REPORT_GROUP = ''Compartment'' then nvl(prd_compartment_name,''No Compartment'')',
'        when :P5_REPORT_GROUP = ''Tenant'' then nvl(tenant_id,''No TenantId'')',
'	end product_name,',
'    sum(COST_MY_COST) TOTAL,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''00'' then COST_MY_COST else null end) H00,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''01'' then COST_MY_COST else null end) H01,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''02'' then COST_MY_COST else null end) H02,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''03'' then COST_MY_COST else null end) H03,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''04'' then COST_MY_COST else null end) H04,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''05'' then COST_MY_COST else null end) H05,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''06'' then COST_MY_COST else null end) H06,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''07'' then COST_MY_COST else null end) H07,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''08'' then COST_MY_COST else null end) H08,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''09'' then COST_MY_COST else null end) H09,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''10'' then COST_MY_COST else null end) H10,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''11'' then COST_MY_COST else null end) H11,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''12'' then COST_MY_COST else null end) H12,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''13'' then COST_MY_COST else null end) H13,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''14'' then COST_MY_COST else null end) H14,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''15'' then COST_MY_COST else null end) H15,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''16'' then COST_MY_COST else null end) H16,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''17'' then COST_MY_COST else null end) H17,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''18'' then COST_MY_COST else null end) H18,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''19'' then COST_MY_COST else null end) H19,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''20'' then COST_MY_COST else null end) H20,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''21'' then COST_MY_COST else null end) H21,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''22'' then COST_MY_COST else null end) H22,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''23'' then COST_MY_COST else null end) H23',
'FROM ',
'    oci_cost ',
'WHERE ',
'    tenant_name=:P5_TENANT_NAME and',
'    :P5_PERIOD=''Hourly'' and ',
'	to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    :P5_REPORT_SELECTOR = ''Hourly Cost Report''',
'GROUP BY ',
'	case ',
'		when :P5_REPORT_GROUP = ''Product'' or :P5_REPORT_GROUP is null then COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'')',
'		when :P5_REPORT_GROUP = ''Region'' then prd_region',
'		when :P5_REPORT_GROUP = ''Tag Special'' then tag_special',
'		when :P5_REPORT_GROUP = ''Top Compartment'' then ',
'			case ',
'                when prd_compartment_path is null then ''No Compartment''',
'                when prd_compartment_path like ''%/%'' then nvl(substr(prd_compartment_path,1,instr(prd_compartment_path,'' /'')-1) ,''(Root)'')',
'                else prd_compartment_path ',
'            end ',
'		when :P5_REPORT_GROUP = ''Compartment'' then nvl(prd_compartment_name,''No Compartment'')',
'        when :P5_REPORT_GROUP = ''Tenant'' then nvl(tenant_id,''No TenantId'')',
'	end',
'having sum(COST_MY_COST)>0;'))
,p_display_when_condition=>'P5_REPORT_SELECTOR'
,p_display_when_cond2=>'Hourly Cost Report'
,p_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_ajax_enabled=>'Y'
,p_query_row_template=>wwv_flow_api.id(9790776953688052)
,p_query_num_rows=>9999
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'Y'
,p_csv_output_link_text=>'Download'
,p_prn_output=>'Y'
,p_prn_format=>'PDF'
,p_prn_output_link_text=>'Print'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width_units=>'PERCENTAGE'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16763274047834718)
,p_query_column_id=>1
,p_column_alias=>'PRODUCT_NAME'
,p_column_display_sequence=>1
,p_column_heading=>'&P5_REPORT_GROUP.'
,p_use_as_row_header=>'N'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT_NAME#</span>'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16763364024834719)
,p_query_column_id=>2
,p_column_alias=>'TOTAL'
,p_column_display_sequence=>2
,p_column_heading=>'Total'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_sum_column=>'Y'
,p_report_column_width=>85
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16770511516841241)
,p_query_column_id=>3
,p_column_alias=>'H00'
,p_column_display_sequence=>3
,p_column_heading=>'H00'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16770689428841242)
,p_query_column_id=>4
,p_column_alias=>'H01'
,p_column_display_sequence=>4
,p_column_heading=>'H01'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16770737453841243)
,p_query_column_id=>5
,p_column_alias=>'H02'
,p_column_display_sequence=>5
,p_column_heading=>'H02'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16770854563841244)
,p_query_column_id=>6
,p_column_alias=>'H03'
,p_column_display_sequence=>6
,p_column_heading=>'H03'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16770997460841245)
,p_query_column_id=>7
,p_column_alias=>'H04'
,p_column_display_sequence=>7
,p_column_heading=>'H04'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16771031468841246)
,p_query_column_id=>8
,p_column_alias=>'H05'
,p_column_display_sequence=>8
,p_column_heading=>'H05'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16771118519841247)
,p_query_column_id=>9
,p_column_alias=>'H06'
,p_column_display_sequence=>9
,p_column_heading=>'H06'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16771262419841248)
,p_query_column_id=>10
,p_column_alias=>'H07'
,p_column_display_sequence=>10
,p_column_heading=>'H07'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16771329063841249)
,p_query_column_id=>11
,p_column_alias=>'H08'
,p_column_display_sequence=>11
,p_column_heading=>'H08'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16771441103841250)
,p_query_column_id=>12
,p_column_alias=>'H09'
,p_column_display_sequence=>12
,p_column_heading=>'H09'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16826879267029001)
,p_query_column_id=>13
,p_column_alias=>'H10'
,p_column_display_sequence=>13
,p_column_heading=>'H10'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16826933010029002)
,p_query_column_id=>14
,p_column_alias=>'H11'
,p_column_display_sequence=>14
,p_column_heading=>'H11'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16827089785029003)
,p_query_column_id=>15
,p_column_alias=>'H12'
,p_column_display_sequence=>15
,p_column_heading=>'H12'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16827116573029004)
,p_query_column_id=>16
,p_column_alias=>'H13'
,p_column_display_sequence=>16
,p_column_heading=>'H13'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
end;
/
begin
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16827224833029005)
,p_query_column_id=>17
,p_column_alias=>'H14'
,p_column_display_sequence=>17
,p_column_heading=>'H14'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16827303340029006)
,p_query_column_id=>18
,p_column_alias=>'H15'
,p_column_display_sequence=>18
,p_column_heading=>'H15'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16827496080029007)
,p_query_column_id=>19
,p_column_alias=>'H16'
,p_column_display_sequence=>19
,p_column_heading=>'H16'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16827516268029008)
,p_query_column_id=>20
,p_column_alias=>'H17'
,p_column_display_sequence=>20
,p_column_heading=>'H17'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16827614635029009)
,p_query_column_id=>21
,p_column_alias=>'H18'
,p_column_display_sequence=>21
,p_column_heading=>'H18'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16827749905029010)
,p_query_column_id=>22
,p_column_alias=>'H19'
,p_column_display_sequence=>22
,p_column_heading=>'H19'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16827896907029011)
,p_query_column_id=>23
,p_column_alias=>'H20'
,p_column_display_sequence=>23
,p_column_heading=>'H20'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16827934142029012)
,p_query_column_id=>24
,p_column_alias=>'H21'
,p_column_display_sequence=>24
,p_column_heading=>'H21'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16828081124029013)
,p_query_column_id=>25
,p_column_alias=>'H22'
,p_column_display_sequence=>25
,p_column_heading=>'H22'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16828165381029014)
,p_query_column_id=>26
,p_column_alias=>'H23'
,p_column_display_sequence=>26
,p_column_heading=>'H23'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_region(
 p_id=>wwv_flow_api.id(16766903294841205)
,p_name=>'Hourly Product Unit Report'
,p_region_name=>'report'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_template=>wwv_flow_api.id(9765042323688020)
,p_display_sequence=>150
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--altRowsDefault:t-Report--rowHighlight'
,p_display_point=>'BODY'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
' SELECT ',
'	product_name,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''00'' then USG_BILLED_QUANTITY else null end) D00,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''01'' then USG_BILLED_QUANTITY else null end) D01,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''02'' then USG_BILLED_QUANTITY else null end) D02,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''03'' then USG_BILLED_QUANTITY else null end) D03,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''04'' then USG_BILLED_QUANTITY else null end) D04,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''05'' then USG_BILLED_QUANTITY else null end) D05,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''06'' then USG_BILLED_QUANTITY else null end) D06,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''07'' then USG_BILLED_QUANTITY else null end) D07,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''08'' then USG_BILLED_QUANTITY else null end) D08,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''09'' then USG_BILLED_QUANTITY else null end) D09,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''10'' then USG_BILLED_QUANTITY else null end) D10,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''11'' then USG_BILLED_QUANTITY else null end) D11,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''12'' then USG_BILLED_QUANTITY else null end) D12,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''13'' then USG_BILLED_QUANTITY else null end) D13,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''14'' then USG_BILLED_QUANTITY else null end) D14,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''15'' then USG_BILLED_QUANTITY else null end) D15,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''16'' then USG_BILLED_QUANTITY else null end) D16,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''17'' then USG_BILLED_QUANTITY else null end) D17,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''18'' then USG_BILLED_QUANTITY else null end) D18,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''19'' then USG_BILLED_QUANTITY else null end) D19,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''20'' then USG_BILLED_QUANTITY else null end) D20,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''21'' then USG_BILLED_QUANTITY else null end) D21,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''22'' then USG_BILLED_QUANTITY else null end) D22,',
'    sum(case when to_char(USAGE_INTERVAL_START,''HH24'') = ''23'' then USG_BILLED_QUANTITY else null end) D23',
'FROM ',
'(',
'	SELECT ',
'		COST_PRODUCT_SKU || '' '' || replace(replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '',''''),''Oracle Cloud Infrastructure'',''OCI'') PRODUCT_NAME,',
'		USAGE_INTERVAL_START,',
'		USG_BILLED_QUANTITY',
'	FROM',
'    	oci_cost ',
'	WHERE ',
'		tenant_name=:P5_TENANT_NAME and',
'		:P5_PERIOD=''Hourly'' and ',
'		to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE and',
'		(:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'		(:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'		(:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'		(:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'		(:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'        (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'        (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'		(:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'		(:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') AND',
'        :P5_REPORT_SELECTOR = ''Hourly Product Unit Report''',
')',
'GROUP BY PRODUCT_NAME',
'having sum(USG_BILLED_QUANTITY)>0;'))
,p_display_when_condition=>'P5_REPORT_SELECTOR'
,p_display_when_cond2=>'Hourly Product Unit Report'
,p_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_ajax_enabled=>'Y'
,p_query_row_template=>wwv_flow_api.id(9790776953688052)
,p_query_num_rows=>9999
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'Y'
,p_csv_output_link_text=>'Download'
,p_prn_output=>'Y'
,p_prn_format=>'PDF'
,p_prn_output_link_text=>'Print'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width_units=>'PERCENTAGE'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16767038146841206)
,p_query_column_id=>1
,p_column_alias=>'PRODUCT_NAME'
,p_column_display_sequence=>1
,p_column_heading=>'Product'
,p_use_as_row_header=>'N'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT_NAME#</span>'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16828243172029015)
,p_query_column_id=>2
,p_column_alias=>'D00'
,p_column_display_sequence=>2
,p_column_heading=>'D00'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16828372110029016)
,p_query_column_id=>3
,p_column_alias=>'D01'
,p_column_display_sequence=>3
,p_column_heading=>'D01'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16828437615029017)
,p_query_column_id=>4
,p_column_alias=>'D02'
,p_column_display_sequence=>4
,p_column_heading=>'D02'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16828549991029018)
,p_query_column_id=>5
,p_column_alias=>'D03'
,p_column_display_sequence=>5
,p_column_heading=>'D03'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16828631498029019)
,p_query_column_id=>6
,p_column_alias=>'D04'
,p_column_display_sequence=>6
,p_column_heading=>'D04'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16828793554029020)
,p_query_column_id=>7
,p_column_alias=>'D05'
,p_column_display_sequence=>7
,p_column_heading=>'D05'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16828813690029021)
,p_query_column_id=>8
,p_column_alias=>'D06'
,p_column_display_sequence=>8
,p_column_heading=>'D06'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16828917414029022)
,p_query_column_id=>9
,p_column_alias=>'D07'
,p_column_display_sequence=>9
,p_column_heading=>'D07'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16829061684029023)
,p_query_column_id=>10
,p_column_alias=>'D08'
,p_column_display_sequence=>10
,p_column_heading=>'D08'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16829112352029024)
,p_query_column_id=>11
,p_column_alias=>'D09'
,p_column_display_sequence=>11
,p_column_heading=>'D09'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16829239676029025)
,p_query_column_id=>12
,p_column_alias=>'D10'
,p_column_display_sequence=>12
,p_column_heading=>'D10'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16829374140029026)
,p_query_column_id=>13
,p_column_alias=>'D11'
,p_column_display_sequence=>13
,p_column_heading=>'D11'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16829409576029027)
,p_query_column_id=>14
,p_column_alias=>'D12'
,p_column_display_sequence=>14
,p_column_heading=>'D12'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16829515328029028)
,p_query_column_id=>15
,p_column_alias=>'D13'
,p_column_display_sequence=>15
,p_column_heading=>'D13'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16829664941029029)
,p_query_column_id=>16
,p_column_alias=>'D14'
,p_column_display_sequence=>16
,p_column_heading=>'D14'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16829724269029030)
,p_query_column_id=>17
,p_column_alias=>'D15'
,p_column_display_sequence=>17
,p_column_heading=>'D15'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16829802026029031)
,p_query_column_id=>18
,p_column_alias=>'D16'
,p_column_display_sequence=>18
,p_column_heading=>'D16'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16829959305029032)
,p_query_column_id=>19
,p_column_alias=>'D17'
,p_column_display_sequence=>19
,p_column_heading=>'D17'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16830085321029033)
,p_query_column_id=>20
,p_column_alias=>'D18'
,p_column_display_sequence=>20
,p_column_heading=>'D18'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16830195992029034)
,p_query_column_id=>21
,p_column_alias=>'D19'
,p_column_display_sequence=>21
,p_column_heading=>'D19'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16830202018029035)
,p_query_column_id=>22
,p_column_alias=>'D20'
,p_column_display_sequence=>22
,p_column_heading=>'D20'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16830368840029036)
,p_query_column_id=>23
,p_column_alias=>'D21'
,p_column_display_sequence=>23
,p_column_heading=>'D21'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16830480806029037)
,p_query_column_id=>24
,p_column_alias=>'D22'
,p_column_display_sequence=>24
,p_column_heading=>'D22'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_report_columns(
 p_id=>wwv_flow_api.id(16830548503029038)
,p_query_column_id=>25
,p_column_alias=>'D23'
,p_column_display_sequence=>25
,p_column_heading=>'D23'
,p_use_as_row_header=>'N'
,p_column_format=>'999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(23961814581267567)
,p_plug_name=>'Cost Over Time - &P5_PERIOD.'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>20
,p_plug_display_point=>'BODY'
,p_plug_source_type=>'NATIVE_JET_CHART'
,p_plug_query_num_rows=>15
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VALUE_OF_ITEM_IN_CONDITION_IN_COLON_DELIMITED_LIST'
,p_plug_display_when_condition=>'P5_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Hourly Cost Over Time:Daily Cost Over Time:Weekly Cost Over Time:Monthly Cost Over Time'
);
wwv_flow_api.create_jet_chart(
 p_id=>wwv_flow_api.id(12036462660075984)
,p_region_id=>wwv_flow_api.id(23961814581267567)
,p_chart_type=>'bar'
,p_height=>'500'
,p_animation_on_display=>'auto'
,p_animation_on_data_change=>'auto'
,p_orientation=>'vertical'
,p_data_cursor=>'auto'
,p_data_cursor_behavior=>'auto'
,p_hide_and_show_behavior=>'none'
,p_hover_behavior=>'none'
,p_stack=>'on'
,p_stack_label=>'off'
,p_connect_nulls=>'Y'
,p_sorting=>'label-asc'
,p_fill_multi_series_gaps=>true
,p_zoom_and_scroll=>'off'
,p_tooltip_rendered=>'Y'
,p_show_series_name=>true
,p_show_group_name=>true
,p_show_value=>true
,p_legend_rendered=>'on'
,p_legend_position=>'bottom'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(12038129542075985)
,p_chart_id=>wwv_flow_api.id(12036462660075984)
,p_seq=>10
,p_name=>'Usage'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end PERIOD,',
'    sum(COST_MY_COST-nvl(COST_MY_COST_OVERAGE,0)) as COST_USAGE',
'from oci_cost',
'where ',
'    tenant_name=:P5_TENANT_NAME and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YY'
||'YY'') = :P5_PERIOD_RANGE) and',
'    not (:P5_TAG_SPECIAL is null and :P5_TENANT_ID is null and :P5_COMPARTMENT_NAME is null and :P5_PRODUCT_SERVICE is null and :P5_PRODUCT_REGION is null and :P5_COMPARTMENT_TOP is null and :P5_TAG_KEY is null and :P5_TAG_DATA is null and :P5_COST_P'
||'RODUCT_SKU is null) and',
'    :P5_REPORT_SELECTOR in (''Hourly Cost Over Time'',''Daily Cost Over Time'',''Weekly Cost Over Time'',''Monthly Cost Over Time'')    ',
'    group by ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end',
'union all',
'select ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end PERIOD,',
'    sum(COST_MY_COST-nvl(COST_MY_COST_OVERAGE,0)) as COST_USAGE',
'from oci_cost_stats',
'where ',
'    tenant_name=:P5_TENANT_NAME and',
'    (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YY'
||'YY'') = :P5_PERIOD_RANGE) and',
'    (:P5_TAG_SPECIAL is null and :P5_TENANT_ID is null and :P5_COMPARTMENT_NAME is null and :P5_PRODUCT_SERVICE is null and :P5_PRODUCT_REGION is null and :P5_COMPARTMENT_TOP is null and :P5_TAG_KEY is null and :P5_TAG_DATA is null and :P5_COST_PRODU'
||'CT_SKU is null) and',
'    :P5_REPORT_SELECTOR in (''Hourly Cost Over Time'',''Daily Cost Over Time'',''Weekly Cost Over Time'',''Monthly Cost Over Time'')    ',
'    group by ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end',
'order by 1',
'',
'',
'',
''))
,p_items_value_column_name=>'COST_USAGE'
,p_items_label_column_name=>'PERIOD'
,p_color=>'#34AADC'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'center'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_jet_chart_series(
 p_id=>wwv_flow_api.id(11933638002191629)
,p_chart_id=>wwv_flow_api.id(12036462660075984)
,p_seq=>20
,p_name=>'Overage'
,p_data_source_type=>'SQL'
,p_data_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end PERIOD,',
'    sum(nvl(COST_MY_COST_OVERAGE,0)) as COST_MY_COST_OVERAGE',
'from oci_cost',
'where ',
'    tenant_name=:P5_TENANT_NAME and',
'    (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'    (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'    (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'    (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'    (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'    (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'    (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'    (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'    (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'    (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YY'
||'YY'') = :P5_PERIOD_RANGE) and',
'    not (:P5_TAG_SPECIAL is null and :P5_TENANT_ID is null and :P5_COMPARTMENT_NAME is null and :P5_PRODUCT_SERVICE is null and :P5_PRODUCT_REGION is null and :P5_COMPARTMENT_TOP is null and :P5_TAG_KEY is null and :P5_TAG_DATA is null and :P5_COST_P'
||'RODUCT_SKU is null) and',
'    :P5_REPORT_SELECTOR in (''Hourly Cost Over Time'',''Daily Cost Over Time'',''Weekly Cost Over Time'',''Monthly Cost Over Time'')    ',
'    group by ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end',
'union all',
'select ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end PERIOD,',
'    sum(nvl(COST_MY_COST_OVERAGE,0)) as COST_USAGE',
'from oci_cost_stats',
'where ',
'    tenant_name=:P5_TENANT_NAME and',
'    (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YY'
||'YY'') = :P5_PERIOD_RANGE) and',
'    (:P5_TAG_SPECIAL is null and :P5_TENANT_ID is null and :P5_COMPARTMENT_NAME is null and :P5_PRODUCT_SERVICE is null and :P5_PRODUCT_REGION is null and :P5_COMPARTMENT_TOP is null and :P5_TAG_KEY is null and :P5_TAG_DATA is null and :P5_COST_PRODU'
||'CT_SKU is null) and',
'    :P5_REPORT_SELECTOR in (''Hourly Cost Over Time'',''Daily Cost Over Time'',''Weekly Cost Over Time'',''Monthly Cost Over Time'')    ',
'    group by ',
'    case ',
'        when :P5_PERIOD=''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD HH24'') ',
'        when :P5_PERIOD=''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'        when :P5_PERIOD=''Weekly'' then to_char(USAGE_INTERVAL_START,''YYYY-WW'') ',
'        when :P5_PERIOD=''Monthly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-MON'')',
'    end',
'order by 1',
'',
'',
'',
''))
,p_items_value_column_name=>'COST_MY_COST_OVERAGE'
,p_items_label_column_name=>'PERIOD'
,p_color=>'#FFCC00'
,p_assigned_to_y2=>'off'
,p_items_label_rendered=>true
,p_items_label_position=>'center'
,p_items_label_font_size=>'10'
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(12037572792075985)
,p_chart_id=>wwv_flow_api.id(12036462660075984)
,p_axis=>'y'
,p_is_rendered=>'on'
,p_format_type=>'decimal'
,p_decimal_places=>1
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_position=>'auto'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_jet_chart_axis(
 p_id=>wwv_flow_api.id(12036986078075984)
,p_chart_id=>wwv_flow_api.id(12036462660075984)
,p_axis=>'x'
,p_is_rendered=>'on'
,p_format_type=>'date-short'
,p_numeric_pattern=>'DD-MON-YYYY'
,p_format_scaling=>'auto'
,p_scaling=>'linear'
,p_baseline_scaling=>'zero'
,p_major_tick_rendered=>'on'
,p_minor_tick_rendered=>'off'
,p_tick_label_rendered=>'on'
,p_tick_label_rotation=>'auto'
,p_tick_label_position=>'outside'
,p_zoom_order_seconds=>false
,p_zoom_order_minutes=>false
,p_zoom_order_hours=>false
,p_zoom_order_days=>false
,p_zoom_order_weeks=>false
,p_zoom_order_months=>false
,p_zoom_order_quarters=>false
,p_zoom_order_years=>false
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(41488126786200900)
,p_plug_name=>'Graph Report Selector'
,p_parent_plug_id=>wwv_flow_api.id(33638842014589649)
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding:t-Region--removeHeader:t-Region--noUI:t-Region--hiddenOverflow:t-Form--noPadding:margin-top-none:margin-bottom-none:margin-left-none:margin-right-none'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>10
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'VALUE_OF_ITEM_IN_CONDITION_IN_COLON_DELIMITED_LIST'
,p_plug_display_when_condition=>'P5_REPORT_SELECTOR'
,p_plug_display_when_cond2=>'Daily Cost Report:Weekly Cost Report:Monthly Cost Report:Hourly Cost Report'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(33639012225589650)
,p_plug_name=>'Choose Tenant'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_source=>'No Data Found, Please Choose Tenant, Date and press Submit.'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_plug_display_condition_type=>'ITEM_IS_ZERO'
,p_plug_display_when_condition=>'P5_ROWS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
end;
/
begin
wwv_flow_api.create_page_button(
 p_id=>wwv_flow_api.id(12048960742076060)
,p_button_sequence=>120
,p_button_plug_id=>wwv_flow_api.id(22846551592241693)
,p_button_name=>'P5_SUBMIT'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#:t-Button--large:t-Button--stretch:t-Button--gapTop'
,p_button_template_id=>wwv_flow_api.id(9821119233688096)
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Submit'
,p_button_position=>'BODY'
,p_grid_new_row=>'Y'
,p_grid_column_span=>3
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11790776892177240)
,p_name=>'P5_TAG_SPECIAL'
,p_item_sequence=>160
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Tag Special Data'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P5_TENANT_NAME',
'    and ref_type=''TAG_SPECIAL''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P5_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11790835644177241)
,p_name=>'P5_ROWS_DISPLAY'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_api.id(22847044863241698)
,p_prompt=>'Rows Filtered'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11933331907191626)
,p_name=>'P5_PERIOD'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Report Period'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'STATIC2:Hourly;Hourly,Daily;Daily,Weekly;Weekly,Monthly;Monthly'
,p_lov_display_null=>'YES'
,p_lov_null_text=>'Please Choose'
,p_cHeight=>1
,p_tag_attributes=>'style="background-color:#e0f0f0"'
,p_begin_on_new_line=>'N'
,p_colspan=>3
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11933438111191627)
,p_name=>'P5_PERIOD_RANGE'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_item_default=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select max(',
'          case ',
'              when :P5_PERIOD = ''Hourly'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'              when :P5_PERIOD = ''Daily'' or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY-MM'') ',
'              when :P5_PERIOD in (''Monthly'',''Weekly'') then to_char(USAGE_INTERVAL_START,''YYYY'') ',
'          end) period',
'     from ',
'         oci_cost_stats',
'     where',
'     tenant_name=:P5_TENANT_NAME and (:P5_PERIOD <> ''Hourly'' or USAGE_INTERVAL_START<trunc(sysdate)-2)',
''))
,p_item_default_type=>'SQL_QUERY'
,p_prompt=>'Year / Month / Day'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    case when :P5_PERIOD = ''Hourly'' then period_d else period_r end o, period_r r',
'from ',
'(',
'     select ',
'          case ',
'              when :P5_PERIOD = ''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD DY'') ',
'              when :P5_PERIOD = ''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM'') ',
'              when :P5_PERIOD in (''Monthly'',''Weekly'') or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY'') ',
'          end||'' - ''||to_char(sum(COST_MY_COST),''999,999,999.9'') period_d,',
'          case ',
'              when :P5_PERIOD = ''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'              when :P5_PERIOD = ''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM'') ',
'              when :P5_PERIOD in (''Monthly'',''Weekly'') or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY'') ',
'          end period_r',
'     from ',
'         oci_cost_stats',
'     where',
'         tenant_name=:P5_TENANT_NAME and :P5_PERIOD is not null',
'         and (:P5_PERIOD <> ''Hourly'' or USAGE_INTERVAL_START>trunc(sysdate)-90 and USAGE_INTERVAL_START<trunc(sysdate)-2)',
'     group by ',
'          case ',
'              when :P5_PERIOD = ''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD DY'') ',
'              when :P5_PERIOD = ''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM'') ',
'              when :P5_PERIOD in (''Monthly'',''Weekly'') or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY'') ',
'          end ,',
'          case ',
'              when :P5_PERIOD = ''Hourly'' then to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') ',
'              when :P5_PERIOD = ''Daily'' then to_char(USAGE_INTERVAL_START,''YYYY-MM'') ',
'              when :P5_PERIOD in (''Monthly'',''Weekly'') or :P5_PERIOD is null then to_char(USAGE_INTERVAL_START,''YYYY'') ',
'          end ',
'     order by 1',
')'))
,p_lov_cascade_parent_items=>'P5_PERIOD,P5_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_tag_attributes=>'style="background-color:#e0f0f0"'
,p_begin_on_new_line=>'N'
,p_colspan=>3
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11933828594191631)
,p_name=>'P5_REPORT_GROUP'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_api.id(41488126786200900)
,p_item_default=>'Product'
,p_prompt=>'Report Group Option'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'STATIC2:Product;Product,Region;Region,Top Compartment;Top Compartment,Compartment;Compartment,Tenant;Tenant,Tag Special;Tag Special'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'SUBMIT'
,p_attribute_03=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11979657320439228)
,p_name=>'P5_TAG_SPECIAL_KEY'
,p_item_sequence=>150
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Tag Special Key'
,p_format_mask=>'FML999G999G999G999G990D00'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P5_TENANT_NAME',
'    and ref_type=''TAG_SPECIAL_KEY''',
'order by 1'))
,p_source_type=>'QUERY_COLON'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_begin_on_new_line=>'N'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12049317069076061)
,p_name=>'P5_TENANT_NAME'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Tenant Name'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'select distinct tenant_name o, tenant_name r from oci_cost_stats order by 1'
,p_lov_display_null=>'YES'
,p_lov_null_text=>'Please Choose...'
,p_cHeight=>1
,p_tag_attributes=>'style="background-color:#e0f0f0"'
,p_colspan=>3
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12050196618076063)
,p_name=>'P5_PRODUCT_SERVICE'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Product Service'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P5_TENANT_NAME',
'    and ref_type=''PRD_SERVICE''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P5_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12050537615076064)
,p_name=>'P5_COMPARTMENT_TOP'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Top Level Compartment'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P5_TENANT_NAME',
'    and ref_type=''PRD_COMPARTMENT_PATH''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P5_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12050935981076064)
,p_name=>'P5_PRODUCT_REGION'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Product Region'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P5_TENANT_NAME',
'    and ref_type=''PRD_REGION''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P5_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12051779019076065)
,p_name=>'P5_COST_PRODUCT_SKU'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Product SKU'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, substr(ref_name,1,6) r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P5_TENANT_NAME',
'    and ref_type=''COST_PRODUCT_SKU''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P5_TENANT_NAME,P5_PERIOD_RANGE'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12052102329076065)
,p_name=>'P5_COMPARTMENT_NAME'
,p_item_sequence=>140
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Compartment'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P5_TENANT_NAME',
'    and ref_type=''PRD_COMPARTMENT_NAME''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P5_TENANT_NAME,P5_PERIOD_RANGE'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12052925060076066)
,p_name=>'P5_TAG_KEY'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Tag Key'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select distinct tag_key o, tag_key r ',
'from ',
'    oci_cost_tag_keys',
'where',
'    tenant_name=:P5_TENANT_NAME',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P5_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12053398346076066)
,p_name=>'P5_TAG_DATA'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Tag Data Filter'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>30
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'N'
,p_attribute_02=>'N'
,p_attribute_04=>'TEXT'
,p_attribute_05=>'BOTH'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12054081919076067)
,p_name=>'P5_COST'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(22847044863241698)
,p_prompt=>'Total Cost'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12054885234076067)
,p_name=>'P5_ROWS'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_api.id(22847044863241698)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12055265653076068)
,p_name=>'P5_SUBSCRIPTION'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_api.id(22847044863241698)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Subscription Id'
,p_format_mask=>'FML999G999G999G999G990D00'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P5_TENANT_NAME',
'    and ref_type=''COST_SUBSCRIPTION_ID''',
'order by 1'))
,p_source_type=>'QUERY_COLON'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_begin_on_new_line=>'N'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12306112237574233)
,p_name=>'P5_TENANT_ID'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Tenant Id'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ref_name o, ref_name r ',
'from ',
'    OCI_COST_REFERENCE ',
'where',
'    tenant_name=:P5_TENANT_NAME',
'    and ref_type=''TENANT_ID''',
'order by 1'))
,p_lov_display_null=>'YES'
,p_lov_null_text=>'All'
,p_lov_cascade_parent_items=>'P5_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_colspan=>3
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(14166029459944674)
,p_name=>'P5_REPORT_SELECTOR'
,p_item_sequence=>130
,p_item_plug_id=>wwv_flow_api.id(22846551592241693)
,p_prompt=>'Chart/Report Selector'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'with data as',
'(',
'    select ''Hourly Cost Over Time - Total'' report_name from dual where :P5_PERIOD=''Hourly''',
'    union all',
'    select ''Hourly Cost Over Time'' report_name from dual where :P5_PERIOD=''Hourly''',
'    union all',
'    select ''Hourly Cost By Service'' report_name from dual where :P5_PERIOD=''Hourly''',
'    union all',
'    select ''Hourly Cost By SKU'' report_name from dual where :P5_PERIOD=''Hourly''',
'    union all',
'    select ''Hourly Cost By Region'' report_name from dual where :P5_PERIOD=''Hourly''',
'    union all',
'    select ''Hourly Cost By Compartment'' report_name from dual where :P5_PERIOD=''Hourly''',
'    union all',
'    select ''Hourly Cost By Top Compartment'' report_name from dual where :P5_PERIOD=''Hourly''',
'    union all',
'    select ''Hourly Cost Report'' report_name from dual where :P5_PERIOD=''Hourly''',
'    union all',
'    select ''Hourly Product Unit Report'' report_name from dual where :P5_PERIOD=''Hourly''',
'    union all',
'    select ''Daily Cost Over Time - Total'' report_name from dual where :P5_PERIOD=''Daily''',
'    union all',
'    select ''Daily Cost Over Time'' report_name from dual where :P5_PERIOD=''Daily''',
'    union all',
'    select ''Daily Cost By Service'' report_name from dual where :P5_PERIOD=''Daily''',
'    union all',
'    select ''Daily Cost By SKU'' report_name from dual where :P5_PERIOD=''Daily''',
'    union all',
'    select ''Daily Cost By Region'' report_name from dual where :P5_PERIOD=''Daily''',
'    union all',
'    select ''Daily Cost By Compartment'' report_name from dual where :P5_PERIOD=''Daily''',
'    union all',
'    select ''Daily Cost By Top Compartment'' report_name from dual where :P5_PERIOD=''Daily''',
'    union all',
'    select ''Daily Cost Report'' report_name from dual where :P5_PERIOD=''Daily''',
'    union all',
'    select ''Daily Product Unit Report - Single'' report_name from dual where :P5_PERIOD=''Daily''',
'    union all',
'    select ''Daily Product Unit Report - Total'' report_name from dual where :P5_PERIOD=''Daily''',
'    union all',
'    select ''Weekly Cost Over Time - Total'' report_name from dual where :P5_PERIOD=''Weekly''',
'    union all',
'    select ''Weekly Cost Over Time'' report_name from dual where :P5_PERIOD=''Weekly''',
'    union all',
'    select ''Weekly Cost By Service'' report_name from dual where :P5_PERIOD=''Weekly''',
'    union all',
'    select ''Weekly Cost By SKU'' report_name from dual where :P5_PERIOD=''Weekly''',
'    union all',
'    select ''Weekly Cost By Region'' report_name from dual where :P5_PERIOD=''Weekly''',
'    union all',
'    select ''Weekly Cost By Compartment'' report_name from dual where :P5_PERIOD=''Weekly''',
'    union all',
'    select ''Weekly Cost By Top Compartment'' report_name from dual where :P5_PERIOD=''Weekly''',
'    union all',
'    select ''Weekly Cost Report'' report_name from dual where :P5_PERIOD=''Weekly''',
'    union all',
'    select ''Weekly Product Unit Report'' report_name from dual where :P5_PERIOD=''Weekly''',
'    union all',
'    select ''Monthly Cost Over Time - Total'' report_name from dual where :P5_PERIOD=''Monthly''',
'    union all',
'    select ''Monthly Cost Over Time'' report_name from dual where :P5_PERIOD=''Monthly''',
'    union all',
'    select ''Monthly Cost By Service'' report_name from dual where :P5_PERIOD=''Monthly''',
'    union all',
'    select ''Monthly Cost By SKU'' report_name from dual where :P5_PERIOD=''Monthly''',
'    union all',
'    select ''Monthly Cost By Region'' report_name from dual where :P5_PERIOD=''Monthly''',
'    union all',
'    select ''Monthly Cost By Compartment'' report_name from dual where :P5_PERIOD=''Monthly''',
'    union all',
'    select ''Monthly Cost By Top Compartment'' report_name from dual where :P5_PERIOD=''Monthly''',
'    union all',
'    select ''Monthly Cost Report'' report_name from dual where :P5_PERIOD=''Monthly''',
'    union all',
'    select ''Monthly Product Unit Report'' report_name from dual where :P5_PERIOD=''Monthly''',
')',
'select report_name r, report_name o',
'from data',
''))
,p_lov_cascade_parent_items=>'P5_PERIOD'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>3
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(14186230501270003)
,p_name=>'P5_YEARLY'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_api.id(22847044863241698)
,p_prompt=>'Yearly Prediction'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_begin_on_new_line=>'N'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(15475859577450204)
,p_name=>'P5_LAST_DATE_LOADED'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_api.id(22847044863241698)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Last Date Loaded'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'    to_char(max(USAGE_INTERVAL_START),''MM/DD/YY HH24:MI'') dte',
'from oci_cost_stats',
'where ',
'    tenant_name=:P5_TENANT_NAME'))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(15476787556464715)
,p_name=>'P5_DAYS_DATA'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_api.id(22847044863241698)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Days of Data'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select to_char(sum(cnt)/24,''99999.0'')',
'from',
'(',
'    select ',
'        count(distinct USAGE_INTERVAL_START) cnt',
'    from oci_cost',
'    where ',
'        tenant_name=:P5_TENANT_NAME and',
'        (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'        (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'        (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'        (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'        (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'        (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'        (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'        (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'        (:P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YYYY'') = :P5_PERIOD_RANGE) and',
'        not (:P5_COMPARTMENT_NAME is null and :P5_PRODUCT_SERVICE is null and :P5_PRODUCT_REGION is null and :P5_COMPARTMENT_TOP is null and :P5_TAG_KEY is null and :P5_TAG_DATA is null and :P5_COST_PRODUCT_SKU is null)',
'    union all',
'    select ',
'        count(distinct USAGE_INTERVAL_START) cnt',
'    from oci_cost_stats',
'    where ',
'        tenant_name=:P5_TENANT_NAME and',
'        (:P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START,''YYYY'') = :P5_PERIOD_RANGE) and',
'        (:P5_TENANT_ID is null and :P5_COMPARTMENT_NAME is null and :P5_PRODUCT_SERVICE is null and :P5_PRODUCT_REGION is null and :P5_COMPARTMENT_TOP is null and :P5_TAG_KEY is null and :P5_TAG_DATA is null and :P5_COST_PRODUCT_SKU is null)',
')'))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_tag_attributes=>'style="background-color:#e8e8e8"'
,p_begin_on_new_line=>'N'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_attribute_01=>'Y'
,p_attribute_02=>'VALUE'
,p_attribute_04=>'Y'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(11934077528191633)
,p_computation_sequence=>10
,p_computation_item=>'P5_REPORT_GROUP'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'STATIC_ASSIGNMENT'
,p_computation=>'Product'
,p_compute_when=>'P5_REPORT_GROUP'
,p_compute_when_type=>'ITEM_IS_NULL'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(11935725590191650)
,p_computation_sequence=>10
,p_computation_item=>'P5_TENANT_NAME'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'QUERY'
,p_computation=>'select tenant_name from oci_cost_stats where rownum=1'
,p_compute_when=>'P5_TENANT_NAME'
,p_compute_when_type=>'ITEM_IS_NULL'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(14186327524270004)
,p_computation_sequence=>10
,p_computation_item=>'P5_REPORT_SELECTOR'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'STATIC_ASSIGNMENT'
,p_computation=>'Daily Cost Over Time - Total'
,p_compute_when=>'P5_REPORT_SELECTOR'
,p_compute_when_type=>'ITEM_IS_NULL'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(12277632815302643)
,p_computation_sequence=>15
,p_computation_item=>'P5_PERIOD_RANGE'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'QUERY'
,p_computation=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select max(to_char(USAGE_INTERVAL_START,''YYYY-MM''))',
'from ',
'     oci_cost_stats',
'where',
'tenant_name=:P5_TENANT_NAME '))
,p_compute_when=>'P5_PERIOD_RANGE'
,p_compute_when_type=>'ITEM_IS_NULL'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(11934196423191634)
,p_computation_sequence=>20
,p_computation_item=>'P5_PERIOD'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'STATIC_ASSIGNMENT'
,p_computation=>'Daily'
,p_compute_when=>'P5_PERIOD'
,p_compute_when_type=>'ITEM_IS_NULL'
);
wwv_flow_api.create_page_process(
 p_id=>wwv_flow_api.id(11790922385177242)
,p_process_sequence=>10
,p_process_point=>'AFTER_HEADER'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'PreFill'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'begin',
'select ',
'    to_char(nvl(sum(COST_MY_COST),0),''999,999,999,990.00'')||'' ''||min(COST_CURRENCY_CODE) MY_COST,',
'    to_char(nvl(sum(ESTIMATE_YEAR),0),''999,999,999,990'')||'' ''||min(COST_CURRENCY_CODE) MY_COST_YEAR,',
'    to_char(sum(cnt),''999,999,999,999'') NUM_ROWS,',
'    sum(cnt) NUM_ROWS_DISPLAY',
'into',
'    :P5_COST,',
'    :P5_YEARLY,',
'    :P5_ROWS_DISPLAY,',
'    :P5_ROWS',
'from ',
'(',
'    select ',
'        sum(COST_MY_COST) COST_MY_COST, ',
'        min(COST_CURRENCY_CODE) COST_CURRENCY_CODE,',
'        sum(COST_MY_COST)*(24 * 365 / count(distinct USAGE_INTERVAL_START)) ESTIMATE_YEAR,',
'        count(*) CNT',
'    from oci_cost',
'    where ',
'        tenant_name=:P5_TENANT_NAME and',
'        (:P5_COMPARTMENT_NAME is null or prd_compartment_name = :P5_COMPARTMENT_NAME) and',
'        (:P5_PRODUCT_SERVICE is null or prd_service = :P5_PRODUCT_SERVICE) and',
'        (:P5_PRODUCT_REGION is null or prd_region = :P5_PRODUCT_REGION) and',
'        (:P5_TENANT_ID is null or tenant_id = :P5_TENANT_ID) and',
'        (:P5_COMPARTMENT_TOP is null or prd_compartment_path like :P5_COMPARTMENT_TOP ||''%'') and',
'        (:P5_TAG_KEY is null or tags_data like ''%#'' || :P5_TAG_KEY || ''=%'') and',
'        (:P5_TAG_DATA is null or tags_data like ''%#'' || nvl(:P5_TAG_KEY,''%'') || ''=%'' || :P5_TAG_DATA || ''#'') and',
'        (:P5_TAG_SPECIAL is null or :P5_TAG_SPECIAL = TAG_SPECIAL) and',
'        (:P5_COST_PRODUCT_SKU is null or COST_PRODUCT_SKU = :P5_COST_PRODUCT_SKU) and',
'        (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START'
||',''YYYY'') = :P5_PERIOD_RANGE) and',
'        not (:P5_TENANT_ID is null and :P5_COMPARTMENT_NAME is null and :P5_PRODUCT_SERVICE is null and :P5_PRODUCT_REGION is null and :P5_COMPARTMENT_TOP is null and :P5_TAG_KEY is null and :P5_TAG_DATA is null and :P5_COST_PRODUCT_SKU is null and :'
||'P5_TAG_SPECIAL is null)',
'    union all',
'    select',
'        sum(COST_MY_COST) COST_MY_COST, ',
'        min(COST_CURRENCY_CODE) COST_CURRENCY_CODE,',
'        sum(COST_MY_COST)*(24 * 365 / count(distinct USAGE_INTERVAL_START)) ESTIMATE_YEAR,',
'        sum(num_rows) cnt',
'    from oci_cost_stats',
'    where ',
'        tenant_name=:P5_TENANT_NAME and',
'        (:P5_PERIOD=''Hourly'' and to_char(USAGE_INTERVAL_START,''YYYY-MM-DD'') = :P5_PERIOD_RANGE or :P5_PERIOD=''Daily'' and to_char(USAGE_INTERVAL_START,''YYYY-MM'') = :P5_PERIOD_RANGE or :P5_PERIOD in (''Monthly'',''Weekly'') and to_char(USAGE_INTERVAL_START'
||',''YYYY'') = :P5_PERIOD_RANGE) and',
'        (:P5_COMPARTMENT_NAME is null and :P5_PRODUCT_SERVICE is null and :P5_PRODUCT_REGION is null and :P5_COMPARTMENT_TOP is null and :P5_TAG_KEY is null and :P5_TAG_DATA is null and :P5_COST_PRODUCT_SKU is null and :P5_TENANT_ID is null and :P5_T'
||'AG_SPECIAL is null)',
');',
'end;'))
,p_process_clob_language=>'PLSQL'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
);
end;
/
prompt --application/pages/page_00006
begin
wwv_flow_api.create_page(
 p_id=>6
,p_user_interface_id=>wwv_flow_api.id(9843694399688199)
,p_name=>'Data Statistics'
,p_step_title=>'Data Statistics'
,p_warn_on_unsaved_changes=>'N'
,p_autocomplete_on_off=>'OFF'
,p_inline_css=>wwv_flow_string.join(wwv_flow_t_varchar2(
'.a-IRR-table tr td[headers*="rep_col_grey"]',
'{',
'    background-color: #efffff;',
'}'))
,p_page_template_options=>'#DEFAULT#'
,p_last_updated_by=>'ADIZOHAR'
,p_last_upd_yyyymmddhh24miss=>'20201103122042'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(11208064619636616)
,p_plug_name=>'Cost Summary Monthly'
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>40
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'	tenant_name, ',
'	month6, ',
'	month5, ',
'	month4, ',
'	month3, ',
'	month2, ',
'	month1, ',
'	case when trunc(greatest(month1,month2,month3,month4,month5,month6)) = trunc(month1) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as month1_color,',
'	case when trunc(greatest(month1,month2,month3,month4,month5,month6)) = trunc(month2) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as month2_color,',
'	case when trunc(greatest(month1,month2,month3,month4,month5,month6)) = trunc(month3) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as month3_color,',
'	case when trunc(greatest(month1,month2,month3,month4,month5,month6)) = trunc(month4) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as month4_color,',
'	case when trunc(greatest(month1,month2,month3,month4,month5,month6)) = trunc(month5) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as month5_color,',
'	case when trunc(greatest(month1,month2,month3,month4,month5,month6)) = trunc(month6) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as month6_color',
'from',
'(',
'    select ',
'        tenant_name,',
'        sum(case when trunc(USAGE_INTERVAL_START,''MM'') = add_months(trunc(sysdate,''MM''),-5) then COST_MY_COST else 0 end) month6,',
'        sum(case when trunc(USAGE_INTERVAL_START,''MM'') = add_months(trunc(sysdate,''MM''),-4) then COST_MY_COST else 0 end) month5,',
'        sum(case when trunc(USAGE_INTERVAL_START,''MM'') = add_months(trunc(sysdate,''MM''),-3) then COST_MY_COST else 0 end) month4,',
'        sum(case when trunc(USAGE_INTERVAL_START,''MM'') = add_months(trunc(sysdate,''MM''),-2) then COST_MY_COST else 0 end) month3,',
'        sum(case when trunc(USAGE_INTERVAL_START,''MM'') = add_months(trunc(sysdate,''MM''),-1) then COST_MY_COST else 0 end) month2,',
'        sum(case when trunc(USAGE_INTERVAL_START,''MM'') = add_months(trunc(sysdate,''MM''), 0) then COST_MY_COST else 0 end) month1',
'    from oci_cost_stats',
'    where ',
'        tenant_name like ''%'' and',
'        USAGE_INTERVAL_START >= add_months(trunc(sysdate,''MM''),-5)',
'    group by tenant_name',
')',
'order by 1'))
,p_plug_source_type=>'NATIVE_IR'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
wwv_flow_api.create_worksheet(
 p_id=>wwv_flow_api.id(11208874726636624)
,p_max_row_count=>'1000000'
,p_show_nulls_as=>'-'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_show_search_bar=>'N'
,p_report_list_mode=>'TABS'
,p_show_detail_link=>'N'
,p_owner=>'ADIZOHAR'
,p_internal_uid=>11208874726636624
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11208958434636625)
,p_db_column_name=>'TENANT_NAME'
,p_display_order=>10
,p_column_identifier=>'A'
,p_column_label=>'Tenant Name'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11211127457636647)
,p_db_column_name=>'MONTH6'
,p_display_order=>20
,p_column_identifier=>'B'
,p_column_label=>'&P6_MONTH6.'
,p_column_html_expression=>'<span  style="#MONTH6_COLOR#">#MONTH6#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11211295849636648)
,p_db_column_name=>'MONTH5'
,p_display_order=>30
,p_column_identifier=>'C'
,p_column_label=>'&P6_MONTH5.'
,p_column_html_expression=>'<span  style="#MONTH5_COLOR#">#MONTH5#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11211379215636649)
,p_db_column_name=>'MONTH4'
,p_display_order=>40
,p_column_identifier=>'D'
,p_column_label=>'&P6_MONTH4.'
,p_column_html_expression=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<span style="#MONTH4_COLOR#">#MONTH4#</span>',
''))
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(11211494413636650)
,p_db_column_name=>'MONTH3'
,p_display_order=>50
,p_column_identifier=>'E'
,p_column_label=>'&P6_MONTH3.'
,p_column_html_expression=>'<span  style="#MONTH3_COLOR#">#MONTH3#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12302959449574201)
,p_db_column_name=>'MONTH2'
,p_display_order=>60
,p_column_identifier=>'F'
,p_column_label=>'&P6_MONTH2.'
,p_column_html_expression=>'<span style="#MONTH2_COLOR#">#MONTH2#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12303005990574202)
,p_db_column_name=>'MONTH1'
,p_display_order=>70
,p_column_identifier=>'G'
,p_column_label=>'&P6_MONTH1.'
,p_column_html_expression=>'<span  style="#MONTH1_COLOR#">#MONTH1#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12303171514574203)
,p_db_column_name=>'MONTH1_COLOR'
,p_display_order=>80
,p_column_identifier=>'H'
,p_column_label=>'Month1 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12303287884574204)
,p_db_column_name=>'MONTH2_COLOR'
,p_display_order=>90
,p_column_identifier=>'I'
,p_column_label=>'Month2 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12303344220574205)
,p_db_column_name=>'MONTH3_COLOR'
,p_display_order=>100
,p_column_identifier=>'J'
,p_column_label=>'Month3 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12303498895574206)
,p_db_column_name=>'MONTH4_COLOR'
,p_display_order=>110
,p_column_identifier=>'K'
,p_column_label=>'Month4 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12303540909574207)
,p_db_column_name=>'MONTH5_COLOR'
,p_display_order=>120
,p_column_identifier=>'L'
,p_column_label=>'Month5 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12303610921574208)
,p_db_column_name=>'MONTH6_COLOR'
,p_display_order=>130
,p_column_identifier=>'M'
,p_column_label=>'Month6 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_rpt(
 p_id=>wwv_flow_api.id(12307939956592577)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'123080'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'TENANT_NAME:MONTH6:MONTH5:MONTH4:MONTH3:MONTH2:MONTH1:MONTH1_COLOR:MONTH2_COLOR:MONTH3_COLOR:MONTH4_COLOR:MONTH5_COLOR:MONTH6_COLOR'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(12552815670313326)
,p_plug_name=>'Usage Statistics - &P6_USAGE_SIZE.'
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>50
,p_plug_display_point=>'BODY'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select /*+ parallel(oci_usage,4) */ ',
'    tenant_name,',
'    to_char(min(USAGE_INTERVAL_START),''MM/DD/YYYY HH24:MI'') MIN_FILE_TIME, ',
'    to_char(max(USAGE_INTERVAL_START),''MM/DD/YYYY HH24:MI'') MAX_FILE_TIME, ',
'    min(file_id) MIN_FILE_ID, ',
'    max(file_id) MAX_FILE_ID, ',
'    count(distinct file_id) num_files, ',
'    sum(num_rows) as num_rows , ',
'    count(distinct USAGE_INTERVAL_START) num_hours,',
'    count(distinct trunc(USAGE_INTERVAL_START)) num_days,',
'    to_char(max(UPDATE_DATE),''MM/DD/YYYY HH24:MI'') LAST_LOAD,',
'    max(AGENT_VERSION) agent_version',
'from ',
'    oci_usage_stats',
'group by tenant_name',
'order by 1,2'))
,p_plug_source_type=>'NATIVE_IR'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet(
 p_id=>wwv_flow_api.id(13352241944239119)
,p_max_row_count=>'1000000'
,p_show_nulls_as=>'-'
,p_show_search_bar=>'N'
,p_report_list_mode=>'TABS'
,p_show_detail_link=>'N'
,p_owner=>'ADI.ZOHAR@ORACLE.COM'
,p_internal_uid=>13352241944239119
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13352369085239120)
,p_db_column_name=>'TENANT_NAME'
,p_display_order=>10
,p_column_identifier=>'A'
,p_column_label=>'Tenant Name'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13352426316239121)
,p_db_column_name=>'MIN_FILE_TIME'
,p_display_order=>20
,p_column_identifier=>'B'
,p_column_label=>'Min File Time'
,p_column_html_expression=>'<span style="white-space:nowrap;">#MIN_FILE_TIME#</span>'
,p_column_type=>'STRING'
,p_heading_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13352557224239122)
,p_db_column_name=>'MAX_FILE_TIME'
,p_display_order=>30
,p_column_identifier=>'C'
,p_column_label=>'Max File Time'
,p_column_html_expression=>'<span style="white-space:nowrap;">#MAX_FILE_TIME#</span>'
,p_column_type=>'STRING'
,p_heading_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13352647044239123)
,p_db_column_name=>'MIN_FILE_ID'
,p_display_order=>40
,p_column_identifier=>'D'
,p_column_label=>'Min File Id'
,p_column_type=>'STRING'
,p_heading_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13352720186239124)
,p_db_column_name=>'MAX_FILE_ID'
,p_display_order=>50
,p_column_identifier=>'E'
,p_column_label=>'Max File Id'
,p_column_type=>'STRING'
,p_heading_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13352865882239125)
,p_db_column_name=>'NUM_FILES'
,p_display_order=>60
,p_column_identifier=>'F'
,p_column_label=>'Num Files'
,p_column_type=>'NUMBER'
,p_heading_alignment=>'RIGHT'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13352980351239126)
,p_db_column_name=>'NUM_ROWS'
,p_display_order=>70
,p_column_identifier=>'G'
,p_column_label=>'Num Rows'
,p_column_type=>'NUMBER'
,p_heading_alignment=>'RIGHT'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13353042517239127)
,p_db_column_name=>'NUM_HOURS'
,p_display_order=>80
,p_column_identifier=>'H'
,p_column_label=>'Num Hours'
,p_column_type=>'NUMBER'
,p_heading_alignment=>'RIGHT'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13353118811239128)
,p_db_column_name=>'NUM_DAYS'
,p_display_order=>90
,p_column_identifier=>'I'
,p_column_label=>'Num Days'
,p_column_type=>'NUMBER'
,p_heading_alignment=>'RIGHT'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13353217852239129)
,p_db_column_name=>'LAST_LOAD'
,p_display_order=>100
,p_column_identifier=>'J'
,p_column_label=>'Last Load'
,p_column_html_expression=>'<span style="white-space:nowrap;">#LAST_LOAD#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13353317412239130)
,p_db_column_name=>'AGENT_VERSION'
,p_display_order=>110
,p_column_identifier=>'K'
,p_column_label=>'Agent Version'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_rpt(
 p_id=>wwv_flow_api.id(13572892797010445)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'135729'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'TENANT_NAME:MIN_FILE_TIME:MAX_FILE_TIME:MIN_FILE_ID:MAX_FILE_ID:NUM_FILES:NUM_ROWS:NUM_HOURS:NUM_DAYS:LAST_LOAD:AGENT_VERSION'
,p_sum_columns_on_break=>'NUM_ROWS:NUM_FILES'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(12630713145041599)
,p_plug_name=>'Cost Statistics - &P6_COST_SIZE.'
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>20
,p_plug_display_point=>'BODY'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'with full_days as',
'(',
'    select ',
'        tenant_name, ',
'        max(COST_DAY) MAX_COST_DAY,',
'        avg(COST_DAY) AVG_COST_DAY,',
'        to_Char(min(date_day),''MM/DD/YYYY'') MIN_FULL_DAY,',
'        to_Char(max(date_day),''MM/DD/YYYY'') MAX_FULL_DAY,',
'        count(*) NUM_FULL_DAYS',
'    from',
'    (',
'        select /*+ parallel(a,4) materialize */ ',
'            tenant_name,',
'            trunc(USAGE_INTERVAL_START) date_day,',
'            count(distinct USAGE_INTERVAL_START) DAY_HOURS,',
'            sum(COST_MY_COST) COST_DAY',
'        from oci_cost_stats a',
'        group by ',
'            tenant_name,',
'            trunc(USAGE_INTERVAL_START) ',
'        having count(distinct USAGE_INTERVAL_START) = 24 ',
'    )',
'    group by tenant_name',
'),',
'total_stats as',
'(',
'    select /*+ parallel(a,4) materialize */ ',
'        tenant_name,',
'        to_char(min(USAGE_INTERVAL_START),''MM/DD/YYYY HH24:MI'') MIN_FILE_TIME, ',
'        to_char(max(USAGE_INTERVAL_START),''MM/DD/YYYY HH24:MI'') MAX_FILE_TIME, ',
'        min(file_id) MIN_FILE_ID, ',
'        max(file_id) MAX_FILE_ID, ',
'        count(distinct file_id) num_files, ',
'        sum(num_rows) as num_rows,',
'        to_char(max(UPDATE_DATE),''MM/DD/YYYY HH24:MI'') LAST_LOAD,',
'        max(agent_version) AGENT_VERSION',
'    from ',
'        oci_cost_stats a',
'    group by tenant_name',
')',
'select ',
'    a.tenant_name,',
'    a.MIN_FILE_TIME, ',
'    a.MAX_FILE_TIME, ',
'    a.MIN_FILE_ID, ',
'    a.MAX_FILE_ID, ',
'    a.num_files, ',
'    a.num_rows,',
'    b.AVG_COST_DAY,',
'    b.MAX_COST_DAY,',
'    nvl(b.NUM_FULL_DAYS,0) NUM_FULL_DAYS,',
'    (select count(*) from OCI_COST_REFERENCE b where a.tenant_name=b.tenant_name and ref_type=''TENANT_ID'') sub_tenants,',
'    LAST_LOAD,',
'    AGENT_VERSION',
'from',
'    total_stats a,',
'    full_days b',
'where ',
'    a.tenant_name = b.tenant_name(+)',
'order by 1'))
,p_plug_source_type=>'NATIVE_IR'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet(
 p_id=>wwv_flow_api.id(13350953403239106)
,p_max_row_count=>'1000000'
,p_show_nulls_as=>'-'
,p_show_search_bar=>'N'
,p_show_detail_link=>'N'
,p_owner=>'ADI.ZOHAR@ORACLE.COM'
,p_internal_uid=>13350953403239106
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13351039214239107)
,p_db_column_name=>'TENANT_NAME'
,p_display_order=>10
,p_column_identifier=>'A'
,p_column_label=>'Tenant Name'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13351130671239108)
,p_db_column_name=>'MIN_FILE_TIME'
,p_display_order=>20
,p_column_identifier=>'B'
,p_column_label=>'Min File Time'
,p_column_html_expression=>'<span style="white-space:nowrap;">#MIN_FILE_TIME#</span>'
,p_column_type=>'STRING'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13351202600239109)
,p_db_column_name=>'MAX_FILE_TIME'
,p_display_order=>30
,p_column_identifier=>'C'
,p_column_label=>'Max File Time'
,p_column_html_expression=>'<span style="white-space:nowrap;">#MAX_FILE_TIME#</span>'
,p_column_type=>'STRING'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13351308990239110)
,p_db_column_name=>'MIN_FILE_ID'
,p_display_order=>40
,p_column_identifier=>'D'
,p_column_label=>'Min File Id'
,p_column_type=>'STRING'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13351432207239111)
,p_db_column_name=>'MAX_FILE_ID'
,p_display_order=>50
,p_column_identifier=>'E'
,p_column_label=>'Max File Id'
,p_column_type=>'STRING'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13351587991239112)
,p_db_column_name=>'NUM_FILES'
,p_display_order=>60
,p_column_identifier=>'F'
,p_column_label=>'Num Files'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13351697692239113)
,p_db_column_name=>'NUM_ROWS'
,p_display_order=>70
,p_column_identifier=>'G'
,p_column_label=>'Num Rows'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13351750794239114)
,p_db_column_name=>'AVG_COST_DAY'
,p_display_order=>80
,p_column_identifier=>'H'
,p_column_label=>'Avg Cost Day'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13351817776239115)
,p_db_column_name=>'MAX_COST_DAY'
,p_display_order=>90
,p_column_identifier=>'I'
,p_column_label=>'Max Cost Day'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13351909314239116)
,p_db_column_name=>'NUM_FULL_DAYS'
,p_display_order=>100
,p_column_identifier=>'J'
,p_column_label=>'Num Full Days'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16674398414602122)
,p_db_column_name=>'SUB_TENANTS'
,p_display_order=>110
,p_column_identifier=>'M'
,p_column_label=>'Sub Tenants'
,p_column_type=>'NUMBER'
,p_column_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13352074223239117)
,p_db_column_name=>'LAST_LOAD'
,p_display_order=>120
,p_column_identifier=>'K'
,p_column_label=>'Last Load'
,p_column_html_expression=>'<span style="white-space:nowrap;">#LAST_LOAD#</span>'
,p_column_type=>'STRING'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(13352104278239118)
,p_db_column_name=>'AGENT_VERSION'
,p_display_order=>130
,p_column_identifier=>'L'
,p_column_label=>'Agent Version'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_rpt(
 p_id=>wwv_flow_api.id(13572217165010430)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_type=>'REPORT'
,p_report_alias=>'135723'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'TENANT_NAME:MIN_FILE_TIME:MAX_FILE_TIME:MIN_FILE_ID:MAX_FILE_ID:NUM_FILES:NUM_ROWS:AVG_COST_DAY:MAX_COST_DAY:NUM_FULL_DAYS:SUB_TENANTS:LAST_LOAD:AGENT_VERSION:'
,p_sum_columns_on_break=>'NUM_ROWS:NUM_FILES'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(14188632778270027)
,p_plug_name=>'Cost Summary Last 7 Days'
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'	tenant_name, ',
'	day7, ',
'	day6, ',
'	day5, ',
'	day4, ',
'	day3, ',
'	day2, ',
'	day1, ',
'	greatest(day1,day2,day3,day4,day5,day6,day7)*365 year,',
'	case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7)) = trunc(day1) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as day1_color,',
'	case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7)) = trunc(day2) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as day2_color,',
'	case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7)) = trunc(day3) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as day3_color,',
'	case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7)) = trunc(day4) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as day4_color,',
'	case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7)) = trunc(day5) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as day5_color,',
'	case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7)) = trunc(day6) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as day6_color,',
'	case when trunc(greatest(day1,day2,day3,day4,day5,day6,day7)) = trunc(day7) then ''background-color:#CCFFCC;font-weight:bold;'' else ''background-color:#FFFFFF'' END as day7_color',
'from',
'(',
'    select ',
'        tenant_name,',
'        sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-7) then COST_MY_COST else 0 end) DAY7,',
'        sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-6) then COST_MY_COST else 0 end) DAY6,',
'        sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-5) then COST_MY_COST else 0 end) DAY5,',
'        sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-4) then COST_MY_COST else 0 end) DAY4,',
'        sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-3) then COST_MY_COST else 0 end) DAY3,',
'        sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-2) then COST_MY_COST else 0 end) DAY2,',
'        sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-1) then COST_MY_COST else 0 end) DAY1,',
'        sum(case when trunc(USAGE_INTERVAL_START) = trunc(sysdate-4) then COST_MY_COST else 0 end)*365 YEAR3 ',
'    from oci_cost_stats',
'    where ',
'        tenant_name like ''%'' and',
'        USAGE_INTERVAL_START > trunc(sysdate-8)',
'    group by tenant_name',
')',
'order by 1'))
,p_plug_source_type=>'NATIVE_IR'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet(
 p_id=>wwv_flow_api.id(14188875057270029)
,p_max_row_count=>'1000000'
,p_show_nulls_as=>'-'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_show_search_bar=>'N'
,p_show_detail_link=>'N'
,p_owner=>'ADIZOHAR'
,p_internal_uid=>14188875057270029
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(14188947516270030)
,p_db_column_name=>'TENANT_NAME'
,p_display_order=>10
,p_column_identifier=>'A'
,p_column_label=>'Tenant Name'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(14189055837270031)
,p_db_column_name=>'DAY7'
,p_display_order=>20
,p_column_identifier=>'B'
,p_column_label=>'&P6_DAY7.'
,p_column_html_expression=>'<span style="#DAY7_COLOR#">#DAY7#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(14189164915270032)
,p_db_column_name=>'DAY6'
,p_display_order=>30
,p_column_identifier=>'C'
,p_column_label=>'&P6_DAY6.'
,p_column_html_expression=>'<span  style="#DAY6_COLOR#">#DAY6#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(14189202068270033)
,p_db_column_name=>'DAY5'
,p_display_order=>40
,p_column_identifier=>'D'
,p_column_label=>'&P6_DAY5.'
,p_column_html_expression=>'<span  style="#DAY5_COLOR#">#DAY5#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(14189318043270034)
,p_db_column_name=>'DAY4'
,p_display_order=>50
,p_column_identifier=>'E'
,p_column_label=>'&P6_DAY4.'
,p_column_html_expression=>'<span style="#DAY4_COLOR#">#DAY4#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(14189429637270035)
,p_db_column_name=>'DAY3'
,p_display_order=>60
,p_column_identifier=>'F'
,p_column_label=>'&P6_DAY3.'
,p_column_html_expression=>'<span  style="#DAY3_COLOR#">#DAY3#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(14189561008270036)
,p_db_column_name=>'DAY2'
,p_display_order=>70
,p_column_identifier=>'G'
,p_column_label=>'&P6_DAY2.'
,p_column_html_expression=>'<span style="#DAY2_COLOR#">#DAY2#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(14189618941270037)
,p_db_column_name=>'DAY1'
,p_display_order=>80
,p_column_identifier=>'H'
,p_column_label=>'&P6_DAY1.'
,p_column_html_expression=>'<span style="#DAY1_COLOR#">#DAY1#</span>'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16672415759602103)
,p_db_column_name=>'YEAR'
,p_display_order=>90
,p_column_identifier=>'J'
,p_column_label=>'Year Estimation'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990'
,p_static_id=>'rep_col_grey'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16361027290490335)
,p_db_column_name=>'DAY1_COLOR'
,p_display_order=>100
,p_column_identifier=>'K'
,p_column_label=>'Day1 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16361147368490336)
,p_db_column_name=>'DAY2_COLOR'
,p_display_order=>110
,p_column_identifier=>'L'
,p_column_label=>'Day2 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16361232740490337)
,p_db_column_name=>'DAY3_COLOR'
,p_display_order=>120
,p_column_identifier=>'M'
,p_column_label=>'Day3 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16361395035490338)
,p_db_column_name=>'DAY4_COLOR'
,p_display_order=>130
,p_column_identifier=>'N'
,p_column_label=>'Day4 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16361499830490339)
,p_db_column_name=>'DAY5_COLOR'
,p_display_order=>140
,p_column_identifier=>'O'
,p_column_label=>'Day5 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16361540378490340)
,p_db_column_name=>'DAY6_COLOR'
,p_display_order=>150
,p_column_identifier=>'P'
,p_column_label=>'Day6 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16361639231490341)
,p_db_column_name=>'DAY7_COLOR'
,p_display_order=>160
,p_column_identifier=>'Q'
,p_column_label=>'Day7 Color'
,p_column_type=>'STRING'
,p_display_text_as=>'HIDDEN'
);
wwv_flow_api.create_worksheet_rpt(
 p_id=>wwv_flow_api.id(16669557578557119)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'166696'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'TENANT_NAME:DAY7:DAY6:DAY5:DAY4:DAY3:DAY2:DAY1:YEAR::DAY1_COLOR:DAY2_COLOR:DAY3_COLOR:DAY4_COLOR:DAY5_COLOR:DAY6_COLOR:DAY7_COLOR'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(16674406142602123)
,p_plug_name=>'Storage Statistics'
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>60
,p_plug_grid_column_span=>3
,p_plug_display_point=>'BODY'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select',
'    ''Cost Tables and Indexes'' area,',
'    to_char(sum(bytes/1024/1024/1024),''999,999.99'') GB',
'from',
'    user_segments',
'where segment_name like ''%OCI_COST%''',
'union all',
'select',
'    ''Usage Tables and Indexes'' object_name,',
'    to_char(sum(bytes/1024/1024/1024),''999,999.99'') GB',
'from',
'    user_segments',
'where segment_name like ''%OCI_USAGE%''',
'union all',
'select',
'    ''Other Objects'' object_name,',
'    to_char(sum(bytes/1024/1024/1024),''999,999.99'') GB',
'from',
'    user_segments',
'where segment_name not like ''BIN%'' and segment_name not like ''%OCI_USAGE%'' and segment_name not like ''%OCI_COST%''',
'union all',
'select',
'    ''Total All Objects'' object_name,',
'    to_char(sum(bytes/1024/1024/1024),''999,999.99'') GB',
'from',
'    user_segments',
'where segment_name not like ''BIN%''',
''))
,p_plug_source_type=>'NATIVE_IR'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
);
end;
/
begin
wwv_flow_api.create_worksheet(
 p_id=>wwv_flow_api.id(16674695736602125)
,p_max_row_count=>'1000000'
,p_show_nulls_as=>'-'
,p_show_search_bar=>'N'
,p_show_detail_link=>'N'
,p_owner=>'ADIZOHAR'
,p_internal_uid=>16674695736602125
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16675890928602137)
,p_db_column_name=>'AREA'
,p_display_order=>10
,p_column_identifier=>'A'
,p_column_label=>'Area'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16675916346602138)
,p_db_column_name=>'GB'
,p_display_order=>20
,p_column_identifier=>'B'
,p_column_label=>'GB'
,p_column_type=>'STRING'
,p_column_alignment=>'RIGHT'
);
wwv_flow_api.create_worksheet_rpt(
 p_id=>wwv_flow_api.id(22814282525347815)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'228143'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'AREA:GB'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11208116210636617)
,p_name=>'P6_MONTH1'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(11208064619636616)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11208271476636618)
,p_name=>'P6_MONTH2'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_api.id(11208064619636616)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11208351769636619)
,p_name=>'P6_MONTH3'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_api.id(11208064619636616)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11208489651636620)
,p_name=>'P6_MONTH4'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_api.id(11208064619636616)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11208533441636621)
,p_name=>'P6_MONTH5'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_api.id(11208064619636616)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(11208672205636622)
,p_name=>'P6_MONTH6'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_api.id(11208064619636616)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12555202081313350)
,p_name=>'P6_USAGE_SIZE'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(12552815670313326)
,p_use_cache_before_default=>'NO'
,p_source=>'select to_char(sum(bytes/1024/1024/1024),''999,990.9'') ||'' GB'' GB from user_segments where segment_name=''OCI_USAGE'''
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(13350578837239102)
,p_name=>'P6_COST_SIZE'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(12630713145041599)
,p_use_cache_before_default=>'NO'
,p_source=>'select to_char(sum(bytes/1024/1024/1024),''999,990.9'') ||'' GB'' GB from user_segments where segment_name=''OCI_COST'''
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(14189745953270038)
,p_name=>'P6_DAY1'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(14188632778270027)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(14189972710270040)
,p_name=>'P6_DAY2'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_api.id(14188632778270027)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(14190110518270042)
,p_name=>'P6_DAY3'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_api.id(14188632778270027)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(14190215017270043)
,p_name=>'P6_DAY4'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_api.id(14188632778270027)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(14190314422270044)
,p_name=>'P6_DAY5'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_api.id(14188632778270027)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(14190487872270045)
,p_name=>'P6_DAY6'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_api.id(14188632778270027)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(14190567586270046)
,p_name=>'P6_DAY7'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_api.id(14188632778270027)
,p_display_as=>'NATIVE_HIDDEN'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(14189861715270039)
,p_computation_sequence=>10
,p_computation_item=>'P6_DAY1'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(trunc(sysdate-1),''DD-MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(14190030026270041)
,p_computation_sequence=>20
,p_computation_item=>'P6_DAY2'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(trunc(sysdate-2),''DD-MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(14190665626270047)
,p_computation_sequence=>30
,p_computation_item=>'P6_DAY3'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(trunc(sysdate-3),''DD-MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(14190773992270048)
,p_computation_sequence=>40
,p_computation_item=>'P6_DAY4'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(trunc(sysdate-4),''DD-MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(14190860366270049)
,p_computation_sequence=>50
,p_computation_item=>'P6_DAY5'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(trunc(sysdate-5),''DD-MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(14190996091270050)
,p_computation_sequence=>60
,p_computation_item=>'P6_DAY6'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(trunc(sysdate-6),''DD-MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(16672287011602101)
,p_computation_sequence=>70
,p_computation_item=>'P6_DAY7'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(trunc(sysdate-7),''DD-MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(11210536697636641)
,p_computation_sequence=>80
,p_computation_item=>'P6_MONTH1'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(add_months(trunc(sysdate,''MM''),0),''MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(11210694543636642)
,p_computation_sequence=>90
,p_computation_item=>'P6_MONTH2'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(add_months(trunc(sysdate,''MM''),-1),''MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(11210745364636643)
,p_computation_sequence=>100
,p_computation_item=>'P6_MONTH3'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(add_months(trunc(sysdate,''MM''),-2),''MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(11210851820636644)
,p_computation_sequence=>110
,p_computation_item=>'P6_MONTH4'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(add_months(trunc(sysdate,''MM''),-3),''MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(11210940658636645)
,p_computation_sequence=>120
,p_computation_item=>'P6_MONTH5'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(add_months(trunc(sysdate,''MM''),-4),''MON-YYYY'') val from dual'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(11211038784636646)
,p_computation_sequence=>130
,p_computation_item=>'P6_MONTH6'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select to_char(add_months(trunc(sysdate,''MM''),-5),''MON-YYYY'') val from dual'
);
end;
/
prompt --application/pages/page_00007
begin
wwv_flow_api.create_page(
 p_id=>7
,p_user_interface_id=>wwv_flow_api.id(9843694399688199)
,p_name=>'Rate Card'
,p_step_title=>'Rate Card'
,p_warn_on_unsaved_changes=>'N'
,p_autocomplete_on_off=>'OFF'
,p_inline_css=>wwv_flow_string.join(wwv_flow_t_varchar2(
'.a-IRR-table tr td[headers*="rep_col_grey"]',
'{',
'    background-color: #efffff;',
'}',
'.a-IRR-table tr td[headers*="rep_col_blue"]',
'{',
'    background-color: #ffefff;',
'}',
'',
''))
,p_page_template_options=>'#DEFAULT#'
,p_last_updated_by=>'ADIZOHAR'
,p_last_upd_yyyymmddhh24miss=>'20210329140201'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(72369311697812384)
,p_plug_name=>'Filter'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--accent12:t-Region--scrollBody:t-Form--noPadding:margin-top-none:margin-bottom-md:margin-left-none:margin-right-none'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_grid_column_span=>12
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(83161602120160340)
,p_plug_name=>'ShowGraphs'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>40
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_attribute_01=>'N'
,p_attribute_02=>'HTML'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(61791178689852192)
,p_plug_name=>'Rate Card Report'
,p_parent_plug_id=>wwv_flow_api.id(83161602120160340)
,p_region_template_options=>'#DEFAULT#:t-Region--accent15:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>60
,p_plug_display_point=>'BODY'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'SELECT',
'	TENANT_NAME               TENANT,',
'    TENANT_ID                 TENANT_ID,',
'    COST_PRODUCT_SKU          SKU,',
'    replace(PRD_DESCRIPTION,COST_PRODUCT_SKU||'' - '','''')  PRODUCT,',
'    COST_CURRENCY_CODE        CURRENCY,',
'    COST_UNIT_PRICE           COST_PRICE,',
'    COST_LAST_UPDATE,',
'	RATE_DESCRIPTION,',
'    ROUND(RATE_MONTHLY_FLEX_PRICE,4) RATE_MONTHLY,',
'	CASE WHEN RATE_MONTHLY_FLEX_PRICE > 0  AND RATE_MONTHLY_FLEX_PRICE IS NOT NULL and COST_UNIT_PRICE>0 THEN',
'	    ROUND((RATE_MONTHLY_FLEX_PRICE - COST_UNIT_PRICE )/RATE_MONTHLY_FLEX_PRICE * 100,1)',
'	ELSE NULL END PCT_MONTH,',
'	RATE_UPDATE_DATE',
'FROM',
'    OCI_PRICE_LIST',
'where tenant_name=:P7_TENANT_NAME and tenant_id=:P7_TENANT_ID',
'order by cost_product_sku;'))
,p_plug_source_type=>'NATIVE_IR'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_document_header=>'APEX'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width=>8.5
,p_prn_height=>11
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#9bafde'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'normal'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#efefef'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet(
 p_id=>wwv_flow_api.id(16358400984490309)
,p_max_row_count=>'1000000'
,p_allow_save_rpt_public=>'Y'
,p_show_nulls_as=>'-'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_show_display_row_count=>'Y'
,p_report_list_mode=>'TABS'
,p_show_detail_link=>'N'
,p_show_rows_per_page=>'N'
,p_show_notify=>'Y'
,p_download_formats=>'CSV:HTML:EMAIL:XLSX:PDF:RTF'
,p_owner=>'ADIZOHAR'
,p_internal_uid=>16358400984490309
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16358519224490310)
,p_db_column_name=>'TENANT'
,p_display_order=>10
,p_column_identifier=>'A'
,p_column_label=>'Tenant'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16358680829490311)
,p_db_column_name=>'SKU'
,p_display_order=>20
,p_column_identifier=>'B'
,p_column_label=>'Sku'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16358753197490312)
,p_db_column_name=>'PRODUCT'
,p_display_order=>30
,p_column_identifier=>'C'
,p_column_label=>'Product'
,p_column_html_expression=>'<span style="white-space:nowrap;">#PRODUCT#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16358884845490313)
,p_db_column_name=>'CURRENCY'
,p_display_order=>40
,p_column_identifier=>'D'
,p_column_label=>'Currency'
,p_column_type=>'STRING'
,p_column_alignment=>'CENTER'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16358959661490314)
,p_db_column_name=>'COST_PRICE'
,p_display_order=>50
,p_column_identifier=>'E'
,p_column_label=>'Cost Price'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D0000'
,p_static_id=>'rep_col_grey'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16359088388490315)
,p_db_column_name=>'COST_LAST_UPDATE'
,p_display_order=>60
,p_column_identifier=>'F'
,p_column_label=>'Cost Last Update'
,p_column_html_expression=>'<span style="white-space:nowrap;">#COST_LAST_UPDATE#</span>'
,p_column_type=>'DATE'
,p_column_alignment=>'CENTER'
,p_format_mask=>'DD-MON-YYYY HH24:MI'
,p_tz_dependent=>'N'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16359157348490316)
,p_db_column_name=>'RATE_DESCRIPTION'
,p_display_order=>70
,p_column_identifier=>'G'
,p_column_label=>'Rate Full Description'
,p_column_html_expression=>'<span style="white-space:nowrap;">#RATE_DESCRIPTION#</span>'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16359449849490319)
,p_db_column_name=>'RATE_MONTHLY'
,p_display_order=>100
,p_column_identifier=>'J'
,p_column_label=>'Public Rate'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D0000'
,p_static_id=>'rep_col_grey'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16359539927490320)
,p_db_column_name=>'PCT_MONTH'
,p_display_order=>110
,p_column_identifier=>'K'
,p_column_label=>'% Discount'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'999G999G999G999G990D00'
,p_static_id=>'rep_col_blue'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(16359640418490321)
,p_db_column_name=>'RATE_UPDATE_DATE'
,p_display_order=>120
,p_column_identifier=>'L'
,p_column_label=>'Rate Update Date'
,p_column_html_expression=>'<span style="white-space:nowrap;">#RATE_UPDATE_DATE#</span>'
,p_column_type=>'DATE'
,p_column_alignment=>'CENTER'
,p_format_mask=>'DD-MON-YYYY HH24:MI'
,p_tz_dependent=>'N'
);
wwv_flow_api.create_worksheet_column(
 p_id=>wwv_flow_api.id(12306435263574236)
,p_db_column_name=>'TENANT_ID'
,p_display_order=>130
,p_column_identifier=>'M'
,p_column_label=>'Tenant Id'
,p_column_type=>'STRING'
);
wwv_flow_api.create_worksheet_rpt(
 p_id=>wwv_flow_api.id(16392788699988040)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'163928'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'SKU:PRODUCT:CURRENCY:RATE_MONTHLY:PCT_MONTH:COST_PRICE:RATE_DESCRIPTION:RATE_UPDATE_DATE:'
);
wwv_flow_api.create_page_button(
 p_id=>wwv_flow_api.id(23803495716503351)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_api.id(72369311697812384)
,p_button_name=>'P7_SUBMIT'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#:t-Button--large:t-Button--stretch:t-Button--gapTop'
,p_button_template_id=>wwv_flow_api.id(9821119233688096)
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Submit'
,p_button_position=>'BODY'
,p_grid_new_row=>'N'
,p_grid_new_column=>'Y'
,p_grid_column_span=>2
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(12306254467574234)
,p_name=>'P7_TENANT_ID'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_api.id(72369311697812384)
,p_prompt=>'Tenant Id'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'select distinct tenant_id o, tenant_id r from  OCI_PRICE_LIST where tenant_name = :P7_TENANT_NAME  order by 1'
,p_lov_cascade_parent_items=>'P7_TENANT_NAME'
,p_ajax_optimize_refresh=>'Y'
,p_cHeight=>1
,p_begin_on_new_line=>'N'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_warn_on_unsaved_changes=>'I'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(16372411599522248)
,p_name=>'P7_TENANT_NAME'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(72369311697812384)
,p_prompt=>'Tenant Name'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'select distinct tenant_name o, tenant_name r from  OCI_PRICE_LIST order by 1'
,p_lov_display_null=>'YES'
,p_lov_null_text=>'Please Choose...'
,p_cHeight=>1
,p_tag_attributes=>'style="background-color:#e0f0f0"'
,p_colspan=>2
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_warn_on_unsaved_changes=>'I'
,p_lov_display_extra=>'NO'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(16378387657522263)
,p_computation_sequence=>10
,p_computation_item=>'P7_TENANT_NAME'
,p_computation_point=>'AFTER_HEADER'
,p_computation_type=>'QUERY'
,p_computation=>'select tenant_name from oci_cost where rownum=1'
,p_compute_when=>'P7_TENANT_NAME'
,p_compute_when_type=>'ITEM_IS_NULL'
);
wwv_flow_api.create_page_computation(
 p_id=>wwv_flow_api.id(12306310413574235)
,p_computation_sequence=>10
,p_computation_item=>'P7_TENANT_ID'
,p_computation_point=>'BEFORE_BOX_BODY'
,p_computation_type=>'QUERY'
,p_computation=>'select min(tenant_id) from  OCI_PRICE_LIST where tenant_name = :P7_TENANT_NAME  '
,p_compute_when=>'P7_TENANT_ID'
,p_compute_when_type=>'ITEM_IS_NULL'
);
end;
/
prompt --application/pages/page_00008
begin
wwv_flow_api.create_page(
 p_id=>8
,p_user_interface_id=>wwv_flow_api.id(9843694399688199)
,p_name=>'FormNW'
,p_alias=>'FORMNW'
,p_step_title=>'FormNW'
,p_autocomplete_on_off=>'OFF'
,p_javascript_code=>'var htmldb_delete_message=''"DELETE_CONFIRM_MSG"'';'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_last_updated_by=>'ADIZOHAR'
,p_last_upd_yyyymmddhh24miss=>'20201113141739'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(23720678853456669)
,p_plug_name=>'FormNW'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>wwv_flow_api.id(9765042323688020)
,p_plug_display_sequence=>10
,p_plug_display_point=>'BODY'
,p_query_type=>'TABLE'
,p_query_table=>'ADI_COST'
,p_include_rowid_column=>false
,p_is_editable=>true
,p_edit_operations=>'i:u:d'
,p_lost_update_check_type=>'VALUES'
,p_plug_source_type=>'NATIVE_FORM'
);
wwv_flow_api.create_page_button(
 p_id=>wwv_flow_api.id(23727005473456739)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_api.id(23720678853456669)
,p_button_name=>'SAVE'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>wwv_flow_api.id(9821119233688096)
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Apply Changes'
,p_button_position=>'REGION_TEMPLATE_CHANGE'
,p_button_condition=>'P8_ID'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_database_action=>'UPDATE'
);
wwv_flow_api.create_page_button(
 p_id=>wwv_flow_api.id(23725807138456731)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_api.id(23720678853456669)
,p_button_name=>'CANCEL'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>wwv_flow_api.id(9821119233688096)
,p_button_image_alt=>'Cancel'
,p_button_position=>'REGION_TEMPLATE_CLOSE'
,p_button_redirect_url=>'f?p=&APP_ID.:1:&SESSION.::&DEBUG.:::'
);
wwv_flow_api.create_page_button(
 p_id=>wwv_flow_api.id(23727462949456739)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_api.id(23720678853456669)
,p_button_name=>'CREATE'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>wwv_flow_api.id(9821119233688096)
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Create'
,p_button_position=>'REGION_TEMPLATE_CREATE'
,p_button_condition=>'P8_ID'
,p_button_condition_type=>'ITEM_IS_NULL'
,p_database_action=>'INSERT'
);
wwv_flow_api.create_page_button(
 p_id=>wwv_flow_api.id(23726651722456738)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_api.id(23720678853456669)
,p_button_name=>'DELETE'
,p_button_action=>'REDIRECT_URL'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>wwv_flow_api.id(9821119233688096)
,p_button_image_alt=>'Delete'
,p_button_position=>'REGION_TEMPLATE_DELETE'
,p_button_redirect_url=>'javascript:apex.confirm(htmldb_delete_message,''DELETE'');'
,p_button_execute_validations=>'N'
,p_button_condition=>'P8_ID'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_database_action=>'DELETE'
);
wwv_flow_api.create_page_branch(
 p_id=>wwv_flow_api.id(23727701505456739)
,p_branch_action=>'f?p=&APP_ID.:2:&SESSION.::&DEBUG.&success_msg=#SUCCESS_MSG#'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'REDIRECT_URL'
,p_branch_sequence=>1
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(23720995918456680)
,p_name=>'P8_ID'
,p_source_data_type=>'NUMBER'
,p_is_primary_key=>true
,p_is_query_only=>true
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(23720678853456669)
,p_item_source_plug_id=>wwv_flow_api.id(23720678853456669)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Id'
,p_source=>'ID'
,p_source_type=>'REGION_SOURCE_COLUMN'
,p_display_as=>'NATIVE_HIDDEN'
,p_label_alignment=>'RIGHT'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_is_persistent=>'N'
,p_protection_level=>'S'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(23721311097456712)
,p_name=>'P8_PRD_SERVICE'
,p_source_data_type=>'VARCHAR2'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_api.id(23720678853456669)
,p_item_source_plug_id=>wwv_flow_api.id(23720678853456669)
,p_prompt=>'Prd Service'
,p_source=>'PRD_SERVICE'
,p_source_type=>'REGION_SOURCE_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>'STATIC:Display1;Return1,Display2;Return2'
,p_lov_display_null=>'YES'
,p_cHeight=>1
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_is_persistent=>'N'
,p_lov_display_extra=>'YES'
,p_attribute_01=>'NONE'
,p_attribute_02=>'N'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(23721766788456721)
,p_name=>'P8_PRD_RESOURCE'
,p_source_data_type=>'VARCHAR2'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_api.id(23720678853456669)
,p_item_source_plug_id=>wwv_flow_api.id(23720678853456669)
,p_prompt=>'Prd Resource'
,p_source=>'PRD_RESOURCE'
,p_source_type=>'REGION_SOURCE_COLUMN'
,p_display_as=>'NATIVE_TEXTAREA'
,p_cSize=>60
,p_cMaxlength=>255
,p_cHeight=>4
,p_begin_on_new_line=>'N'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_is_persistent=>'N'
,p_attribute_01=>'Y'
,p_attribute_02=>'N'
,p_attribute_03=>'N'
,p_attribute_04=>'BOTH'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(23722165787456722)
,p_name=>'P8_COST_PRODUCT_SKU'
,p_source_data_type=>'VARCHAR2'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_api.id(23720678853456669)
,p_item_source_plug_id=>wwv_flow_api.id(23720678853456669)
,p_prompt=>'Cost Product Sku'
,p_source=>'COST_PRODUCT_SKU'
,p_source_type=>'REGION_SOURCE_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>32
,p_cMaxlength=>50
,p_begin_on_new_line=>'N'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_is_persistent=>'N'
,p_attribute_01=>'N'
,p_attribute_02=>'N'
,p_attribute_04=>'TEXT'
,p_attribute_05=>'NONE'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(23722538075456723)
,p_name=>'P8_PRD_DESCRIPTION'
,p_source_data_type=>'VARCHAR2'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_api.id(23720678853456669)
,p_item_source_plug_id=>wwv_flow_api.id(23720678853456669)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Prd Description'
,p_source=>'PRD_DESCRIPTION'
,p_source_type=>'REGION_SOURCE_COLUMN'
,p_display_as=>'NATIVE_TEXTAREA'
,p_cSize=>60
,p_cMaxlength=>4000
,p_cHeight=>4
,p_label_alignment=>'RIGHT'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_is_persistent=>'N'
,p_attribute_01=>'Y'
,p_attribute_02=>'N'
,p_attribute_03=>'N'
,p_attribute_04=>'BOTH'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(23722935349456724)
,p_name=>'P8_COST_UNIT_PRICE'
,p_source_data_type=>'NUMBER'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_api.id(23720678853456669)
,p_item_source_plug_id=>wwv_flow_api.id(23720678853456669)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Cost Unit Price'
,p_source=>'COST_UNIT_PRICE'
,p_source_type=>'REGION_SOURCE_COLUMN'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_cSize=>32
,p_cMaxlength=>255
,p_cHeight=>1
,p_label_alignment=>'RIGHT'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_is_persistent=>'N'
,p_attribute_03=>'right'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(23723323523456725)
,p_name=>'P8_COST_BILLING_UNIT'
,p_source_data_type=>'VARCHAR2'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_api.id(23720678853456669)
,p_item_source_plug_id=>wwv_flow_api.id(23720678853456669)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Cost Billing Unit'
,p_source=>'COST_BILLING_UNIT'
,p_source_type=>'REGION_SOURCE_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>32
,p_cMaxlength=>50
,p_label_alignment=>'RIGHT'
,p_field_template=>wwv_flow_api.id(9820028477688087)
,p_item_template_options=>'#DEFAULT#'
,p_is_persistent=>'N'
,p_attribute_01=>'N'
,p_attribute_02=>'N'
,p_attribute_03=>'N'
,p_attribute_04=>'TEXT'
,p_attribute_05=>'NONE'
);
wwv_flow_api.create_page_process(
 p_id=>wwv_flow_api.id(23728692356456745)
,p_process_sequence=>10
,p_process_point=>'AFTER_SUBMIT'
,p_region_id=>wwv_flow_api.id(23720678853456669)
,p_process_type=>'NATIVE_FORM_DML'
,p_process_name=>'Process form FormNW'
,p_attribute_01=>'REGION_SOURCE'
,p_attribute_05=>'Y'
,p_attribute_06=>'Y'
,p_attribute_08=>'Y'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
);
wwv_flow_api.create_page_process(
 p_id=>wwv_flow_api.id(23728218987456743)
,p_process_sequence=>10
,p_process_point=>'BEFORE_HEADER'
,p_region_id=>wwv_flow_api.id(23720678853456669)
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize form FormNW'
);
end;
/
prompt --application/pages/page_09999
begin
wwv_flow_api.create_page(
 p_id=>9999
,p_user_interface_id=>wwv_flow_api.id(9843694399688199)
,p_name=>'Login Page'
,p_alias=>'LOGIN_DESKTOP'
,p_step_title=>'OCI Usage and Cost Report - Sign In'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>wwv_flow_api.id(9721413857687955)
,p_page_template_options=>'#DEFAULT#'
,p_page_is_public_y_n=>'Y'
,p_last_updated_by=>'ADIZOHAR'
,p_last_upd_yyyymmddhh24miss=>'20200506182856'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9849397199688308)
,p_plug_name=>'OCI Usage and Cost Report'
,p_icon_css_classes=>'app-icon'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>wwv_flow_api.id(9764594135688020)
,p_plug_display_sequence=>10
,p_plug_display_point=>'BODY'
,p_plug_query_options=>'DERIVED_REPORT_COLUMNS'
,p_attribute_01=>'N'
,p_attribute_02=>'TEXT'
,p_attribute_03=>'Y'
);
wwv_flow_api.create_page_plug(
 p_id=>wwv_flow_api.id(9854066498688358)
,p_plug_name=>'Language Selector'
,p_parent_plug_id=>wwv_flow_api.id(9849397199688308)
,p_region_template_options=>'#DEFAULT#'
,p_component_template_options=>'#DEFAULT#'
,p_escape_on_http_output=>'Y'
,p_plug_template=>wwv_flow_api.id(9739874064687990)
,p_plug_display_sequence=>20
,p_plug_display_point=>'BODY'
,p_plug_source=>'apex_lang.emit_language_selector_list;'
,p_plug_source_type=>'NATIVE_PLSQL'
,p_plug_query_num_rows=>15
);
wwv_flow_api.create_page_button(
 p_id=>wwv_flow_api.id(9852132109688343)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_api.id(9849397199688308)
,p_button_name=>'LOGIN'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>wwv_flow_api.id(9821119233688096)
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Sign In'
,p_button_position=>'REGION_TEMPLATE_NEXT'
,p_button_alignment=>'LEFT'
,p_grid_new_row=>'Y'
,p_grid_new_column=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9849768555688324)
,p_name=>'P9999_USERNAME'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_api.id(9849397199688308)
,p_prompt=>'username'
,p_placeholder=>'username'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>40
,p_cMaxlength=>100
,p_label_alignment=>'RIGHT'
,p_field_template=>wwv_flow_api.id(9819754494688084)
,p_item_icon_css_classes=>'fa-user'
,p_item_template_options=>'#DEFAULT#'
,p_is_persistent=>'N'
,p_attribute_01=>'N'
,p_attribute_02=>'N'
,p_attribute_03=>'N'
,p_attribute_04=>'TEXT'
,p_attribute_05=>'NONE'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9850117375688329)
,p_name=>'P9999_PASSWORD'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_api.id(9849397199688308)
,p_prompt=>'password'
,p_placeholder=>'password'
,p_display_as=>'NATIVE_PASSWORD'
,p_cSize=>40
,p_cMaxlength=>100
,p_label_alignment=>'RIGHT'
,p_field_template=>wwv_flow_api.id(9819754494688084)
,p_item_icon_css_classes=>'fa-key'
,p_item_template_options=>'#DEFAULT#'
,p_is_persistent=>'N'
,p_attribute_01=>'Y'
);
wwv_flow_api.create_page_item(
 p_id=>wwv_flow_api.id(9851205065688338)
,p_name=>'P9999_REMEMBER'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_api.id(9849397199688308)
,p_prompt=>'Remember username'
,p_display_as=>'NATIVE_CHECKBOX'
,p_named_lov=>'LOGIN_REMEMBER_USERNAME'
,p_lov=>'.'||wwv_flow_api.id(9850484666688331)||'.'
,p_label_alignment=>'RIGHT'
,p_field_template=>wwv_flow_api.id(9819754494688084)
,p_item_template_options=>'#DEFAULT#'
,p_is_persistent=>'N'
,p_lov_display_extra=>'NO'
,p_help_text=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>',
'If you select this checkbox, the application will save your username in a persistent browser cookie named "LOGIN_USERNAME_COOKIE".',
'When you go to the login page the next time,',
'the username field will be automatically populated with this value.',
'</p>',
'<p>',
'If you deselect this checkbox and your username is already saved in the cookie,',
'the application will overwrite it with an empty value.',
'You can also use your browser''s developer tools to completely remove the cookie.',
'</p>'))
,p_attribute_01=>'1'
);
wwv_flow_api.create_page_process(
 p_id=>wwv_flow_api.id(9852900871688355)
,p_process_sequence=>10
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Set Username Cookie'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'apex_authentication.send_login_username_cookie (',
'    p_username => lower(:P9999_USERNAME),',
'    p_consent  => :P9999_REMEMBER = ''Y'' );'))
,p_process_clob_language=>'PLSQL'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
);
wwv_flow_api.create_page_process(
 p_id=>wwv_flow_api.id(9852563696688350)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Login'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'apex_authentication.login(',
'    p_username => :P9999_USERNAME,',
'    p_password => :P9999_PASSWORD );'))
,p_process_clob_language=>'PLSQL'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
);
wwv_flow_api.create_page_process(
 p_id=>wwv_flow_api.id(9853734327688356)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'Clear Page(s) Cache'
,p_attribute_01=>'CLEAR_CACHE_CURRENT_PAGE'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
);
wwv_flow_api.create_page_process(
 p_id=>wwv_flow_api.id(9853301172688356)
,p_process_sequence=>10
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Get Username Cookie'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
':P9999_USERNAME := apex_authentication.get_login_username_cookie;',
':P9999_REMEMBER := case when :P9999_USERNAME is not null then ''Y'' end;'))
,p_process_clob_language=>'PLSQL'
);
end;
/
prompt --application/end_environment
begin
wwv_flow_api.import_end(p_auto_install_sup_obj => nvl(wwv_flow_application_install.get_auto_install_sup_obj, false));
commit;
end;
/
set verify on feedback on define on
prompt  ...done
