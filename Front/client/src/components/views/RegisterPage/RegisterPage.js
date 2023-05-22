import React , {useState} from "react";
import moment from "moment";
import { Formik } from 'formik';
import * as Yup from 'yup';
import { registerUser } from "../../../_actions/user_actions";
import { useDispatch } from "react-redux";

import {
  Form,
  Input,
  Button,
} from 'antd';

const formItemLayout = {
  labelCol: {
    xs: { span: 24 },
    sm: { span: 8 },
  },
  wrapperCol: {
    xs: { span: 24 },
    sm: { span: 16 },
  },
};
const tailFormItemLayout = {
  wrapperCol: {
    xs: {
      span: 24,
      offset: 0,
    },
    sm: {
      span: 16,
      offset: 8,
    },
  },
};

function RegisterPage(props) {
  const dispatch = useDispatch();

  // const [rating1, setRating1] = useState(0) // initial rating value
  // const [rating2, setRating2] = useState(0)
  // const [rating3, setRating3] = useState(0)
  // const [rating4, setRating4] = useState(0)
  // const [total, settotal] = useState(10)
 
  // // Catch Rating value
  // const handleRating1 = (rate1) => {
  //   setRating1(rate1)
  //   // Some logic
  // }
  // const handleRating2 = (rate2) => {
  //   setRating2(rate2)
  //   // Some logic
  // }
  // const handleRating3 = (rate3) => {
  //   setRating3(rate3)
  //   // Some logic
  // }
  // const handleRating4 = (rate4) => {
  //   setRating4(rate4)
  //   // Some logic
  // }



  return (

    <Formik
      initialValues={{
        email: '',
        name: '',
        password: '',
        confirmPassword: '',
        cleanliness: '',
        convenience:'',
        kindness:'',
        position:''

      }}
      validationSchema={Yup.object().shape({
        name: Yup.string()
          .required('Name is required'),
        email: Yup.string()
          .email('Email is invalid')
          .required('Email is required'),
        password: Yup.string()
          .min(6, 'Password must be at least 6 characters')
          .required('Password is required'),
        confirmPassword: Yup.string()
          .oneOf([Yup.ref('password'), null], 'Passwords must match')
          .required('Confirm Password is required')
      })}
      onSubmit={(values, { setSubmitting }) => {
        setTimeout(() => {

          let dataToSubmit = {
            email: values.email,
            password: values.password,
            name: values.name,
            image: `http://gravatar.com/avatar/${moment().unix()}?d=identicon`
          };

          dispatch(registerUser(dataToSubmit)).then(response => {
            if (response.payload.success) {
              props.history.push("/login");
            } else {
              alert(response.payload.err.errmsg)
            }
          })

          setSubmitting(false);
        }, 500);
      }}
    >
      {props => {
        const {
          values,
          touched,
          errors,
          dirty,
          isSubmitting,
          handleChange,
          handleBlur,
          handleSubmit,
          handleReset,
        } = props;
        return (
          <div className="app">
            <h2>Sign up</h2>
            <Form style={{ minWidth: '375px' }} {...formItemLayout} onSubmit={handleSubmit} >

              <Form.Item required label="Name">
                <Input
                  id="name"
                  placeholder="Enter your name"
                  type="text"
                  value={values.name}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  className={
                    errors.name && touched.name ? 'text-input error' : 'text-input'
                  }
                />
                {errors.name && touched.name && (
                  <div className="input-feedback">{errors.name}</div>
                )}
              </Form.Item>


              <Form.Item required label="Email" hasFeedback validateStatus={errors.email && touched.email ? "error" : 'success'}>
                <Input
                  id="email"
                  placeholder="Enter your Email"
                  type="email"
                  value={values.email}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  className={
                    errors.email && touched.email ? 'text-input error' : 'text-input'
                  }
                />
                {errors.email && touched.email && (
                  <div className="input-feedback">{errors.email}</div>
                )}
              </Form.Item>

              <Form.Item required label="Password" hasFeedback validateStatus={errors.password && touched.password ? "error" : 'success'}>
                <Input
                  id="password"
                  placeholder="Enter your password"
                  type="password"
                  value={values.password}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  className={
                    errors.password && touched.password ? 'text-input error' : 'text-input'
                  }
                />
                {errors.password && touched.password && (
                  <div className="input-feedback">{errors.password}</div>
                )}
              </Form.Item>

              <Form.Item required label="Confirm" hasFeedback>
                <Input
                  id="confirmPassword"
                  placeholder="Enter your confirmPassword"
                  type="password"
                  value={values.confirmPassword}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  className={
                    errors.confirmPassword && touched.confirmPassword ? 'text-input error' : 'text-input'
                  }
                />
                {errors.confirmPassword && touched.confirmPassword && (
                  <div className="input-feedback">{errors.confirmPassword}</div>
                )}
              </Form.Item>


<h2> 중요하게 생각하는 요소에 0-4까지 점수를 주세요!</h2>
<h3 style={{position:'center'}}> (총 10점을 넘어가면 안됩니다.)</h3>

              <Form.Item required label="청결도" hasFeedback>
                <Input
                  id="cleanliness"
                  placeholder="0 to 4 score"
                  type="number"
                  value={values.cleanliness}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  className={
                    errors.cleanliness && touched.cleanliness ? 'text-input error' : 'text-input'
                  }
                />
                {errors.cleanliness && touched.cleanliness && (
                  <div className="input-feedback">{errors.cleanliness}</div>
                )}
              </Form.Item>

              <Form.Item required label="편의성" hasFeedback>
                <Input
                  id="convenience"
                  placeholder="0 to 4 score"
                  type="number"
                  value={values.convenience}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  className={
                    errors.convenience && touched.convenience ? 'text-input error' : 'text-input'
                  }
                />
                {errors.convenience && touched.convenience && (
                  <div className="input-feedback">{errors.convenience}</div>
                )}
              </Form.Item>

              <Form.Item required label="친절함" hasFeedback>
                <Input
                  id="kindness"
                  placeholder="0 to 4 score"
                  type="number"
                  value={values.kindness}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  className={
                    errors.kindness && touched.kindness ? 'text-input error' : 'text-input'
                  }
                />
                {errors.kindness && touched.kindness && (
                  <div className="input-feedback">{errors.kindness}</div>
                )}
              </Form.Item>

              <Form.Item required label="위치" hasFeedback>
                <Input
                  id="position"
                  placeholder="0 to 4 score"
                  type="number"
                  value={values.position}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  className={
                    errors.position && touched.position ? 'text-input error' : 'text-input'
                  }
                />
                {errors.position && touched.position && (
                  <div className="input-feedback">{errors.position}</div>
                )}
              </Form.Item>






              <Form.Item {...tailFormItemLayout}>
                <Button onClick={handleSubmit} type="primary" disabled={isSubmitting}>
                  Submit
                </Button>
              </Form.Item>
            </Form>
          </div>
        );
      }}
    </Formik>
  );
};


export default RegisterPage
