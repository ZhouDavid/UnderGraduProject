import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Vector;

/**
 * Created by Jianyu Zhou on 2017/3/12.
 */
class IndexPair{
    Integer start;
    Integer end;
    IndexPair(Integer start,Integer end){this.start = start;this.end = end;}
}
public class QA {
    public List<String> questions = new ArrayList<>();
    public List<String> raw_clozes = new ArrayList<>();  //原始挖了空的陈述句
    public String context;  //答案存在的段落
    public String seged_context;  //分过词的context
    public List<IndexPair> answer_index_pairs = new ArrayList<>();
    public List<String> candidate_answers = new ArrayList<>(); //答案，短文本

    public QA(String context,String seged_context){
        this.context = context;
        this.seged_context = seged_context;
    }

    public void add_cloze(String cloze){raw_clozes.add(cloze);}

    public void add_answer_index(Integer start,Integer end,String answer){
        answer_index_pairs.add(new IndexPair(start,end));
        candidate_answers.add(answer);
    }

    public void randomChoose(int qaNum){
        qaNum = qaNum<raw_clozes.size()?qaNum:raw_clozes.size();
        Random ra = new Random();
        int[] qaIndex = new int[qaNum];
        for(int i = 0;i<qaNum;i++){
            qaIndex[i] = ra.nextInt(raw_clozes.size());
        }
        List<String>tmp_raw_clozes=  new ArrayList<>();
        List<IndexPair>tmp_index_pair = new ArrayList<>();
        List<String>tmp_candidate_answers = new ArrayList<>();
        for(int i = 0;i<qaIndex.length;i++){
            tmp_raw_clozes.add(raw_clozes.get(i));
            tmp_index_pair.add(answer_index_pairs.get(i));
            tmp_candidate_answers.add(candidate_answers.get(i));
        }
        raw_clozes = tmp_raw_clozes;
        answer_index_pairs = tmp_index_pair;
        candidate_answers = tmp_candidate_answers;
    }
    public void convert2questions(){}
}
