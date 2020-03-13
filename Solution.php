<?php


/**
 * Class Solution
 * https://leetcode.com/
 */
class Solution
{


  /**
   * 2. Add Two Numbers
   * https://leetcode.com/problems/add-two-numbers/
   *
   * @param ListNode $l1
   * @param ListNode $l2
   * @return ListNode
   */
  function addTwoNumbers(ListNode $l1, ListNode $l2): ListNode
  {
    $sum=self::getInt($l1)+self::getInt($l2);
    return self::getListNode($sum);
  }

  /**
   * For
   * 2. Add Two Numbers
   * https://leetcode.com/problems/add-two-numbers/
   *
   * @param int $intVal
   * @return ListNode
   */
  static function getListNode(int $intVal): ListNode
  {
    $strVal = (string)$intVal;
    $arrVal = str_split($strVal);
    $listNode=null;
    foreach ($arrVal as $val) {
      if (isset($listNode)) {
        $listNodeNext=$listNode;
        $listNode = new ListNode($val);
        $listNode->next=$listNodeNext;
      } else {
        $listNode = new ListNode($val);
      }
    }
    return $listNode;
  }

  /**
   * For
   * 2. Add Two Numbers
   * @param ListNode $listNode
   * @return int
   */
  static function getInt(ListNode $listNode): int{
    $arrInt=[];
    while($listNode){
      $arrInt[]=$listNode->val;
      $listNode=$listNode->next;
    }
    $arrInt=array_reverse($arrInt);
    return (int)implode('',$arrInt);
  }


  /**
   * 1. Two Sum
   * https://leetcode.com/problems/two-sum/
   * @param Integer[] $nums
   * @param Integer $target
   * @return Integer[]
   */
  function twoSum(array $nums, int $target)
  {

    foreach ($nums as $k1 => $num1) {
      foreach ($nums as $k2 => $num2) {
        if ($num1 + $num2 == $target && $k1 != $k2) {
          return [$k1, $k2];
        }
      }
    }
    return [];
  }

  /**
   * 4 Median of Two Sorted Arrays
   * https://leetcode.com/problems/median-of-two-sorted-arrays/
   * @param Integer[] $nums1
   * @param Integer[] $nums2
   * @return Float
   */
  function findMedianSortedArrays(array $nums1, array $nums2): float
  {
    $numAll = array_merge($nums1, $nums1);

    //echo "asdfsadfsa";
    print_r($nums1);
    print_r($nums1);

    print_r($numAll);

    //var_dump($nums1);
    sort($numAll);
    return 0;
  }


}

/**
 * 2. Add Two Numbers
 * https://leetcode.com/problems/add-two-numbers/
 * Class ListNode
 */
class ListNode
{
  public $val = 0;
  public $next = null;

  function __construct($val)
  {
    $this->val = $val;
  }
}
