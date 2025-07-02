package com.example.phishingdetector

import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.Headers
import retrofit2.http.POST

data class UrlRequest(val url: String)
data class UrlResponse(val result: String)

interface ApiService {
    @Headers("Content-Type: application/json")
    @POST("/predict")
    fun predictUrl(@Body request: UrlRequest): Call<UrlResponse>
}
