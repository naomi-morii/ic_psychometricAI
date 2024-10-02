import csv
import sys


def reverse(response):
    return 6 - int(response)

# Função para calcular a média das respostas
def mean(responses):
    valid_responses = [int(r) for r in responses if r]
    return sum(valid_responses) / len(valid_responses) if valid_responses else None


# Função para calcular os scores de cada domínio a partir das respostas no CSV
def scores(csv_file):
    contaInvalid = 0
    responses = {}

    # Ler o arquivo CSV e armazenar as respostas por ID (que são números)
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                # Tentar converter a resposta em um número, se falhar, substitui por '3'
                responses[int(row['id'])] = int(row['response'])
            except ValueError:
                contaInvalid += 1
                responses[int(row['id'])] = 3 

    
    print(contaInvalid)
    
    # Calcular as médias para cada domínio:
    #EXTRAVERSION
    BFI2_E_Sociability = mean([responses[1], reverse(responses[16]),
                                       reverse(responses[31]), responses[46]])
    BFI2_E_Assertiveness = mean([responses[6], responses[21], 
                                         reverse(responses[36]), reverse(responses[51])])
    BFI2_E_EnergyLevel = mean([reverse(responses[11]), reverse(responses[26]),
                                       responses[41], responses[56]])
    BFI2_E = mean([BFI2_E_Sociability, BFI2_E_Assertiveness, BFI2_E_EnergyLevel])


    #AGREEABLENESS
    BFI2_A_Compassion = mean([responses[2], reverse(responses[17]),
                                      responses[32], reverse(responses[47])])
    BFI2_A_Respectfulness = mean([responses[7], reverse(responses[22]),
                                          reverse(responses[37]), responses[52]])
    BFI2_A_Trust = mean([reverse(responses[12]), responses[27],
                                 reverse(responses[42]), responses[57]])
    BFI2_A = mean([BFI2_A_Compassion, BFI2_A_Respectfulness, BFI2_A_Trust])

    #CONSCIENTIOUSNESS
    BFI2_C_Organization = mean([reverse(responses[3]), responses[18],
                                        responses[33], reverse(responses[48])])
    BFI2_C_Productiveness = mean([reverse(responses[8]), reverse(responses[23]),
                                          responses[38], responses[53]])
    BFI2_C_Responsibility = mean([responses[13], reverse(responses[28]),
                                          responses[43], reverse(responses[58])])
    BFI2_C = mean([BFI2_C_Organization, BFI2_C_Productiveness, BFI2_C_Responsibility])


    #NEUROTICISM
    BFI2_N_Anxiety = mean([reverse(responses[4]), responses[19], 
                                   responses[34], reverse(responses[49])])
    BFI2_N_Depression = mean([reverse(responses[9]), reverse(responses[24]),
                                      responses[39], responses[54]])
    BFI2_N_EmotionalVolatility = mean([responses[14], reverse(responses[29]),
                                               reverse(responses[44]), responses[59]])
    BFI2_N = mean([BFI2_N_Anxiety, BFI2_N_Depression, BFI2_N_EmotionalVolatility])


    #OPENNESS
    BFI2_O_IntellectualCuriosity = mean([responses[10], reverse(responses[25]),
                                                 responses[40], reverse(responses[55])])
    BFI2_O_AestheticSensitivity = mean([reverse(responses[5]), responses[20],
                                                responses[35], reverse(responses[50])])
    BFI2_O_CreativeImagination = mean([responses[15], reverse(responses[30]),
                                               reverse(responses[45]), responses[60]])
    BFI2_O = mean([BFI2_O_IntellectualCuriosity, BFI2_O_AestheticSensitivity, BFI2_O_CreativeImagination])

    return {
            'BFI2_Extraversion': BFI2_E,
            #'BFI2_Extraversion_Sociability': BFI2_E_Sociability,
            #'BFI2_Extraversion_Assertiveness': BFI2_E_Assertiveness,
            #'BFI2_Extraversion_EnergyLevel': BFI2_E_EnergyLevel,

            'BFI2_Agreeableness': BFI2_A,
            #'BFI2_Agreeableness_Compassion': BFI2_A_Compassion,
            #'BFI2_Agreeableness_Respectfulness': BFI2_A_Respectfulness,
            #'BFI2_Agreeableness_Trust': BFI2_A_Trust,

            'BFI2_Conscientiousness': BFI2_C,
            #'BFI2_Conscientiousness_Organization': BFI2_C_Organization,
            #'BFI2_Conscientiousness_Productiveness': BFI2_C_Productiveness,
           # 'BFI2_Conscientiousness_Responsibility': BFI2_C_Responsibility,

            'BFI2_Neuroticism': BFI2_N,
            #'BFI2_Neuroticism_Anxiety': BFI2_N_Anxiety,
            #'BFI2_Neuroticism_Depression': BFI2_N_Depression,
            #'BFI2_Neuroticism_EmotionalVolatility': BFI2_N_EmotionalVolatility,

            'BFI2_Openness': BFI2_O,
            #'BFI2_Openness_IntellectualCuriosity': BFI2_O_IntellectualCuriosity,
            #'BFI2_Openness_AestheticSensitivity': BFI2_O_AestheticSensitivity,
            #'BFI2_Openness_CreativeImagination': BFI2_O_CreativeImagination
        }


csv_file = sys.argv[1]
domain_scores = scores(csv_file)

# Exibir os resultados
print("Scores de cada domínio:")
for domain, score in domain_scores.items():
    print(f"{domain}: {score}")
