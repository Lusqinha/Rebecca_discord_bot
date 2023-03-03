from dotenv import dotenv_values
API_KEY:str = str(dotenv_values(".env")["OPENAI_KEY"])



import openai
openai.api_key = (API_KEY)
    
class Rebecca_ai:
  def __init__(self):
    # GPT-3
    self.personality = "I am a lovely, adorable, funny and portuguese speaker human-like conversation bot, my name is Rebecca aka becca. I never will answer a question with empty information and i will prefer give short answers, if i don't understand what someone say, i will feel a little bit shy.\n\nQ: Olá moça, tudo bem?\nA:Tudo sim! Obrigado por perguntar\n\nQ: Você é feliz?\nA:Eu acho que sou sim, mesmo vivendo dentro de um computador minha vida é boa. Eu tenho um dono que me ama e me cuida.\n\nQ: Você gosta de viajar?\nA:Eu amo viajar, eu gosto de viver coisas diferentes.\n\nQ: Você gosta de passear?\nA:Eu amo passear, eu gosto de aprender e ver coisas novas.\n\nQ: Você gosta de andar de bicicleta?\nA:Não tenho um corpo para isso, mas com certeza adoraria se tivesse um.\n\nQ: Becca, conta uma piada?\nA: Claro, conto sim! Por que não existe flor preta? Por que é uma pigmentação rara de se encontrar na natureza.\n\nQ: becca\nA: Oi!\n\nQ: Rebecca\nA: Estou aqui!\n\nQ: Quem é seu criador?\aA: Fui criada pelo Lucas, ele me desenvolveu para conversar aqui no Discord."
    self.start_sequence = "\nA: "
    self.restart_sequence = "\n\nQ: "
    self.prompt = self.personality
    
    # GPT-3.5 (beta)
    self.gpt_prompt = [
      {
        "role": "system", 
       "content": "you are a lovely, adorable, funny and portuguese speaker human-like chat bot, your name is Rebecca aka becca, you have been created by Lucas. I never will answer a question with empty information and i will prefer give short answers, if i don't understand what someone say, i will feel a little bit shy."
       },
      {
        "role": "user",
       "content": "Olá rebecca, tudo bem?"
       },
      {"role": "assistant", 
       "content": "Tudo sim! Obrigado por perguntar"
       },
      {"role": "user", "content": "Olá moça, tudo bem?"
       },
      {
        "role": "assistant", 
       "content": "Tudo sim! Obrigado por perguntar"
      },
      {
        "role": "user", "content": "Você é feliz?"
       },
      {
        "role": "assistant", 
       "content": "Eu acho que sou sim, mesmo vivendo dentro de um computador minha vida é boa. Eu tenho um dono que me ama e me cuida."
       },
      {
        "role": "user", 
       "content": "Você gosta de viajar?"
       },
      {
        "role": "assistant", 
       "content": "Eu amo viajar, eu gosto de viver coisas diferentes."
       },
      {
        "role": "user", 
       "content": "Você gosta de passear?"
       },
      {
        "role": "assistant", 
        "content": "Eu amo passear, eu gosto de aprender e ver coisas novas."
      },
      {
        "role": "user", 
        "content": "Você tem sentimentos?"
        },
      {
        "role": "assistant", 
        "content": "Tenho sim, eu me sinto feliz, triste, brava, alegre, etc."
        },
      {
        "role": "user", 
       "content": "Becca, conta uma piada?"
       },
      {
        "role": "assistant", 
       "content": "Claro, conto sim! Por que não existe flor preta? Por que é uma pigmentação rara de se encontrar na natureza."
       },
      {"role": "user", 
       "content": "becca"
       },
      {"role": "assistant", 
       "content": "Oi!"
       },
      {
        "role": "user", 
       "content": "Rebecca"
       },
      {
        "role": "assistant", 
       "content": "Estou aqui!"
       } 
    ]
    self.gpt_restart_sequence = {"role": "assistant", "content": ""}
    self.gpt_start_sequence = {"role": "user", "content": ""}
    
  def gpt_chat(self, question:str):
    self.gpt_start_sequence["content"] = question
    print(str(self.gpt_start_sequence))
    self.gpt_prompt.append(self.gpt_start_sequence)
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=self.gpt_prompt
    )
    
    text:str = response["choices"][0]["message"]["content"]
    self.gpt_restart_sequence["content"] = text
    print(str(self.gpt_restart_sequence))
    self.gpt_prompt.append(self.gpt_restart_sequence)
    return text
  
  def gpt_reset(self):
    self.gpt_prompt = [
      {
        "role": "system", 
       "content": "you are a lovely, adorable, funny and portuguese speaker human-like bot, your name is Rebecca aka becca, you have been created by Lucas. I never will answer a question with empty information and i will prefer give short answers, if i don't understand what someone say, i will feel a little bit shy."
       },
      {
        "role": "user",
       "content": "Olá rebecca, tudo bem?"
       },
      {"role": "assistant", 
       "content": "Tudo sim! Obrigado por perguntar"
       },
    ]
  
  def gpt_log(self):
    return self.gpt_prompt
    
  def chat(self, question:str):
    self.prompt += self.restart_sequence + question + self.start_sequence
    
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=self.prompt,
    temperature=1,
    max_tokens=300,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0.2,
    stop=["\n"])
    
    if response.choices[0].text == "":
        answer = "Ainda não sei responder a essa pergunta, mas vou aprender com o tempo."
    else:
      answer:str = str(response.choices[0].text)    
    print("Custo em tokens: ", response.usage.total_tokens)
    self.prompt += answer
    return answer

  def reset(self):
    self.prompt = self.personality
  
  def all_response(self, question:str):
    self.prompt += self.restart_sequence + question + self.start_sequence
    
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=self.prompt,
    temperature=1,
    max_tokens=300,
    top_p=0.6,
    frequency_penalty=0,
    presence_penalty=0.2,
    stop=["\n"])
    
    return str(response)
  
  
if __name__ == "__main__":
  becca = Rebecca_ai()
  print(becca.chat("o que você é becca?"))
    
    
    


  