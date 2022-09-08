# STM32U5_AWS_QuickConnect

## Clone the repo
`git clone https://github.com/SlimJallouli/STM32U5_AWS_QuickConnect.git`

## Create 2 IAM users
    
* First usesr with the AWSIoTFullAccess policy. This IAM user will be used to register the device with AWS IoI core
    
* Second user with the following policy

``

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "iot:Receive",
                    "iot:ListNamedShadowsForThing",
                    "iot:Subscribe",
                    "iot:Connect",
                    "iot:GetThingShadow",
                    "iot:DeleteThingShadow",
                    "iot:UpdateThingShadow",
                    "iot:Publish"
                ],
                "Resource": [
                    "arn:aws:iot:<your-region>:<your-account-number>:topic/*",
                    "arn:aws:iot:<your-region>:<your-account-number>:topic/$aws/things/*",
                    "arn:aws:iot:<your-region>:<your-account-number>:client/*",
                    "arn:aws:iot:<your-region>:<your-account-number>:thing/*",
                    "arn:aws:iot:<your-region>:<your-account-number>:topicfilter/*"
                ]
            }
        ]
    }
``



* use AWS CLI to create 2 profiles (default and dash_board)

* python .\STM32U5_AWS_QuickConnect.py --ssid=<YOUR_2.4HGz_WIFI_SSID> --password=<YOUR_WIFI_PASSWORD> --dashboard-profile=<AWS_CLI_DASHBOARD_PROFILE> --provision-profile=<AWS_CLI_PROVISION_PROFILE> --dashboard-url=<DASHBOARD_URL>


## Example:

    python .\STM32U5_AWS_QuickConnect.py --ssid=st_iot_demo --password=stm32u585 --dashboard-profile=dash_board --provision-profile=default --dashboard-url=https://main.3mkj47qkab3qo.amplifyapp.com
