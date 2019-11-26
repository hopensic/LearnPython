class Solution:
    def countCharacters(self, words: list, chars: str) -> int:
        # total = sum(len(x) for x in list(filter(lambda w: len(set(w) - c) == 0, words)))
        compared_list, len_compared = sorted(chars), len(chars)
        num_word = 0
        num_compared = 0
        ret_total = 0
        for word in words:
            sorted_word = sorted(word)
            le = len(word)
            num_word = 0
            num_compared = 0
            while True:
                if num_word == le or num_compared == len_compared: break
                if sorted_word[num_word] == compared_list[num_compared]:
                    num_word += 1
                    num_compared += 1
                    continue
                else:
                    num_compared += 1
                    while True:
                        if num_word == le or num_compared == len_compared: break
                        if sorted_word[num_word] == compared_list[num_compared]:
                            num_word += 1
                            num_compared += 1
                            break
                        else:
                            num_compared += 1

            if num_word == le:
                ret_total += le

        return ret_total


lst = ["pxlqovnbsgvqjzpfeidchzrodnbqfrccfydzjptukscjuatlsrcurepllxzyghhdepitqptlmfkhzxjgswaulxkfydhkilg",
       "uqklvqnlhdkwryjawkqfajfpbcnhglxlwxlaskxlytr", "jvgkxcdkxrvfahjkvhmfuyjzxtyxrsogbtsjybeaxugqymcr",
       "rgxditmosplnqvodtis", "jm",
       "ruqjwejuanjtiizcmbieobesnjnadzqvqumggblzmkxilgfarnxwpcawtkzxlvugibpidvwtikloeziuxqoi",
       "wxeyzrnbhlhwxecrgejsrawyulynvgtszwqqlihkcvckgcgtgpyqtkuwvjywmhpskaiwmpyarftqhnogxpith",
       "vdpbykqlihtpvfnqbrcjpggojqbalerohyitktuikbffvfatcnneuvbanjihiaorrjcdthntnrxebfhvshmpodmzhtwnasbm",
       "wgjstkoaojcesfdrllugmojwdmgeejyiqvshlowtktddattunarnohgvqsoskfmbrami", "ecwqxbawirvnxvsjybbebclaturorlcbpf",
       "gtjbaigvufrotlwfoqqolnjabnvtbcygtfcytinzpcjbvprdkdjawrcbthmxjrabimhhs",
       "cvzlbrvppkyxtjxzeglzwoagmpjnfxddbwolxmwdohgtfktgftzzkwpianslkpldyfzubtjczse", "neaw",
       "mxhmvkajofnmdiiduactlemcvpztscmsnrdhuhquxnnzywsrzxyplgbppiypxwcfbsnyzblaeifo",
       "krekecabfpufucjhqphjnibaeqdvdpmrfougdwugvoioqangdnxromwlxnfeydaneyazzclscqgdxlhhgnoqmslfflzqv",
       "klutvchxsceihfmzitgqakytesfjykribjhjzdruuoycjkwaghmmqkfrhkrtawudtjyjwqbyspamlegqjlwlj",
       "raykfkflqdzrpthdejetwolgciygwaktulkxemkdbbllkjxhnnafsms", "os",
       "xhchkcetmlprcdmrnalvkvgabxxnomphqpqhnddqhecogspbdebeoshvjgzvmqu",
       "jqtdysnpskktynxwmsfaabglagnqcllptvuyyqjwrmqaftenusmsahhhqubkwxltpr",
       "sulmwluiwvlroldpiyecaicwrawzwflokefqkdwmxejaovvpbflfdtviinbvvtlhhhefmgfsqs", "sxyhcckvyl",
       "vsaacsybcddxvuzkddjmuivsvtjyanpbydmkcwnkmxvsiantgkvkmqjysclsvd", "sxcghypulvmfqfunxj", "pozekufhlooosxpcggbi",
       "xzaoxzllcixfqbupqozmzrnugj", "j", "tgslwp",
       "ntrdkixexajlpjgmcbrqimwtqnzfrqjszeiuvrgzclerzmsnagzaxbredvlrmipzflrzusclckmxphc",
       "ifdflsywdfizpodsehrrifsvejcxarrxmxyjgbbvqyqvywncphzfmnxhybxpdcozfnzablfx",
       "uluhplzrsaehaqxfnbcmixueedevhirbwqdyztwaxnkogcauymxgcpabxekib", "agtfkinbdccoemxetbryzpluzlpyzicnfopphrxriqm",
       "pdympxpwvxwcqaxrvbvyqkrresrjgzgxuyfxtkgldtathokdbyfsqfmitmiyagtqgijaiazvsumeyutbbwxqdshquzrehn", "rqe",
       "sljsvenhhstnnngzqyo", "dezrzpgldeimxfoqajuhjctgvalwkhkjemjaxumxqmifglbizusuqlttxirpbqbuvauwy",
       "dkwpyezbmkcskoxxcgrxcewknqgdckjxfyzcmzqcbyeucxbqybxoldogtkmdknsrruvnlfqnpfx",
       "sjeftmjkuperfynbreycwhuoyqybticswblbrrpugzhlrmiedjqufnehevzqwtaebwvdswsz",
       "lolnfyliloqmhjmhhohdtgfajjfdjqpubslbsrwitbjmrcegdrdjzvonxaefdvdfcbqmaaks", "qhcoaiocjhuzywkirlblajgeapzajqsoa",
       "sxrmoqxqbtakuqwmrrkljmegbwbeqbywmlyuprwyhljzejbybxoumidpxdrohwdjoqycpxcmivaulnqzneydwqfsvcxgyyseuk", "yrowy",
       "dohrzkrzdjehpctnjrvhzojullsiucrhphshwxwicyzkvzbqrztic",
       "rmshnxtbhsdgkiijrmwulocdzjzpgfyimkjdthuzkhoqgkeawgwincubrloknocxwzgqqcxafksxgzh",
       "aymovnuhptozhkiyowbeguzlkmrwjnujgjbdne", "abc", "vxoigovwmqizmkwbkktqk", "uokwktdempzloaglvvkqstztmwzcmhgxtoua",
       "bzwjxqueazlzfojrkbqmhtwrvuwsnfcnylurnddpektekca", "qgndjgvzcyajhgmrrnhdywwdbmkhtthwcfiueuxfldanyrmccwcy"]
string = "figspbov"
s = Solution()
print(s.countCharacters(lst, string))
