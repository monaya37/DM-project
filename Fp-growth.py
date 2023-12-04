#Import Data
from collections import defaultdict
import pandas as pd

HorizantalData = pd.read_excel('Horizontal_Format.xlsx')
VerticalData = pd.read_excel('Vertical_Format.xlsx')

print(HorizantalData)
print(VerticalData)

#Variables
min_support = 0;
min_confidence = 0;
item_counts =l;


#Functions

def convert_to_horizantal(Vertical_Data):
    #code
    return 0; #retrun data in horizantal fromat

def generate_frequent_itemset(df, min_support):

    #Split items in the lists
    transactions = df['items'].str.split(',')

    #Store itemsets and support count in dictionary
    item_counts = defaultdict(int)
    total_transactions = len(transactions)

    #Loop on transactions to count item occurrences
    for transaction in transactions:
        unique_items = set(transaction)
        for item in unique_items:
            item_counts[item] += 1


   # --> Check if min_support is a number or a percentage

     #if min_support is a number
    if isinstance(min_support, (int, float)) and not (0 < min_support <= 1):
        min_support_count = min_support

     #if min_support is a ratio/fraction
    elif isinstance(min_support, (int, float)) and (0 < min_support <= 1):
        min_support_count = min_support * total_transactions

     #if min_support is a percentage
    else:
        min_support_count = min_support * total_transactions / 100


    #calculate support and filter frequent items
    frequent_itemsets = {item: support for item, support in item_counts.items() if support >= min_support_count}
    print("Frequent Itemsets With Support >=" , min_support , ":")
    return frequent_itemsets

frequent_itemsets = generate_frequent_itemset(df, 3)
for itemset, support in frequent_itemsets.items():
    print(f"{itemset}: {support}")

def ordered_itemsets(item_counts):
    sorted_items = sorted(item_counts.items(), key=lambda x:x[1])
    converted_dict = dict(sorted_items)
    return converted_dict

ordered_transaction = ordered_itemsets(item_counts)
    

def represent(data):
    #code
    #represent the frequent items in the form of association rules.
    #print? return in array ?
    return 0; 

def extract(data):
    #code
    #Extract the strong rules.
    #تعتمد نوعا ما على اللي قبلها
    return 0; 

def get_sorted_transactions(frequent_itemsets):
    transactions = HorizantalData['items'].str.split(',')

    T1 = defaultdict(int) #for each transaction
    T2  = []              #to copy values into
    Transactions = []     #array of transactions

    for transaction in transactions:
        items = set(transaction)
        for item in items:
            if frequent_itemsets.get(item) is not None:
                T1.update({item : frequent_itemsets[item]})
        T2 = T1.copy()
        Transactions.append(T2)
        T1.clear()

    Sorted_Transactions = []
    for transaction in Transactions:
        sorted_transactions = sorted(transaction.items(), key=lambda x:x[1], reverse = True)
        Sorted_Transactions.append(dict(sorted_transactions))

    return Sorted_Transactions

        
sorted_transactions = get_sorted_transactions(frequent_itemsets)
print(sorted_transactions)


def get_conditional_pattern_base(frequent_itemsets,sorted_sransactions):
    x = dict(sorted(frequent_itemsets.items(), key=lambda x:x[1]))
    sorted_frequent_itemsets = x.keys() #menna handled this already?
    pattern_base = defaultdict(int)
    temp = defaultdict(int) #used to copy
    coditional_pattern_base = dict()

    for item in sorted_frequent_itemsets:
        for i in range(len(sorted_sransactions)):
            if (sorted_sransactions[i].get(item) is not None):
                transaction = sorted_sransactions[i].keys()
                index = list(transaction).index(item)
                path1 = list(transaction)[:index]
                path = ''
                if(len(path1) > 0):
                    for i in range(len(path1)):
                        path+=path1[i] + ','
                    path = list(path)
                    path.pop()
                    path = ''.join(path)
                pattern_base[path] += 1

        temp = pattern_base.copy()
        coditional_pattern_base[item] = temp
        pattern_base.clear()

    return coditional_pattern_base; 

coditional_pattern_base = get_conditional_pattern_base(frequent_itemsets,sorted_transactions)
for item in frequent_itemsets.keys():
    print("item:" , item, dict(coditional_pattern_base[item]))


def get_conditional_trees(coditional_pattern_base):
    conditional_trees = dict()
    x = defaultdict(int)

    for item in coditional_pattern_base:
        summ = sum(coditional_pattern_base[item].values())

        if(coditional_pattern_base[item]):
            common = list(coditional_pattern_base[item].keys())[0]
            
            for path in coditional_pattern_base[item]:
                common = set(path) & set(common)
            common = str(common)
            
            for i in range(len(common)):
                if(common[i].isalpha()):
                    x[common[i]] = summ
            temp = x.copy()
            conditional_trees[item] = temp
            x.clear()
            
    return conditional_trees


for item in conditional_trees:
    print(item , dict(conditional_trees[item]))