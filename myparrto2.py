from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")

''' 
uncomment to get reproducable paraphrase generations
def random_state(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

random_state(1234)
'''

parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")
phrases = ["I unable to access my facebook account",
           "What are the best courses available for learning Data Science? "
]

for phrase in phrases:
  print("-"*100)
  print("Input_phrase: ", phrase)
  print("-"*100)
  para_phrases =  para_phrases = parrot.rephrase(input_phrase=phrase,
                               use_gpu=False,
                               diversity_ranker="levenshtein",
                               do_diverse=True, 
                               max_length=32, 
                               adequacy_threshold = 0.99, 
                               fluency_threshold = 0.90)
  for para_phrase in para_phrases:
   print(para_phrase)
