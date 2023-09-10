## noCaptcha_Selenium
This repository aims to utilize noCaptcha in selenium while the current API isn't yet available, at least in Google Recaptcha.


Note: This doesn't directly use noCaptcha API since it's yet [work in progress](https://docs.nocaptchaai.com/en/image/reCaptcha.html) but this repository aims to automate installation of noCaptcha extension in chrome and provides functions to check captcha's current states (not available, currently solving, solved).


Basically this repository does the following:
1. Install noCaptcha on selenium
2. Detects for captcha and waits until the extension solves it.
