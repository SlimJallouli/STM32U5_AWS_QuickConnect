#!/bin/bash

# ******************************************************************************
# * @file    AWS_CLI_ProfileConfig.sh
# * @author  MCD Application Team
# * @brief   Configures aws cli for prod account
# ******************************************************************************
# * Copyright (c) 2022 STMicroelectronics.
#
# * All rights reserved.
#
# * This software component is licensed by ST under BSD 3-Clause license,
# * the "License"; You may not use this file except in compliance with the
# * License. You may obtain a copy of the License at:
# *                        opensource.org/licenses/BSD-3-Clause
# *
# ******************************************************************************

# Setting provision profile credentials 
provision_accessKey='1234567890ABCDEFG'
provision_secretKey='2YDnAuIZflnJt/bun8f2GoNScKQ8ao0YbnqFHUVBKNgEHg2k'
provision_profile='provision'

# Setting dashboard profile credentials 
dashboard_accessKey='1234567890ABCDEFG'
dashboard_secretKey='2YDnAuIZflnJt/bun8f2GoNScKQ8ao0YbnqFHUVBKNgEHg2k'
dashboard_profile='dashboard'

region='us-west-1'
outputForm='json'


# Configures aws cli for prod account

cat << EOF >> $HOME/.aws/config

[$provision_profile]
$region
$outputForm

[$dashboard_profile]
$region
$outputForm

EOF

cat << EOF >> $HOME/.aws/credentials

[$provision_profile]
aws_access_key_id=$provision_accessKey
aws_secret_access_key=$provision_secretKey

[$dashboard_profile]
aws_access_key_id=$dashboard_accessKey
aws_secret_access_key=$dashboard_secretKey

EOF
