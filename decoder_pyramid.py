'''
Prompt:
Decode an input.txt file made up of strs delimited by whitespace and newline. example:

    "3 love\ncomputers\n2 dogs\n4 cats\n1 I\n5 you"

Using encoded numbers given in a pyramid scheme of last number in each newline formatted like this:
       1
      2 3
     4 5 6

Result should be:

    "I love computers"

Explanation:
    Each "encoded number" corresponds to a word.
    1: "I", 3: "love", 6: "computers"
    Use each "encoded number" to create a str of words resulting in the "decoded msg"

'''

# input files
decoder_file= "3 love 6 computers 2 dogs 4 cats 1 I 5 you"
#decoder_file= "283 land 45 sun 149 too 258 huge 161 dont 224 such 169 noun 10 student 185 brown 41 complete 63 play 187 cook 160 yard 82 clock 300 would 179 plain 174 excite 273 fire 84 wish 22 cool 263 child 212 past 261 colony 248 oil 218 dog 292 back 89 money 70 kind 126 open 214 finger 86 touch 249 are 296 dad 122 am 256 modern 171 meant 206 ocean 231 pitch 250 suit 71 town 76 east 116 over 177 group 157 good 146 kind 164 down 4 band 56 especially 234 organ 298 of 180 fire 49 out 232 area 124 touch 123 happen 26 sat 130 electric 295 wrote 127 buy 15 lot 69 stop 11 corn 54 where 247 check 73 live 221 best 168 hold 286 cause 233 grand 6 present 79 indicate 46 counter 162 we 193 like 222 visit 251 state 139 morning 112 true 279 are 142 ball 190 history 34 seat 228 rain 227 less 25 glass 240 tone 37 song 128 fair 211 element 197 speed 57 produce 32 quotient 259 sand 290 begin 138 moment 24 offer 16 probable 235 all 163 necessary 147 post 35 cent 2 happen 8 speech 198 object 267 silver 297 third 36 crease 191 wait 111 triangle 219 idea 136 clothe 1 young 181 discuss 154 field 118 company 215 capital 132 compare 217 chart 141 possible 257 written 78 remember 119 mile 245 cold 196 lady 165 felt 153 against 96 skin 107 prepare 51 he 90 card 5 organ 274 object 47 our 159 major 60 discuss 3 system 266 hole 188 above 246 they 83 produce 148 straight 134 level 62 though 99 modern 59 dry 275 bought 91 milk 294 make 80 show 207 middle 291 center 184 blood 167 speak 74 prove 50 select 223 power 108 come 39 brown 21 experiment 28 strong 66 hurry 229 touch 30 reach 110 case 216 beat 129 over 143 dry 264 hill 55 company 203 opposite 131 work 238 field 158 felt 65 prepare 12 now 281 his 125 stay 64 toward 288 observe 102 time 194 stop 72 possible 284 card 271 prepare 262 current 93 compare 121 neighbor 178 thus 254 include 17 copy 14 bit 42 stead 100 does 101 general 77 solve 252 glad 106 duck 40 offer 88 happen 293 ball 276 bread 61 like 92 machine 287 come 109 any 226 band 58 it 202 section 282 close 23 heavy 205 produce 68 got 140 possible 18 insect 201 way 176 before 98 men 237 bird 270 ease 277 trade 172 winter 97 am 120 repeat 104 first 103 to 135 each 225 guide 53 column 156 single 43 remember 243 wild 236 major 242 coast 52 class 170 done 75 jump 67 sister 166 feel 239 check 269 fire 19 nine 210 indicate 189 parent 94 whole 289 her 173 the 209 temperature 260 design 175 big 208 skill 38 friend 278 hit 230 wait 48 instant 199 blow 113 about 244 chick 241 answer 137 man 200 material 255 current 85 think 253 print 95 nor 220 better 29 example 27 people 186 drink 44 gun 87 together 81 cost 150 require 155 or 9 people 7 planet 183 ease 114 ready 115 enough 33 sugar 299 deal 133 with 105 us 272 share 152 office 268 protect 265 low 213 thus 13 farm 280 oxygen 144 fire 117 force 195 select 285 paragraph 204 always 31 poem 20 chick 145 planet 151 fact 192 moment 182 term"


#convert decoder file to dict using comprehension
def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
    
#decode encoded file
def Decode(decoder):
    decoder_len = len(decoder)
    decoded_msg = ""
    
    iterator = 1
    for number in range(1, decoder_len):
        if number != 1:
            encoded_number = iterator + number
            iterator = encoded_number
        else:
            encoded_number = number
        
        decoded_msg += str(decoder.get(str(encoded_number))) + " "
        
        if encoded_number >= decoder_len:
            return decoded_msg

print (Decode(Convert(decoder_file.split())))
