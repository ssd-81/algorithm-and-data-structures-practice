/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/
class Solution {
    public Node cloneGraph(Node node) {
        if(node == null) {return null;}
        Map<Node, Node> cloned = new HashMap<>();
        return clone(node, cloned);
    }

    private Node clone(Node node, Map<Node, Node> cloned){
        if(cloned.containsKey(node)) return cloned.get(node);

        Node newNode = new Node(node.val);
        cloned.put(node, newNode);
        for(Node neighbor: node.neighbors){
            newNode.neighbors.add(clone(neighbor, cloned));
        }
        
    
        return newNode;
    }


}