::******************************************************************************
::* @file    awsConfig.bat
::* @author  MCD Application Team
::* @brief   Configures aws cli for prod account
::******************************************************************************
:: * Copyright (c) 2022 STMicroelectronics.
::
:: * All rights reserved.
::
:: * This software component is licensed by ST under BSD 3-Clause license,
:: * the "License"; You may not use this file except in compliance with the
:: * License. You may obtain a copy of the License at:
:: *                        opensource.org/licenses/BSD-3-Clause
:: *
:: ******************************************************************************

@echo off

cd %HOMEPATH%\.aws

if exist config (
    echo config file exist

    if exist config.bak (
        echo baclup file exist
    ) else (
        echo creating baclup file
        ren config   config.bak
    )

    del config
)

if exist credentials (
    echo config file exist

    if exist credentials.bak (
        echo baclup file exist
    ) else (
        echo creating baclup file
        ren credentials   credentials.bak
    )

    del credentials
)

::Setting provision profile credentials 
set provision_accessKey=AKIAQC3VOUARQERJ5LVQ
set provision_secretKey=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
set provision_profile=default

::Setting dashboard profile credentials 
set dashboard_accessKey=AKIAQC3VOUARXGGMWHHO
set dashboard_secretKey=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
set dashboard_profile=dashboard

set region=us-west-1
set outputForm=json


::Configures aws cli for prod account
(echo %provision_accessKey% && echo %provision_secretKey% && echo %region% && echo %outputForm%) | (aws configure --profile %provision_profile%)

(echo %dashboard_accessKey% && echo %dashboard_secretKey% && echo %region% && echo %outputForm%) | (aws configure --profile %dashboard_profile%)

@echo on
