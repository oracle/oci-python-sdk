# 1. Create approved sender
```
OCI -> Menu -> Solutions and Platform -> Email Delivery -> Email Approved Sender
--> Create approved sender
--> email address to be used, your domain must allow to send e-mail from it, if not use report@oracleemaildelivery.com, 
```

![](img/report_01.png)

![](img/report_02.png)

# 2. Create user smtp password
```
OCI -> Menu -> Identity -> Users

Find the user that will send e-mail
Bottom left -> SMTP Credentials 

Generate SMTP Credentials
--> Description = cost_usage_email_credentials
--> Copy the username and password to notepad, they won't appear again
```


![](img/report_03.png)

![](img/report_04.png)

# 3. Find connection end point for current region

Find your SMTP endpoint from the documentation - 

https://docs.cloud.oracle.com/en-us/iaas/Content/Email/Tasks/configuresmtpconnection.htm

Example For Ashburn - smtp.us-ashburn-1.oraclecloud.com

# 4. Integrating Oracle Application Express with Email Delivery

Based on the documentation - https://docs.oracle.com/en-us/iaas/Content/Email/Reference/apex.htm

```
Login to the unix machine

connect to the ADW Database using sqlplus
> sqlplus admin@usage2adw_low

Execute:

BEGIN
	APEX_INSTANCE_ADMIN.SET_PARAMETER('SMTP_HOST_ADDRESS', 'smtp.region.oraclecloud.com');
	APEX_INSTANCE_ADMIN.SET_PARAMETER('SMTP_USERNAME', 'ocid1.user.oc1.username');
	APEX_INSTANCE_ADMIN.SET_PARAMETER('SMTP_PASSWORD', 'paste your password');
	COMMIT;
END;
/	

# Test
BEGIN
	APEX_MAIL.SEND(p_from => 'oci_user@domain.com',
		       p_to   => 'john@example.com',
		       p_subj => 'Email from Oracle Autonomous Database',
	               p_body => 'Sent using APEX_MAIL');
END;
/

```

## 5. Configure APEX application to use the approved sender

### 5.1. Open Autonomous Database APEX Workspace

```
    OCI Console -> Autonomous Databases -> ADWCUSG -> Service Console
    Development Menu -> Oracle APEX
    Choose Workspace Login.

    Workspace = Usage
    User = Usage
    Password = Password you defined for the application


```
![](img/Image_16.png)

### 5.2. Choose the OCI Usage and Cost Report application

![](img/Image_33.png)

### 5.3. Press on Edit Application Definition - Top Right

![](img/Image_34.png)

### 5.4. Update "Application Email From Address" with approved sender

![](img/Image_35.png)

## 6. Send report via download to e-mail or Subscription

![](img/Image_36.png)

```
    Please bear in mind:
    1. OCI e-mail delivery is limited to 2mb
    2. If Subscribed to report, please use future date filter 

```