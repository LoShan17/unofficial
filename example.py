

import unofficial.unofficial
import pprint

new_terminal = unofficial.unofficial.UnofficialTerminal()

new_terminal.get_ratios_summary('eln', 'ita')
print(new_terminal.current_response_text)
new_terminal.last_response_csv_dump()


new_terminal.get_statement('fca', 'ita', unofficial.unofficial.StatementsParams.INCOME_STATEMENT, 6)
print(new_terminal.current_response_text)
new_terminal.last_response_csv_dump()