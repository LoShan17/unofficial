

import unofficial.unofficial

new_terminal = unofficial.unofficial.UnofficialTerminal()

new_terminal.get_ratios_summary('eln', 'ita')
print(new_terminal.current_response_text)
new_terminal.last_response_csv_dump()