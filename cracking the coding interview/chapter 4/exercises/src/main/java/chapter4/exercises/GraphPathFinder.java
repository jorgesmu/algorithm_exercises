package chapter4.exercises;

import java.util.ArrayList;
import java.util.List;

public class GraphPathFinder {
	boolean find(Graph startingNode, int targetId){
		List<Integer> visited = new ArrayList<Integer>();
		List<Graph> edgesQueue = new ArrayList<Graph>();
		visited.add(startingNode.id());
		edgesQueue.add(startingNode);
		
		while (edgesQueue.size() > 0){
			Graph currentNode = edgesQueue.remove(0);
			
			if (currentNode.id() == targetId){
				return true;
			}

			for (int i=0; i < currentNode.edges().size();i++){
				Graph edgeNode = currentNode.edges().get(i);
				if (!visited.contains(edgeNode.id())){
					edgesQueue.add(edgeNode);
				}
			}
		}
		return false;
	}

}
