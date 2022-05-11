{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "684c8bba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of elements required\t2\n",
      "Enter the elements\tdd\n",
      "Enter the elements\t44\n",
      "{'dd', '44'}\n",
      "Select your Option to perform Set operation\n",
      " 1.View set\n",
      " 2.Update\n",
      " 3.Add element\n",
      " 4.Subset\n",
      " 5.Remove\n",
      " 6.Discard\n",
      " 7.Pop\n",
      " 8.Length\n",
      " 9.Union\n",
      " 10. Intersection\n",
      " 11.Copy\n",
      " 15.Exiting---->>>>\n",
      "choice15\n",
      "You have selected Exiting---->>>> operation\n"
     ]
    }
   ],
   "source": [
    "\n",
    "def createSet():\n",
    "    set1=set( )\n",
    "    numEle=int(input(\"Enter the number of elements required\\t\"))\n",
    "    for i in range(0,numEle):\n",
    "        elem=input(\"Enter the elements\\t\")\n",
    "        set1.add(elem)\n",
    "    return set1\n",
    "set1=createSet()\n",
    "print(set1)\n",
    "def updateSet(upd):\n",
    "    set1.update(set2)\n",
    "    return set1\n",
    "def addSet(addEle):\n",
    "    set1.add(ele)\n",
    "    return set1\n",
    "def subSet(sub):\n",
    "    s=set2.issubset(set1)\n",
    "    return s\n",
    "def removeSet(remove):\n",
    "    set1.remove(ele)\n",
    "    return set1\n",
    "def discardSet(disc):\n",
    "    set1.discard(ele)\n",
    "    return set1\n",
    "def popSet(pop1):\n",
    "    set1.pop()\n",
    "    return set1\n",
    "def lenghtSet(length):\n",
    "    l=len(set1)\n",
    "    return l\n",
    "def unionSet(uni):\n",
    "    set2=set( )\n",
    "    numEle=int(input(\"Enter the number of elements required\\t\"))\n",
    "    for i in range(0,numEle):\n",
    "        elem=input(\"Enter the elements\\t\")\n",
    "        set1.add(elem)\n",
    "    return set1\n",
    "\n",
    "\n",
    "def setOp(options):   \n",
    "    if choice==1:\n",
    "        select=\"Create\"\n",
    "        print(f\"You have selected {select} operation\")     \n",
    "    elif choice==2:\n",
    "        select=\"Update\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==3:\n",
    "        select=\"Add elements\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==4:\n",
    "        select=\"Subset\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==5:\n",
    "        select=\"Remove\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==6:\n",
    "        select=\"Discard\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==7:\n",
    "        select=\"Pop\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==8:\n",
    "        select=\"Length\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==9:\n",
    "        select=\"Union\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==10:\n",
    "        select=\"Intersection\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==11:\n",
    "        select=\"Copy\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==15:\n",
    "        select=\"Exit---->>>>\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    else:\n",
    "        print(\"Invalid input\")\n",
    "    return choice\n",
    "print(\"Select your Option to perform Set operation\\n 1.View set\\n 2.Update\\n 3.Add element\\n 4.Subset\\n 5.Remove\\n 6.Discard\\n 7.Pop\\n 8.Length\\n 9.Union\\n 10. Intersection\\n 11.Copy\\n 15.Exit---->>>>\")\n",
    "while True:    \n",
    "    choice=int(input(\"choice\"))\n",
    "    setOp(choice)\n",
    "    if choice==1:\n",
    "        print(set1)\n",
    "    elif choice==2:\n",
    "        s=input(\"Enter the element to update\")\n",
    "        set2=str(s)\n",
    "        print(updateSet(set1),end=\" \")\n",
    "    elif choice==3:\n",
    "        ele=input(\"Enter the element to add\\n\")\n",
    "        print(addSet(set1),end=\" \")\n",
    "    elif choice==4:\n",
    "        set2=set(input(\"Enter the element to chech the Subset\"))\n",
    "        subSet(set1)\n",
    "    elif choice==5:\n",
    "        ele=input(\"Enter element to remove from set\\n\")\n",
    "        print(removeSet(ele),end=\"\")\n",
    "    elif choice==6:\n",
    "        ele=input(\"Enter an element to discard from list\\n\")\n",
    "        print(discardSet(set1),end=\" \")\n",
    "    elif choice==7:\n",
    "        print(popSet(set1),end=\" \")\n",
    "    elif choice==8:\n",
    "        print(lenghtSet(set1))\n",
    "    elif choice==9:\n",
    "        set2=createSet()\n",
    "        unionSet=set1.union(set2)\n",
    "        print(unionSet)\n",
    "    elif choice==15:\n",
    "        break\n",
    "    else:\n",
    "        print(\"!Wrong Input!\")\n"
   ]
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
