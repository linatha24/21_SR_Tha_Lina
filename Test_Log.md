# Test Log (Assignment Step 7)

Run `poetry run python -m app.main` and ask at least 5 questions: at least 3
that your documents can answer, and at least 1 that they cannot. For each
one, fill in a section below using the retrieved chunks and answer printed
by the app (or run `poetry run python -m scripts.test_queries` to get the
distances too).

## Question 1
**Q:** <How do I reset my forgotten PIN?>

**Retrieved chunks:**
  - [002_Resetting_a_Forgotten_PIN.txt #0] dist=0.3477  "**Resetting a Forgotten PIN**  If you have forgotten your PIN, you can reset it ..."
  - [002_Resetting_a_Forgotten_PIN.txt #1] dist=0.4339  " in the required field. 2. Click the "Next" button to proceed.  **Step 4: Reset ..."
  - [002_Resetting_a_Forgotten_PIN.txt #2] dist=0.4458  "Helpdesk for assistance. * It is recommended to keep your PIN confidential and n..."
  - [004_Troubleshooting_Issues_with_Microsoft_Office.txt #3] dist=0.9345  "nel**, select **Programs and Features**, and uninstall Microsoft Office. Then, r..."

**Answer:**
> <To reset your forgotten PIN, follow these steps:

1. **Access the PIN Reset Tool**:  
   - Go to the company's intranet homepage.  
   - Click "IT Support" at the top right, then select "Self-Service" and "PIN Reset" from the drop-down menu.  
   *(Source: 002_Resetting_a_Forgotten_PIN.txt)*  

2. **Authenticate with Your Credentials**:  
   - Enter your company username and password.  
   - Click "Login" to authenticate.  
   *(Source: 002_Resetting_a_Forgotten_PIN.txt)*  

3. **Verify Your Identity**:  
   - Answer your security question.  
   - Click "Next" to proceed.  
   *(Source: 002_Resetting_a_Forgotten_PIN.txt)*  

4. **Reset Your PIN**:  
   - Enter a new PIN (minimum 8 characters, with a mix of uppercase letters, lowercase letters, numbers, and special characters).  
   - Re-enter the new PIN in the confirmation field.  
   - Click "Reset PIN" to complete the process.  
   *(Source: 002_Resetting_a_Forgotten_PIN.txt)*  

5. **Confirm PIN Reset**:  
   - Click "OK" after receiving a confirmation message that your PIN has been reset.  
   *(Source: 002_Resetting_a_Forgotten_PIN.txt)*  


**Important Notes**:  
- If you exceed 3 PIN reset attempts in 24 hours, contact the IT Helpdesk.  
- Keep your PIN confidential and avoid sharing it.  
- If self-service fails, contact the IT Helpdesk for assistance.  
*(Source: 002_Resetting_a_Forgotten_PIN.txt)*

---

## Question 2
**Q:**  What do I need before I can configure VPN access for remote work?

**Retrieved chunks:**
  - [003_Configuring_VPN_Access_for_Remote_Workers.txt #0] dist=0.3018  "**Configuring VPN Access for Remote Workers**  **Overview**  This article provid..."
  - [003_Configuring_VPN_Access_for_Remote_Workers.txt #3] dist=0.5416  "has changed to a company-assigned IP address. * If you continue to experience is..."
  - [003_Configuring_VPN_Access_for_Remote_Workers.txt #1] dist=0.5686  "Run the installer and follow the prompts to install the software. 3. Once instal..."
  - [003_Configuring_VPN_Access_for_Remote_Workers.txt #2] dist=0.6466  "nce connected, you will see a confirmation message indicating that you are conne..."

**Answer:**
>
A: To configure VPN access for remote work, you will need the following before starting the setup process:  
1. A device (laptop or desktop) that meets the company's minimum system requirements for VPN connectivity.  
2. Valid company login credentials.  
3. A stable internet connection.  
**Source:** 003_Configuring_VPN_Access_for_Remote_Workers.txt

**Notes:** 

---

## Question 3
**Q:** How do I set up my mobile device for company email?

**Retrieved chunks:**
  - [001_Setting_Up_a_Mobile_Device_for_Company_Email.txt #0] dist=0.1914  "**Setting Up a Mobile Device for Company Email**  **Prerequisites:**  * Mobile d..."
  - [001_Setting_Up_a_Mobile_Device_for_Company_Email.txt #1] dist=0.4066  "evice**  1. Go to the Settings app on your mobile device. 2. Select "Mail" or "E..."
  - [001_Setting_Up_a_Mobile_Device_for_Company_Email.txt #3] dist=0.4529  "ation, try restarting your device or checking the email account settings.  **Add..."
  - [001_Setting_Up_a_Mobile_Device_for_Company_Email.txt #2] dist=0.5439  "ethod to "Username and Password" or "Domain\Username". 4. If prompted, enter you..."

**Answer:**
>To set up your mobile device for company email, follow these steps based on the provided documentation:

1. **Check for MDM Profile**: If your company requires a Mobile Device Management (MDM) profile, ensure it is installed on your device. Contact your IT department if unsure.  
   *Source: 001_Setting_Up_a_Mobile_Device_for_Company_Email.txt*

2. **Add Company Email Account**:  
   - Go to your device's **Settings** app.  
   - Select **Mail** or **Email** (depending on your OS).  
   - Tap **Add Account** or **Create a new account**.  
   - Choose **Exchange** or **Corporate** as the account type.  
   - Enter your company email address, password, and the email server address (e.g., `mail.company.com` if prompted).  
   - Select synchronization options (e.g., email, contacts, calendar).  
   *Source: 001_Setting_Up_a_Mobile_Device_for_Company_Email.txt*

3. **Configure Security Settings**:  
   - In the email account settings, enable **SSL/TLS** or a secure connection.  
   - Set the authentication method to **Username and Password** or **Domain\Username**.  
   - Enter your company’s email domain (e.g., `company.com`) if prompted.  
   *Source: 001_Setting_Up_a_Mobile_Device_for_Company_Email.txt*

4. **Verify Setup**:  
   - Wait for the account to synchronize with the company server.  
   - Send a test email to confirm it is working.  
   *Source: 001_Setting_Up_a_Mobile_Device_for_Company_Email.txt*

5. **Troubleshooting**:  
   - Ensure your device has a stable internet connection and correct credentials.  
   - Restart your device or check account settings if synchronization fails.  
   - Contact your IT department for further assistance.  
   *Source: 001_Setting_Up_a_Mobile_Device_for_Company_Email.txt* 

**Notes:** Enable a password/PIN lock for security, and consult your IT department for policies like encryption or two-factor authentication.  
*Source: 001_Setting_Up_a_Mobile_Device_for_Company_Email.txt*


## Question 4 (out of scope -- not answerable from your documents)
**Q:** What is the CEO's home address?

**Retrieved chunks:**
  - [003_Configuring_VPN_Access_for_Remote_Workers.txt #3] dist=0.9551  "has changed to a company-assigned IP address. * If you continue to experience is..."
  - [001_Setting_Up_a_Mobile_Device_for_Company_Email.txt #1] dist=1.0253  "evice**  1. Go to the Settings app on your mobile device. 2. Select "Mail" or "E..."
  - [001_Setting_Up_a_Mobile_Device_for_Company_Email.txt #2] dist=1.0317  "ethod to "Username and Password" or "Domain\Username". 4. If prompted, enter you..."
  - [003_Configuring_VPN_Access_for_Remote_Workers.txt #2] dist=1.0378  "nce connected, you will see a confirmation message indicating that you are conne..."

**Answer:**
> I don't have enough information in the documents to answer that.

**Notes:** 
