# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

helps['complete'] = """
type: command
short-summary: Provides argument completions for any shell.
examples:
    - name: Auto-completes as "az keyvault" because "keyvault" is the first match alphabetically.
      text: >
        az complete "az key⇥"
    - name: Auto-completes as "az keyvault --help" because "p" is a subscript of "--help", which is the first match alphabetically.
      text: >
        az complete "az keyvault p⇥
"""
