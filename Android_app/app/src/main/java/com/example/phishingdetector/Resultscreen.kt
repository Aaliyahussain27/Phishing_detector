package com.example.phishingdetector

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.phishingdetector.ui.theme.PhishingDetectorTheme

@Composable
fun Resultscreen(prediction: String, onBack: () -> Unit) {
    Column(modifier=Modifier
        .fillMaxSize()
        .padding(20.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ){
        Text(
            text = "Result",
            fontSize = 30.sp,
            fontFamily = FontFamily.Serif,
            modifier = Modifier
                .padding(bottom = 12.dp)
        )

        Text(
            text=prediction,
            fontSize=38.sp,
            fontFamily = FontFamily.Serif,
            fontWeight = FontWeight.Bold,
            modifier = Modifier
                .padding(bottom=12.dp)
        )

        Button(onClick=onBack){
            Text("Previous Screen")
        }
    }
}
