/**
 * Created by Jianyu Zhou on 2017/3/12.
 */
import edu.stanford.nlp.ie.AbstractSequenceClassifier;
import edu.stanford.nlp.ie.crf.*;
import edu.stanford.nlp.io.IOUtils;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.sequences.DocumentReaderAndWriter;
import edu.stanford.nlp.util.Triple;
import jdk.nashorn.api.scripting.JSObject;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class ChineseQAGenerator {
    //public String []
    public final String basedir = "E:\\Graduation-Project\\dataset\\stanford-segmenter-2016-10-31\\data";
    Properties props = new Properties();
    CRFClassifier<CoreLabel> segmenter;
    List<String> contexts = new ArrayList<>();
    List<QA> qas = new ArrayList<>();

    public ChineseQAGenerator(){
        props.setProperty("sighanCorporaDict",basedir);
        props.setProperty("serDictionary", basedir + "\\dict-chris6.ser.gz");
        props.setProperty("inputEncoding", "UTF-8");
        props.setProperty("sighanPostProcessing", "true");
        segmenter = new CRFClassifier<>(props);
        segmenter.loadClassifierNoExceptions(basedir+"\\ctb.gz",props);
    }

    public List<String> word_split(String sentence){
        return segmenter.segmentString(sentence);
    }

    public String[] sentence_split(String context){
        String[] sentences = context.split("。");
        for(int i = 0;i<sentences.length;i++){
            sentences[i]+="。";
        }
        return sentences;
    }

    public String combine_word(List<String> words){
        String space_seged_sentence = "";
        for(int i = 0;i<words.size();i++){
            space_seged_sentence+=words.get(i)+" ";
        }
        return space_seged_sentence.trim();
    }

    public void readContexts(String filePath)throws FileNotFoundException,IOException{
        FileReader fr = new FileReader(filePath);
        BufferedReader bf = new BufferedReader(fr);
        String line = null;
        while((line = bf.readLine())!=null){
            contexts.add(line);
        }
    }

    public void generateQA(AbstractSequenceClassifier<CoreLabel> classifier){
        for(int i = 0;i<contexts.size();i++){
            String seged_context = combine_word(word_split(contexts.get(i)));
            QA tmp = new QA(contexts.get(i),seged_context);
            String[] sentences = sentence_split(contexts.get(i));
            for(int j = 0;j<sentences.length;j++){
                String seged_sentence = combine_word(word_split(sentences[j]));
                List<Triple<String,Integer,Integer>> triples = classifier.classifyToCharacterOffsets(seged_sentence);
                for(Triple<String,Integer,Integer>trip:triples){
                    tmp.add_cloze(seged_sentence.substring(0,trip.second)+"["+trip.first+"]"+seged_sentence.substring(trip.third));
                }
            }
            List<Triple<String,Integer,Integer>> triples = classifier.classifyToCharacterOffsets(seged_context);
            for(Triple<String,Integer,Integer>trip:triples){
                tmp.add_answer_index(trip.second,trip.third,seged_context.substring(trip.second,trip.third));
            }
            if(tmp.raw_clozes.size() == tmp.candidate_answers.size()){
                tmp.randomChoose(3);
                qas.add(tmp);
            }
        }
    }

    public void write(String fileName)throws FileNotFoundException,IOException{
        FileWriter fw  = new FileWriter(fileName);
        BufferedWriter bw = new BufferedWriter(fw);
        JSONArray cs = new JSONArray();
        for(int i = 0;i<qas.size();i++){
            JSONObject c = new JSONObject();
            c.put("context",qas.get(i).context);
            JSONArray qaList = new JSONArray();
            for(int j = 0;j<qas.get(i).raw_clozes.size();j++){
                JSONObject qa = new JSONObject();
                qa.put("question",qas.get(i).raw_clozes.get(j));
                qa.put("answer",qas.get(i).candidate_answers.get(j));
                qa.put("start",qas.get(i).answer_index_pairs.get(j).start);
                qa.put("end",qas.get(i).answer_index_pairs.get(j).end);
                qaList.add(qa);
            }
            c.put("qas",qaList);
            cs.add(c);
        }
        JSONObject all = new JSONObject();
        all.put("data",cs);
        bw.write(all.toString());
    }
    public static void main(String[] args) throws Exception {
        ChineseQAGenerator qag= new ChineseQAGenerator();
        String outFileName = "qa-json";
        String serializedClassifier = "E:\\Graduation-Project\\dataset\\stanford-ner-2016-10-31\\classifiers\\chinese.misc.distsim.crf.ser.gz";
        AbstractSequenceClassifier<CoreLabel> classifier = CRFClassifier.getClassifier(serializedClassifier);
        qag.readContexts("E:\\Graduation-Project\\dataset\\baidubaike-pop_star");
        qag.generateQA(classifier);
        qag.write(outFileName);
    }
}
