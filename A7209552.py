print('第一題')
import string
alphabet=string.ascii_letters
print(alphabet)
print('第二題')
count_letters={}
count_letters=count_letters.fromkeys(alphabet,0)
address = 'Four score and seven years ago our fathers brought forth on thiscontinent, a new nation, conceived in Liberty, and dedicated to theproposition that all men are created equal. Now we are engaged in a greatcivil war, testing whether that nation, or any nation so conceived anddedicated, can long endure. We are met on a great battle-field of that war.We have come to dedicate a portion of that field, as a final resting placefor those who here gave their lives that that nation might live. It isaltogether fitting and proper that we should do this. But, in a largersense, we cannot dedicate -- we cannot consecrate -- we cannot hallow --this ground. The brave men, living and dead, who struggled here, haveconsecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forgetwhat they did here. It is for us the living, rather, to be dedicated hereto the unfinished work which they who fought here have thus far so noblyadvanced. It is rather for us to be here dedicated to the great taskremaining before us -- that from these honored dead we take increaseddevotion to that cause for which they gave the last full measure ofdevotion -- that we here highly resolve that these dead shall not have diedin vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shallnot perish from the earth.'
for letter in address:
    if letter in count_letters.keys():
        count_letters[letter]+=1
print(count_letters)
print('第三題')
count_letters={}
sentence=count_letters
def counter(input_string):
    count_letters=input_string
    count_letters=count_letters.fromkeys(alphabet,0)
    for letter in address:
        if letter in count_letters.keys():
            count_letters[letter]+=1
    return count_letters
address_count=counter(sentence)
print(address_count)