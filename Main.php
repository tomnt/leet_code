<?php
include_once 'Solution.php';

class Main
{
  function __construct()
  {
    $s = new Solution();

    // 1 Two Sum
    print_r($s->twoSum([2,7,11,15],9));
    //print_r($s->twoSum([3, 2, 4], 6));

    // 2. Add Two Numbers
    // https://leetcode.com/problems/add-two-numbers/

    //print_r($s->addTwoNumbers(Solution::getListNode(342),Solution::getListNode(465)));

    //$listNode=Solution::getListNode(1000000000000000000000000000001);
    //$intVal=Solution::getInt($listNode);

    //print_r($intVal);



    // 4 Median of Two Sorted Arrays
    //echo $s->findMedianSortedArrays([1,3],[2]);

  }
}

new Main();
