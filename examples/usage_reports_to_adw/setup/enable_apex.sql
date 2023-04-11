
---------------------------------------------------
-- APEX Create user and import app
---------------------------------------------------

begin
    apex_util.set_workspace(p_workspace => 'USAGE');
    apex_util.create_user(
        p_user_name                    => 'USAGE',
        p_web_password                 => '&pass.',
        p_developer_privs              => 'ADMIN:CREATE:DATA_LOADER:EDIT:HELP:MONITOR:SQL',
        p_email_address                => 'usage@example.com',
        p_default_schema               => 'USAGE',
        p_change_password_on_first_use => 'N' );
end;
/
prompt Remove Application 100
begin
    apex_util.set_workspace(p_workspace => 'USAGE');
    wwv_flow_api.remove_flow(100);
end;
/

prompt Install Application 100
declare
    c_workspace constant apex_workspaces.workspace%type := 'USAGE';
    c_app_id constant apex_applications.application_id%type := 100;
    c_app_alias constant apex_applications.alias%type := 'USAGE2ADW';

    l_workspace_id apex_workspaces.workspace_id%type;
begin
    apex_application_install.clear_all;

    select workspace_id into l_workspace_id from apex_workspaces where workspace = 'USAGE';

    apex_application_install.set_workspace_id(l_workspace_id);
    apex_application_install.set_application_id(c_app_id);
    apex_application_install.set_application_alias(c_app_alias);
    apex_application_install.generate_offset;
end;
/

-----------------------------
-- setup the application
-----------------------------
@/home/opc/usage_reports_to_adw/apex_demo_app/usage.demo.apex.sql


