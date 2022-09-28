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
provision_accessKey='AKIAQC3VOUARQERJ5LVQ'
provision_secretKey='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'
provision_profile='default'

# Setting dashboard profile credentials 
dashboard_accessKey='AKIAQC3VOUARXGGMWHHO'
dashboard_secretKey='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'
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
