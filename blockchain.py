import functools
# reward for new timers(for creating a new block)
MINING_REWARD = 10
# starting block for theblock-chain
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
    tx_sender = [[tx [amount] for tx in block ['transactions'] if tx['sender']== participant]for block in blockchain]
    # fetch a list of all sent coin amounts for the given person(empty lists are returned if the person was not the sender)
    # This fetches sent amounts of open transactions to avoid double spending
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender']==participant]
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amt:tx_sum + sum(tx_amt) if len(tx_amt)>0 else tx_sum+0, tx_sender, 0)
    # this fetches coin amounts of transaction that were already included in block of bllockchain
    # we ignore open transactions here because you shouldnt be ale to spend coins before the transaction is confirmed 
    tx_recepient = [[tx ['amount'] for tx in block ['transactions'] if tx['recepient']== participant]for block in blockchain]
    amount_received = functools.reduce(lambda tx_sum, tx_amt:tx_sum + sum(tx_amt) if len(tx_amt)>0 else tx_sum+0, tx_recepient, 0)
    # Return the balance
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
        return True
    return False


def mine_block():
   last_block = blockchain[-1]
   hashed_block = hash_block(last_block)
   reward_transaction = {
       'sender': 'MINING',
       'recepient' : owner,
       'amount': MINING_REWARD
   }
#    This ensures that the original list remains unchanged.
   copied_transactions = open_transactions[:]
   copied_transactions.append(reward_transaction)   
   block = {'previous_hash': hashed_block, 
            'index':len(blockchain), 
            'transactions': copied_transactions
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

def verify_transactions():
    return all([verify_transaction[tx] for tx in open_transactions])
            

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
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q:Quit')
    user_choice  = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recepient, amount = tx_data
        # Add transaction amount to the block chain
        if add_transaction(recepient, amount=amount):
            print('Added transaction')

        else:
            print('transction failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print('participants1')
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('Invalid transactions!')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '', 
            'index': 0, 
            'transactions': [{'sender':'Seazle', 'recepient':'waynee', 'amount':'100.0'}]}
    
    elif user_choice == 'q':
        waiting_for_input = False

    else:
        print('Input was invalid, please pick a value from the list!')

    if not verify_chain():    
        print_blockchain_elements()
        print('invalid chain')
        break
    print('Balance of {}:{:6.2f}'.format ('Seazle',get_balance('Seazle')))
else:
    print('User left')
   
print(get_balance('seazle'))

print('Done!')