#initialising blockchain list
blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]
#returns value for easier readability 


def add_transaction(transactional_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transactional_amount])

def get_transaction_value():
    return float(input('Your Transaction amount please:'))

def get_user_choice():
    user_input = input('your choice: ')
    return user_input

def print_blockchain_elements():
     # outputting the blockchain list to the console
     for block in blockchain:
        print('Outputing Blockchain')
        print(block)
     else:
        print('-' * 20)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
        elif block[0] == blockchain[block_index-1]:
            is_valid = True
        else:
           is_valid = False
           break
        return is_valid

   
tx_amount= get_transaction_value()
add_transaction(tx_amount)

waiting_for_input = True

while waiting_for_input:
    print('please choose')
    print('1: Add a new transactional value')
    print('2: Output the chain block')
    print('h: Manipulate the chain')
    print('q:Quit')
    user_choice  = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())

    elif user_choice == '2':
        print_blockchain_elements()
    
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    
    elif user_choice == 'q':
        waiting_for_input = False

    else:
        print('Input was invalid, please pick a value from the list!')

    if not verify_chain():
        print('Invalid blockchain')
        break
else:
    print('User left')
   


print('Done!')