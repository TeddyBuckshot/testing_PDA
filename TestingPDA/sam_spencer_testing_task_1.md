### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.:
Thinking that methods should be renamed or should be class level, or using string interpolation etc.

These aren't errors but rather standards that vary from developer to developer.

Only comment on errors that would stop the tests running.

```python

class CardGame:

  def check_for_ace(self, card):
    # the if statement below should be '==' to express 'is equal to'.
    # currently it is trying to assign the INT 1 to 'card.value'
    if card.value = 1:
      return True
      # this else statement is missing a colon.
    else
      return False

# below is not a function, functions are declared with def. not dif.
# a comma is also missing between the two card variables.
  dif highest_card(self, card1 card2):
  # this if statement is not indented correctly.
  if card1.value > card2.value:
    # the return statement below is invalid. card is not a variable that has been initialised.
    return card
  else:
    return card2


# this entire function is not indented correctly.
def cards_total(self, cards):
  # the below variable is not initialised.
  total
  for card in cards:
    total += card.value
    # this return statement should be outside of the for loop or it will display the total after each itteration.
    # also better to remove the string return and use it where ever the the value 'total' is returned to
    return "You have a total of" + total

```
