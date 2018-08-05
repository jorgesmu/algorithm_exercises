package chapter4.exercises;

import java.util.ArrayList;
import java.util.List;

public class Graph {
	List<Graph> edges = new ArrayList <Graph>();
	int id;

	public Graph (int id) {
		this.id = id;
	}
	
	void addEdge (Graph graph) {
		edges.add(graph);	
	}
	
	List<Graph> edges(){
		return this.edges; 
	}
	
	public int id(){
		return this.id; 
	}

}
