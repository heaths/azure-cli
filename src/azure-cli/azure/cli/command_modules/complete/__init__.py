# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

import azure.cli.command_modules.complete._help  # pylint: disable=unused-import

class CompleteCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        complete_custom = CliCommandType(operations_tmpl='azure.cli.command_modules.complete.custom#{}')
        super(CompleteCommandsLoader, self).__init__(cli_ctx=cli_ctx, custom_command_type=complete_custom)

    def load_command_table(self, _):

        with self.command_group('') as g:
            g.custom_command('complete', 'complete_command')
        return self.command_table

    def load_arguments(self, _):
        with self.argument_context('complete') as c:
            c.positional('word', help='The word to complete.')
            c.argument('position', type=int, help='The current cursor position.')
            c.ignore('_subscription')

COMMAND_LOADER_CLS = CompleteCommandsLoader
