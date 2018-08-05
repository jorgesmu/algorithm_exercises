package chapter4.exercises;

public class excersice4_5 {
	// Lets assume its a integer number, it could be extended to anything comparable
	public Integer next(BinaryTree tree, Integer initialValue) {
		if (tree == null) {
			return null;
		}
		if (tree.value() > initialValue) {
			return tree.value();
		}
		return next(tree.parent(), initialValue);
	}
}
