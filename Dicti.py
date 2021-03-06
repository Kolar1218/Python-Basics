{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75a6a0ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "==============================================================================================================\n",
    "\n",
    "Project1: Datastructure calculator (List/tuple/set/dictionary/loops)\n",
    "\n",
    "==========================================\n",
    "\n",
    "Welcome to Data structure calculator\n",
    "\n",
    "Please select any one Data structure, \n",
    "1. List (15 operations) ==> List.py\n",
    "2. Tuple (5 operatios)  ===> Tuple.py\n",
    "3. Set (15 operations) ===> Set.py\n",
    "4. Dictionary (10 operations) ==> Dict.py\n",
    "\n",
    "Main.py\n",
    "\n",
    "import List\n",
    "import Tuple\n",
    "import Set\n",
    "import Dict\n",
    "\n",
    "\n",
    "Do create Datastructure:\n",
    "\n",
    "List ==> selected\n",
    "1. create list \n",
    "\n",
    "Options under List:\n",
    "\n",
    "1. append\n",
    "2. pop\n",
    "3. update / concatenation\n",
    "4. sum/min/max\n",
    "6. len \n",
    "7. mean\n",
    "8. median\n",
    "9. find\n",
    "10. frequency\n",
    "11. .... 15 operations\n",
    "\n",
    "(15 operations)\n",
    "\n",
    "\n",
    "Set:\n",
    "\n",
    "Create a set\n",
    "\n",
    "Options:\n",
    "\n",
    "1. add\n",
    "2. update\n",
    "3. intersection\n",
    "\n",
    "1. Start with the project\n",
    "2. Modules\n",
    "3. Documentation\n",
    "4. Exception handling\n",
    "5. Github documentation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c5491354",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number of elements required2\n",
      "Enter key10\n",
      "Enter valuefront\n",
      "Enter key14\n",
      "Enter valueback\n",
      "{'gk': 'dk', '10': 'front', '14': 'back'}\n"
     ]
    }
   ],
   "source": [
    "#create dict\n",
    "def createDict():\n",
    "    dict={}\n",
    "    noEle=int(input(\"Enter number of elements required\"))\n",
    "    for i in range(0,noEle):\n",
    "        keys1=input(\"Enter key\")\n",
    "        values1=input(\"Enter value\")\n",
    "        dict1[keys1]=values1\n",
    "    return dict1\n",
    "dict1=createDict()\n",
    "print(dict1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a8211f9b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'gk': 'dk', '10': 'front', '14': 'back'}\n"
     ]
    }
   ],
   "source": [
    "print(dict1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8ed28cc8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter th key to search the vlaue\n",
      "14\n",
      "the value is:\t back\n"
     ]
    }
   ],
   "source": [
    "#get vlue using key\n",
    "def getDict(getd):\n",
    "    k=dict1.get(ele)\n",
    "    return k\n",
    "ele=input(\"Enter the key to search the vlaue\\n\")\n",
    "print(\"the value  of key is:\\t\",getDict(dict1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "1d04889f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'1': 'kolar', 'password': 'system', 'kolar': 'gowda', 'bajaj': 'Pulsar', 'ktm': 'duke'} "
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "48428f02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter key to update14\n",
      "Enter value to updatewas\n",
      "{'gk': 'dk', '10': 'front', '14': 'was'} "
     ]
    }
   ],
   "source": [
    "#update\n",
    "def updateDict(upd1):\n",
    "    keys=input(\"Enter key to update\")\n",
    "    values=input(\"Enter value to update\")\n",
    "    dict1.update({keys:values})\n",
    "    return dict1\n",
    "print(updateDict(dict1),end=\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "170fbefe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the key to delete item10\n",
      "{'gk': 'dk'}\n"
     ]
    }
   ],
   "source": [
    "#del item\n",
    "def delDict(delete):\n",
    "    keys=input(\"Enter the key to delete item\")\n",
    "    del[dict1[keys]]\n",
    "    return dict1\n",
    "print(delDict(dict1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "08263cdd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the key to add11\n",
      "enter the value to addform\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{'gk': 'dk', '11': 'form'}"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def addDict(add):\n",
    "    keys=input(\"Enter the key to add\")\n",
    "    values=input(\"enter the value to add\")\n",
    "    dict1[keys]=values\n",
    "    return dict1\n",
    "addDict(dict1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "fc13ddf1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the key to search547\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Check perticular key exist in dict\n",
    "def membDictKey(mem):\n",
    "    keys=input(\"Enter the key to search\")\n",
    "    if keys in dict1:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "membDict(dict1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a6fe8213",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the key to searchgk\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c192fcd0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values(['kolar', 'manager', 'system', 'gowda', 'Pulsar'])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#show values\n",
    "def valuesDict(val):\n",
    "    v=dict1.values()\n",
    "    return v\n",
    "valuesDict(dict1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "a7ff244d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['gk', 'ff', '9ddkd', '552'])"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#show keys\n",
    "def keysDict(val):\n",
    "    k=dict1.keys()\n",
    "    return k\n",
    "keysDict(dict1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "3636f471",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([('1', 'kolar'), ('2', 'manager'), ('password', 'system'), ('kolar', 'gowda'), ('bajaj', 'Pulsar')])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#items of dict\n",
    "def itemDict(item):\n",
    "    r=dict1.items()\n",
    "    return r\n",
    "itemDict(dict1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "acbdfc7c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the key to pop element8\n",
      "{'gk': 'dk', 'ff': '54', '9ddkd': '787', '552': 'eded'} "
     ]
    }
   ],
   "source": [
    "#pop\n",
    "def popDict(pop1):\n",
    "    keys=input(\"Enter the key to pop element\\t\")\n",
    "    dict1.pop(keys)\n",
    "    return dict1\n",
    "print(popDict(dict1),end=\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "e3276fc9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'1': 'kolar', 'password': 'system', 'kolar': 'gowda', 'bajaj': 'Pulsar'}"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#popitems\n",
    "def popitemDict(itmpop):\n",
    "    dict1.popitem()\n",
    "    return dict1\n",
    "popitemDict(dict1)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "b2d91111",
   "metadata": {},
   "source": [
    "kolar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "7cbc7c32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the new dict to copy existing dictkolar\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{'gk': 'dk', 'ff': '54', '9ddkd': '787', '552': 'eded'}"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#copy\n",
    "def copyDict(copy1):\n",
    "    file=dict1.copy()\n",
    "    return file\n",
    "file=input(\"Enter the new dict to copy existing dict\")\n",
    "file=dict1\n",
    "copyDict(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "35049dd6",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'kolar' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_280/2498657089.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkolar\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'kolar' is not defined"
     ]
    }
   ],
   "source": [
    "print(kolar)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "12b00b09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'gk': 'dk', '11': 'form', 'ff': '54', '4': '55', '8': 'ggo', '9ddkd': '787', '552': 'eded', '2': 'fff'} "
     ]
    }
   ],
   "source": [
    "def viewDict(dic):\n",
    "    return dict1\n",
    "print(viewDict(dict1),end=\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "7945f50a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number of elements required2\n",
      "Enter key10\n",
      "Enter valuess\n",
      "Enter key20\n",
      "Enter valuewew\n",
      "{'gk': 'dk', 'ff': '54', '552': 'eded', '5': 'kolar', '4': 'gowda', '10': 'ss', '20': 'wew'}\n",
      "Select your Option to perform Dictionary operation\n",
      " 1.View Dictionary\n",
      " 2.Get Element\n",
      " 3.Update\n",
      " 4.Delete\n",
      " 5.Add\n",
      " 6.Pop\n",
      " 7.Keys of Dict\n",
      " 8.Pop item\n",
      " 9.Check key exists in dict\n",
      " 10.Display values of dict\n",
      " 11.Exit\n",
      "Select operation to perform11\n",
      "You have selected Exit operation\n"
     ]
    }
   ],
   "source": [
    "def createDict():\n",
    "    dict={}\n",
    "    noEle=int(input(\"Enter number of elements required\"))\n",
    "    for i in range(0,noEle):\n",
    "        keys1=input(\"Enter key\")\n",
    "        values1=input(\"Enter value\")\n",
    "        dict1[keys1]=values1\n",
    "    return dict1\n",
    "dict1=createDict()\n",
    "print(dict1)\n",
    "\n",
    "def viewDict(dic):\n",
    "    return dict1\n",
    "\n",
    "\n",
    "def getDict(getd):\n",
    "    k=dict1.get(ele)\n",
    "    return k\n",
    "\n",
    "def updateDict(upd1):\n",
    "    keys=input(\"Enter key to update\")\n",
    "    values=input(\"Enter value to update\")\n",
    "    dict1.update({keys:values})\n",
    "    return dict1\n",
    "def delDict(delete):\n",
    "    keys=input(\"Enter the key to delete item\")\n",
    "    del[dict1[keys]]\n",
    "    return dict1\n",
    "def addDict(add):\n",
    "    keys=input(\"Enter the key to add\")\n",
    "    values=input(\"enter the value to add\")\n",
    "    dict1[keys]=values\n",
    "    return dict1\n",
    "\n",
    "def popDict(pop1):\n",
    "    keys=input(\"Enter the key to pop element\\t\")\n",
    "    dict1.pop(keys)\n",
    "    return dict1\n",
    "def keysDict(key1):\n",
    "    k=dict1.keys()\n",
    "    return k\n",
    "def popitemDict(itmpop):\n",
    "    dict1.popitem()\n",
    "    return dict1\n",
    "def membDictKey(mem):\n",
    "    keys=input(\"Enter the key to search\")\n",
    "    if keys in dict1:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "def valuesDict(val):\n",
    "    v=dict1.values()\n",
    "    return v\n",
    "\n",
    "\n",
    "\n",
    "def dictOp(options):   \n",
    "    if choice==1:\n",
    "        select=\"View Dictionary\"\n",
    "        print(f\"You have selected {select} operation\")     \n",
    "    elif choice==2:\n",
    "        select=\"Get Element\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==3:\n",
    "        select=\"Update\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==4:\n",
    "        select=\"Delete\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==5:\n",
    "        select=\"Add\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==6:\n",
    "        select=\"Pop\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==7:\n",
    "        select=\"Keys of Dict\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==8:\n",
    "        select=\"Pop item\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==9:\n",
    "        select=\"Check key exists in dict\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==10:\n",
    "        select=\"Display values of dict\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==11:\n",
    "        select=\"Exit\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    else:\n",
    "        print(\"Invalid input\")\n",
    "    return choice\n",
    "\n",
    "while True:\n",
    "    print(\"Select your Option to perform Dictionary operation\\n 1.View Dictionary\\n 2.Get Element\\n 3.Update\\n 4.Delete\\n 5.Add\\n 6.Pop\\n 7.Keys of Dict\\n 8.Pop item\\n 9.Check key exists in dict\\n 10.Display values of dict\\n 11.Exit\")\n",
    "    \n",
    "    choice=int(input(\"Select operation to perform\"))\n",
    "    dictOp(choice)\n",
    "    if choice==1:\n",
    "        print(viewDict(dict1),end=\" \")\n",
    "\n",
    "    elif choice==2:\n",
    "        ele=input(\"Enter the key to search the vlaue\\n\")\n",
    "        print(\"the value  of key is:\\t\",getDict(dict1))\n",
    "    elif choice==3:\n",
    "        print(updateDict(dict1),end=\" \")\n",
    "    elif choice==4:\n",
    "        print(delDict(dict1))\n",
    "    elif choice==5:\n",
    "        addDict(dict1)\n",
    "    elif choice==6:\n",
    "        print(popDict(dict1),end=\" \")\n",
    "    elif choice==7:\n",
    "        keysDict(dict1)\n",
    "    elif choice==8:\n",
    "        popitemDict(dict1)\n",
    "    elif choice==9:\n",
    "        membDict(dict1)\n",
    "    elif choice==10:    \n",
    "        valuesDict(dict1)\n",
    "    elif choice==11:\n",
    "        break\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8cccc50",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
