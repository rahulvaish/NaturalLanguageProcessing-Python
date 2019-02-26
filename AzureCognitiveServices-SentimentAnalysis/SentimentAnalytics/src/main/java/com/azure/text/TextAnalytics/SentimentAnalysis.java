package com.azure.text.TextAnalytics;


import java.net.URI;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

public class SentimentAnalysis 
{
    public static void main(String[] args) 
    {
        HttpClient httpclient = HttpClients.createDefault();

        try
        {
            URIBuilder builder = new URIBuilder("https://centralus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment");


            URI uri = builder.build();
            HttpPost request = new HttpPost(uri);
            request.setHeader("Content-Type", "application/json");
            request.setHeader("Ocp-Apim-Subscription-Key", "bc8ead63c7bf4269aa9c0c6f7d64a775");


            // Request body
            StringEntity reqEntity = new StringEntity("{ \"documents\": [\r\n" + 
            		"            {\r\n" + 
            		"                \"language\": \"en\",\r\n" + 
            		"                \"id\": \"1\",\r\n" + 
            		"                \"text\": \"I am very sad. I am very happy\"\r\n" + 
            		"            }\r\n" + 
            		"            ]}");
            request.setEntity(reqEntity);

            HttpResponse response = httpclient.execute(request);
            HttpEntity entity = response.getEntity();

            if (entity != null) 
            {
                System.out.println(EntityUtils.toString(entity));
            }
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
