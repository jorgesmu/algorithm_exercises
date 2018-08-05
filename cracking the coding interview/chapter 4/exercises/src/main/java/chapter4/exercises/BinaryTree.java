package chapter4.exercises;

import java.util.List;

public interface BinaryTree {
	public BinaryTree parent();
	public List<BinaryTree> childs();
	public void leftLeaf(BinaryTree tree);
	public void rightLeaf(BinaryTree tree);
	public Integer value(); // assume its a integer tree
}
