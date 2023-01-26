package com.example;

import java.io.*;
import java.util.Base64;

public class 图片转base64再转回图片 {
    protected static String imageToBase64Str(String imgFile) {
        String strRet = "";

        InputStream inputStream = null;
        byte[] data = null;
        try {
            inputStream = new FileInputStream(imgFile);
            data = new byte[inputStream.available()];
            System.out.println(data.length);
            inputStream.read(data);
            inputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        org.apache.commons.codec.binary.Base64 encoder = new org.apache.commons.codec.binary.Base64();
        strRet = encoder.encodeAsString(data);

        return strRet;
    }

    /**
     * @param imgStr base64编码字符串
     * @param path   图片路径-具体到文件
     * @return
     * @Description: 将base64编码字符串转换为图片
     * @Author:
     * @CreateTime:
     */
    public static boolean generateImage(String imgStr, String path) {
        if(imgStr == null){
            return false;
        }
        Base64.Decoder decoder = Base64.getDecoder();
        try{
            byte[] b = decoder.decode(imgStr);
            for (int i = 0;i<b.length;++i){
                if(b[i]<0){
                    b[i]+=256;
                }
            }
            OutputStream out = new FileOutputStream(path);
            out.write(b);
            out.flush();
            out.close();
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }

    public static void main(String[] args) throws IOException {
        String picBase = imageToBase64Str("dataset/pic/21.jpg");
        System.out.println(picBase.length());
        try {
            BufferedWriter out = new BufferedWriter(new FileWriter("pic2base64.txt"));
            out.write(picBase);
            out.close();
            System.out.println("文件创建成功！");
        } catch (IOException e) {

        }
        try {
            BufferedReader in = new BufferedReader(new FileReader("pic2base64.txt"));
            String str;
            while ((str = in.readLine()) != null) {
                System.out.println(str);
                System.out.println(generateImage(str,"base642pic.jpg"));
            }
        } catch (IOException e) {

        }

        /*
        String name = "47_1.jpg";
        String[] lastName = name.split(".jpg");
        System.out.println(lastName[0]);
        for(int i = 0;i < lastName.length;i++){
            System.out.println(lastName[i].toString());
        }

         */


    }
}
