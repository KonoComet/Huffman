import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char #character A/G/T/C
        self.freq = freq #frequency
        self.left = None
        self.right = None
        
        #custom comparison
    def __lt__(self, other):
        return self.freq < other.freq

def calculate_nucleotide_frequency(filename="dna.txt"):
    with open(filename, 'r') as f:
        dna_sequence = f.read()
    return Counter(dna_sequence) #this will also count the frequency

#Help function to generate Huffman codes
def _generate_huffman_codes(node, current_code, huffman_codes):
    if node is None:
        return

    if node.char is not None:  # Leaf node
        huffman_codes[node.char] = current_code

    _generate_huffman_codes(node.left, current_code + "0", huffman_codes)
    _generate_huffman_codes(node.right, current_code + "1", huffman_codes)

def huffman_coding(freq_dict):
    priority_queue = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue) #make a min-heap in this point

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue) #pop out the lowest frequency node
        right = heapq.heappop(priority_queue) #again

        merged_node = Node(None, left.freq + right.freq) #A new merged node with a summed frequencies from left and right node
        merged_node.left = left #new left
        merged_node.right = right #new right

        heapq.heappush(priority_queue, merged_node) #merged nodes are added back until one left

    # Now traverse it to get Huffman codes
    root = priority_queue[0]
    codes = {} #for storing characters
    _generate_huffman_codes(root, "", codes) #traverse tree to codes
    return codes

#Encode the entire DNA sequence using Huffman codes and save to file
def encode_and_save_compressed(huffman_codes, filename="dna.txt", output_file="compressed.txt"):
    with open(filename, 'r') as f:
        dna_sequence = f.read()
    encoded_sequence = ''.join([huffman_codes[nucleotide] for nucleotide in dna_sequence])
    with open(output_file, 'w') as f:
        f.write(encoded_sequence)

if __name__ == "__main__":
    #freq_dict = calculate_nucleotide_frequency()
    #huffman_codes = huffman_coding(freq_dict)
    #encode_and_save_compressed(huffman_codes)
    
    dna_sequence = "AAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATTAAACGATATACGATATT"

    freq_dict = Counter(dna_sequence)

    huffman_codes = huffman_coding(freq_dict)

    encoded_sequence = ''.join([huffman_codes[nucleotide] for nucleotide in dna_sequence])

    print("Frequencies:", freq_dict)
    print("Huffman:", huffman_codes)
    print("Compressed:", encoded_sequence)

