d = input('Enter a sentence: ')
def backwards(text):
  backwards_text = ''
  for c in text:
    backwards_text = f'{c}{backwards_text}'
  return backwards_text
print(backwards(d))
