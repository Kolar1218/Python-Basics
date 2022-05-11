{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9ca5d149",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Number of elements required\t2\n",
      "Enter the elements\t5\n",
      "Enter the elements\t6\n",
      "[5, 6]\n",
      "Select any Options to perform list operation\n",
      " 1.View List\n",
      " 2.Length\n",
      " 3.Sum of List\n",
      " 4.Median\n",
      " 5.Mean\n",
      " 6.Update\n",
      " 7.Access Element\n",
      " 8.Sort\n",
      " 9.Minimum of list\n",
      " 10. Maximum of List\n",
      " 11.Remove\n",
      " 12.Add Element\n",
      " 13.Extend List\n",
      " 14.View List\n",
      " 15.Clear\n",
      "16.Exit\n",
      "\n",
      "Select operation1\n",
      "You have selected View List operation\n",
      "[5, 6]\n",
      "Select operation2\n",
      "You have selected Length operation\n",
      "2\n",
      "Select operation3\n",
      "You have selected Sum operation\n",
      "11\n",
      "Select operation4\n",
      "You have selected Median operation\n",
      "[5, 6]\n",
      "Select operation5\n",
      "You have selected Mean operation\n",
      "5.5\n",
      "Select operation6\n",
      "You have selected Update operation\n",
      "Enter the position1\n",
      "Enter the element to update88\n",
      "Updated list is [5, 88]\n",
      "Select operation7\n",
      "You have selected Access Element operation\n",
      "Enter the position0\n",
      "5\n",
      "Select operation8\n",
      "You have selected Sort operation\n",
      "[5, 88]\n",
      "Select operation9\n",
      "You have selected Minimum of List operation\n",
      "5\n",
      "Select operation10\n",
      "You have selected Maximum of List operation\n",
      "88\n",
      "Select operation11\n",
      "You have selected Remove operation\n",
      "Enter the element to remove from the list5\n",
      "List before removing the element [5, 88]\n",
      "List after removing the element [88]\n",
      "Select operation12\n",
      "You have selected Add Element operation\n",
      "Enter an intger to add\t445\n",
      "List before adding the element [88]\n",
      "List after adding the element [88, 445]\n",
      "Select operation13\n",
      "You have selected Extend operation\n",
      "Number of ele3\n",
      "elements5\n",
      "elements55\n",
      "elements555\n",
      "[5, 55, 555]\n",
      "List after Extend [88, 445, 5, 55, 555]\n",
      "Select operation15\n",
      "You have selected Clear operation\n",
      "[]\n",
      "Select operation16\n",
      "You have selected Exit operation\n"
     ]
    }
   ],
   "source": [
    "def createList():\n",
    "    listEle=[]\n",
    "    eleReq=int(input(\"Enter the Number of elements required\\t\"))\n",
    "    for i in range(0,eleReq):\n",
    "        ele=int(input(\"Enter the elements\\t\"))\n",
    "        listEle.append(ele)\n",
    "    return listEle\n",
    "list1=createList()\n",
    "print(list1)\n",
    "\n",
    "def lenList():\n",
    "    length=len(list1)\n",
    "    return length\n",
    "\n",
    "def sumList(addi):\n",
    "    add=sum(list1)\n",
    "    return add\n",
    "def medianList(median):\n",
    "    median=list1[(len(list1)-1)//2:(len(list1)+2)//2]\n",
    "    return median\n",
    "def meanList(mean):\n",
    "    mean=sum(list1)/len(list1)\n",
    "    return mean\n",
    "def updateList(update):\n",
    "    list1[pos]=ele\n",
    "    return update\n",
    "def accessList(access):\n",
    "    return list1[ele]\n",
    "def sortList(sort):\n",
    "    list1.sort()\n",
    "    return list1\n",
    "def minList(min):\n",
    "    list1.sort()\n",
    "    mini=list1[0]\n",
    "    return mini\n",
    "def maxList(max):\n",
    "    list1.sort()\n",
    "    maxi=list1[-1]\n",
    "    return maxi\n",
    "def removeList(rem):\n",
    "    r=list1.remove(ele)\n",
    "    return r\n",
    "def addele(newEle):\n",
    "    e=list1.append(ele)\n",
    "    return e\n",
    "def clearList(allClear):\n",
    "    list1.clear()\n",
    "    return allClear\n",
    "def listView(lis):\n",
    "    return list1\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "def listOp(options):   \n",
    "    if choice==1:\n",
    "        select=\"View List\"\n",
    "        print(f\"You have selected {select} operation\")     \n",
    "    elif choice==2:\n",
    "        select=\"Length\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==3:\n",
    "        select=\"Sum\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==4:\n",
    "        select=\"Median\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==5:\n",
    "        select=\"Mean\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==6:\n",
    "        select=\"Update\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==7:\n",
    "        select=\"Access Element\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==8:\n",
    "        select=\"Sort\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==9:\n",
    "        select=\"Minimum of List\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==10:\n",
    "        select=\"Maximum of List\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==11:\n",
    "        select=\"Remove\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==12:\n",
    "        select=\"Add Element\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==13:\n",
    "        select=\"Extend\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==14:\n",
    "        select=\"View list\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==15:\n",
    "        select=\"Clear\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    elif choice==16:\n",
    "        select=\"Exit\"\n",
    "        print(f\"You have selected {select} operation\")\n",
    "    else:\n",
    "        print(\"Invalid input\")\n",
    "    return choice\n",
    "print(\"Select any Options to perform list operation\\n 1.View List\\n 2.Length\\n 3.Sum of List\\n 4.Median\\n 5.Mean\\n 6.Update\\n 7.Access Element\\n 8.Sort\\n 9.Minimum of list\\n 10. Maximum of List\\n 11.Remove\\n 12.Add Element\\n 13.Extend List\\n 14.View List\\n 15.Clear\\n16.Exit\\n\")\n",
    "while True:\n",
    "    choice=int(input(\"Select operation\"))\n",
    "    listOp(choice)\n",
    "    if choice==1:\n",
    "        print(list1)\n",
    "    elif choice==2:\n",
    "        print(lenList())\n",
    "    elif choice==3:\n",
    "        print(sumList(list1))\n",
    "    elif choice==4:\n",
    "        print(medianList(list1))\n",
    "    elif choice==5:\n",
    "        print(meanList(list1))    \n",
    "    elif choice==6:\n",
    "        pos=int(input(\"Enter the position\"))\n",
    "        ele=int(input(\"Enter the element to update\"))\n",
    "        updateList(list1)\n",
    "        print(\"Updated list is\",list1)\n",
    "    elif choice==7:\n",
    "        ele=int(input(\"Enter the position\"))\n",
    "        print(accessList(list1))\n",
    "    elif choice==8:\n",
    "        print(sortList(list1))\n",
    "    elif choice==9:  \n",
    "        print(minList(list1))\n",
    "    elif choice==10:\n",
    "        print(maxList(list1))\n",
    "    elif choice==11:\n",
    "        ele=int(input(\"Enter the element to remove from the list\"))\n",
    "        print(\"List before removing the element\",list1)\n",
    "        removeList(list1)\n",
    "        print(\"List after removing the element\",list1)\n",
    "    elif choice==12:\n",
    "        ele=int(input(\"Enter an intger to add\\t\"))\n",
    "        print(\"List before adding the element\",list1)\n",
    "        addele(list1)\n",
    "        print(\"List after adding the element\",list1)\n",
    "    elif choice==13:\n",
    "        newList=[]\n",
    "        eler=int(input(\"Number of ele\"))\n",
    "        for i in range(0,eler):\n",
    "            element=int(input(\"elements\"))\n",
    "            newList.append(element)\n",
    "        print(newList)\n",
    "        list1.extend(newList)\n",
    "        print(\"List after Extend\",list1)\n",
    "    elif choice==14:\n",
    "        print(list1)\n",
    "    elif choice==15:\n",
    "        print(clearList(list1))\n",
    "    elif choice==16:\n",
    "        break\n",
    "        "
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
