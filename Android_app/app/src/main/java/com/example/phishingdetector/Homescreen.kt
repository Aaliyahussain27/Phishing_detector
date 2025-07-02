package com.example.phishingdetector

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.phishingdetector.ui.theme.PhishingDetectorTheme
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response


@Composable
fun Homescreen(onNavigate: (String) -> Unit){
    var url by remember{ mutableStateOf("") }
    var isLoading by remember { mutableStateOf(false) }

    Column(modifier = Modifier
        .fillMaxSize(),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally) {

        OutlinedTextField(
            value = url,
            onValueChange = {url=it},
            label={ Text("Enter URL") })

        Spacer(modifier = Modifier
            .height(12.dp))

        Button(
            onClick = {
                isLoading = true

                val request = UrlRequest(url)

                RetrofitClient.instance.predictUrl(request)
                    .enqueue(object : Callback<UrlResponse> {
                        override fun onResponse(
                            call: Call<UrlResponse>,
                            response: Response<UrlResponse>
                        ) {
                            isLoading = false
                            val result = response.body()?.result ?: "error"
                            onNavigate(result)
                        }

                        override fun onFailure(call: Call<UrlResponse>, t: Throwable) {
                            isLoading = false
                            onNavigate("Error: ${t.message}")
                        }
                    })
            },
            enabled = !isLoading,
            shape = RoundedCornerShape(12.dp),
            modifier = Modifier.padding(12.dp)
        ) {
            Text(if (isLoading) "Checking..." else "Check")
        }
    }
}
