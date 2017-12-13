package chapter4.exercises;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Tree {
	private List<Tree> childs = new ArrayList<Tree>();
	private int value;
	
	public Tree(int value) {
		this.value = value;
	}
	
	void addChild(int value) {
		Tree child = new Tree(value);
		childs.add(child);
	}
	
	void addChild(Tree tree) {
		//  No limit on the number of childs
		childs.add(tree);
	}
	
	int value() {
		return this.value;
	}
	
	int level() {
		int maxChildLevel = 0;
		for(int childIndex=0; childIndex < childs.size(); childIndex++) {
			int childLevel = childs.get(childIndex).level();
			if (childLevel > maxChildLevel) {
				maxChildLevel = childLevel;
			}
		}
		return (maxChildLevel + 1);
	}
	
	boolean is_balanced() {
		// Just take in consideration that this implementation doesnt care about if subtrees are also balanced
		// it just consider if the root is balanced.
		if (childs.size() == 0)
			return true;
		List<Integer> childLevels = new ArrayList<Integer>();
		for(int childIndex=0; childIndex < childs.size(); childIndex++) {
			childLevels.add(childs.get(childIndex).level());
		}
		Collections.sort(childLevels); 
		return (childLevels.get(childLevels.size() -1) - childLevels.get(0)) < 1;	
	}
}
