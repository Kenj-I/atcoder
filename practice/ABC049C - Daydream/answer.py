# daydream

import re
answer = input()
answer = re.sub('eraser', '', answer)
answer = re.sub('erase', '', answer)
answer = re.sub('dreamer', '', answer)
answer = re.sub('dream', '', answer)

print('YES' if len(answer) == 0 else 'NO')