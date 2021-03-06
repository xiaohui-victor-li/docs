/*
 * QES Quant Service API
 * QES Quant Service API provides easy access to Risk/Optimization API 
 *
 * OpenAPI spec version: 0.0.4
 * Contact: luo.qes@wolferesearch.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * RiskModel
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-01-22T20:31:04.892Z")
public class RiskModel {
  @SerializedName("uuid")
  private String uuid = null;

  @SerializedName("template")
  private String template = null;

  @SerializedName("dateCreated")
  private String dateCreated = null;

  public RiskModel uuid(String uuid) {
    this.uuid = uuid;
    return this;
  }

   /**
   * Unique id of the risk model
   * @return uuid
  **/
  @ApiModelProperty(value = "Unique id of the risk model")
  public String getUuid() {
    return uuid;
  }

  public void setUuid(String uuid) {
    this.uuid = uuid;
  }

  public RiskModel template(String template) {
    this.template = template;
    return this;
  }

   /**
   * Template used for risk model
   * @return template
  **/
  @ApiModelProperty(value = "Template used for risk model")
  public String getTemplate() {
    return template;
  }

  public void setTemplate(String template) {
    this.template = template;
  }

  public RiskModel dateCreated(String dateCreated) {
    this.dateCreated = dateCreated;
    return this;
  }

   /**
   * Date on which riks model was created
   * @return dateCreated
  **/
  @ApiModelProperty(value = "Date on which riks model was created")
  public String getDateCreated() {
    return dateCreated;
  }

  public void setDateCreated(String dateCreated) {
    this.dateCreated = dateCreated;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RiskModel riskModel = (RiskModel) o;
    return Objects.equals(this.uuid, riskModel.uuid) &&
        Objects.equals(this.template, riskModel.template) &&
        Objects.equals(this.dateCreated, riskModel.dateCreated);
  }

  @Override
  public int hashCode() {
    return Objects.hash(uuid, template, dateCreated);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RiskModel {\n");
    
    sb.append("    uuid: ").append(toIndentedString(uuid)).append("\n");
    sb.append("    template: ").append(toIndentedString(template)).append("\n");
    sb.append("    dateCreated: ").append(toIndentedString(dateCreated)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

