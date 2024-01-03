MINING_REWARD = 10

genesis_block = {'previous_hash': '', 
            'index': 0, 
            'transactions': []}
blockchain = [genesis_block]
# initializing an empty list
# The list intends to store dictionaries.
open_transactions = []
owner = 'Seazle'
participants = {'Seazle'}


def hash_block(block):
    return '-'.join([str(block[key] for key in block)])

def get_balance(participant):
    tx_sender = [[tx [amount] for tx in l ['transactions'] if tx['sender']== participant]for l in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    
    tx_recepient = [[tx [amount] for tx in block ['transactions'] if tx['recepient']== participant]for block in blockchain]
    amount_received = 0
    for tx in tx_recepient:
         if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent

def get_last_blockchain_value():
    if len(blockchain) < 1 :
        return None
    return blockchain[-1]

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']



# the function below accepts 2 arguments
# one that is required (transactional amount) and the optional (last transaction)
# the optional one is optional since it has default value of => [1]

def add_transaction(recepient, sender= owner, amount=1.0):
    """arguments:
    sender:the sender of the coin
    recepient:the receiver of the coin
    amount: the amount of coins send with the transaction(default =1.0)
    """
    transaction ={
        'sender':sender,  
        'recepient':recepient, 
        'amount':amount
        }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recepient)


def mine_block():
   last_block = blockchain[-1]
   hashed_block = hash_block(last_block)
   reward_transaction = {
       'sender': 'MINING',
       'recepient' : owner,
       'amount': MINING_REWARD
   }
   open_transactions.append(reward_transaction)
#    for key in blockchain:
#        value = last_block[key]
#        hashed_block= hashed_block + str(value)
   block = {'previous_hash': hashed_block, 
            'index':len(blockchain), 
            'transactions': open_transactions
           }
   blockchain.append(block)
   return True

def get_transaction_value():
    tx_recepient = input('Enter the recepient of the transaction:')
    tx_amount = float(input('Your Transaction amount please:'))
    return tx_recepient, tx_amount

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
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain(blockchain[index - 1])):
            return False
    return True

    # block_index = 0
    # is_valid = True
    # for block_index in range(len(blockchain)):
    #     if block_index == 0:
    #         continue
    #     elif blockchain[block_index][0] == blockchain[block_index-1]:
    #         is_valid = True
    #     else:
    #        is_valid = False
    #        break
    #     return is_valid


    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #          continue
    #     elif block[0] == blockchain[block_index-1]:
    #         is_valid = True
    #     else:
    #        is_valid = False
    #        break
    #     return is_valid

   
# tx_amount= get_transaction_value()
# add_transaction(tx_amount)

waiting_for_input = True

# a while loop is fot the user input
# this is a loop thatexits once waiting_for_input becomeFalse or break
while waiting_for_input:
    print('please choose')
    print('1: Add a new transactional value')
    print('2: mine a new block')
    print('3: Output the chain block')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q:Quit')
    user_choice  = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recepient, amount = tx_data
        # Add transaction amount to the block chain
        add_transaction(recepient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print('participants1')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '', 
            'index': 0, 
            'transactions': [{'sender':'Seazle', 'recepient':'waynee', 'amount':'100.0'}]}
    
    elif user_choice == 'q':
        waiting_for_input = False

    else:
        print('Input was invalid, please pick a value from the list!')

    # if not verify_chain():    
    #     print_blockchain_elements()
    #     print('invalid chain')
    #     break
else:
    print('User left')
   
print(get_balance('seazle'))

print('Done!')