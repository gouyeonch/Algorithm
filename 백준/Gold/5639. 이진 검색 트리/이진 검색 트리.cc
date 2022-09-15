#include <iostream>

using namespace std;

typedef struct TreeNode *nodeptr;
struct TreeNode
{
	int key;
	nodeptr left;
	nodeptr right;
};

nodeptr insert(nodeptr node, int data) 
{
	if (node == NULL) {
		node = new TreeNode;
		node->key = data;
		node->left = node->right = NULL;
	}
	else if (data <= node->key)
		node->left = insert(node->left, data);
	else
		node->right = insert(node->right, data);
	return node;
}

void printbst(nodeptr node)
{
	if (node->left != NULL)
		printbst(node->left);
	if (node->right != NULL)
		printbst(node->right);
	cout << node->key << endl;
}

int main()
{
	int key;
	nodeptr root=NULL;

	while(scanf("%d",&key)!=EOF) {
		root = insert(root, key);
	}
	
	printbst(root);
	
	return 0;
}